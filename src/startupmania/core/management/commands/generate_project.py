import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = 'Generates a new Django project with selected apps'

    def add_arguments(self, parser):
        parser.add_argument('project_name', type=str, help='Name of the project to create')
        parser.add_argument('--apps', nargs='+', type=str, help='List of apps to include')

    def handle(self, *args, **options):
        project_name = options['project_name']
        selected_apps = options['apps'] or []
        
        # Create new Django project
        os.system(f'django-admin startproject {project_name}')
        
        # Copy selected apps
        for app in selected_apps:
            src = os.path.join(settings.BASE_DIR, 'app_templates', app)
            dest = os.path.join(project_name, app)
            if os.path.exists(src):
                shutil.copytree(src, dest)
        
        # Update settings.py
        self.update_settings(project_name, selected_apps)
        
        # Generate Docker files
        self.generate_docker_files(project_name)
        
        # Generate requirements.txt
        self.generate_requirements(project_name, selected_apps)
        
        # Update URLs
        self.update_urls(project_name, selected_apps)

    def update_settings(self, project_name, apps):
        settings_path = os.path.join(project_name, project_name, 'settings.py')
        with open(settings_path, 'r+') as f:
            content = f.read()
            
            # Add to INSTALLED_APPS
            installed_apps = "INSTALLED_APPS = [\n"
            for app in apps:
                installed_apps += f"    '{app}.apps.{app.title()}Config',\n"
            content = content.replace("INSTALLED_APPS = [", installed_apps)
            
            # Add environment variables
            env_content = "\nfrom dotenv import load_dotenv\nload_dotenv()\n"
            content = env_content + content
            
            # Update database config
            db_config = """
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
"""
            content = content.replace("DATABASES = {", db_config)
            
            f.seek(0)
            f.write(content)
            f.truncate()

    def generate_docker_files(self, project_name):
        # Create Dockerfile
        dockerfile_content = """FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "%s.wsgi"]
""" % project_name
        with open(os.path.join(project_name, 'Dockerfile'), 'w') as f:
            f.write(dockerfile_content)
        
        # Create docker-compose.yml
        compose_content = """version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DB_NAME=${DB_NAME}
      - DB_USER=${DB_USER}
      - DB_PASSWORD=${DB_PASSWORD}
      - DB_HOST=db
      - DB_PORT=5432
    depends_on:
      - db

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=${DB_NAME}
      - POSTGRES_USER=${DB_USER}
      - POSTGRES_PASSWORD=${DB_PASSWORD}
"""
        with open(os.path.join(project_name, 'docker-compose.yml'), 'w') as f:
            f.write(compose_content)
        
        # Create .env file
        env_content = """DEBUG=False
SECRET_KEY=your-secret-key-here
DB_NAME=startupdb
DB_USER=startupuser
DB_PASSWORD=startuppassword
DB_HOST=db
DB_PORT=5432
"""
        with open(os.path.join(project_name, '.env'), 'w') as f:
            f.write(env_content)

    def generate_requirements(self, project_name, apps):
        base_reqs = """Django==4.0.3
gunicorn==20.1.0
psycopg2-binary==2.9.3
python-dotenv==0.19.2
"""
        app_reqs = set()
        for app in apps:
            req_path = os.path.join(project_name, app, 'requirements.txt')
            if os.path.exists(req_path):
                with open(req_path) as f:
                    app_reqs.update(f.read().splitlines())
        
        with open(os.path.join(project_name, 'requirements.txt'), 'w') as f:
            f.write(base_reqs + '\n'.join(app_reqs))

    def update_urls(self, project_name, apps):
        urls_path = os.path.join(project_name, project_name, 'urls.py')
        imports = "\n".join([f"from {app} import urls as {app}_urls" for app in apps])
        path_includes = "\n".join([f"    path('{app}/', include({app}_urls))," for app in apps])
        
        urls_content = f"""from django.contrib import admin
from django.urls import path, include
{imports}

urlpatterns = [
    path('admin/', admin.site.urls),
{path_includes}
]
"""
        with open(urls_path, 'w') as f:
            f.write(urls_content)