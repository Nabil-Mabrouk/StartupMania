from celery import shared_task
from .project_generator import generate_project
from .deployer import deploy_project

@shared_task
def create_project_task(project_name, apps, deploy_info=None):
    project_path = generate_project(project_name, apps)
    if deploy_info:
        deploy_project(
            project_path,
            deploy_info['host'],
            deploy_info['username'],
            deploy_info['key_path']
        )
    return project_path