import os
import shutil
import subprocess
from django.conf import settings

def generate_project(project_name, selected_apps):
    project_path = os.path.join(settings.BASE_DIR, 'generated_projects', project_name)
    
    # Create project structure
    subprocess.run([
        'django-admin', 'startproject', project_name, project_path
    ], check=True)

    # Copy selected apps
    for app in selected_apps:
        src = os.path.join(settings.APP_TEMPLATES_ROOT, app)
        dest = os.path.join(project_path, app)
        if os.path.exists(src):
            shutil.copytree(src, dest)

    # Update settings
    update_settings(project_path, selected_apps)
    
    # Create Docker files
    create_docker_files(project_path)
    
    return project_path

def update_settings(project_path, apps):
    # Similar to previous settings update logic
    # Add security middleware, allowed hosts, etc.
    pass

def create_docker_files(project_path):
    # Dockerfile and docker-compose generation
    pass