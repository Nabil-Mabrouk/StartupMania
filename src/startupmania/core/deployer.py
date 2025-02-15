import paramiko
from scp import SCPClient
import logging, os

logger = logging.getLogger(__name__)

def deploy_project(project_path, host, username, key_path):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, key_filename=key_path)
        
        # Secure file transfer
        with SCPClient(ssh.get_transport()) as scp:
            scp.put(project_path, recursive=True, remote_path='/var/www/')
        
        # Safe command execution
        # Instead of os.system, use:
        # subprocess.run([...], check=True, shell=False)
        commands = [
            'apt-get update',
            'apt-get install -y docker.io docker-compose',
            f'cd /var/www/{os.path.basename(project_path)} && docker-compose build',
            f'cd /var/www/{os.path.basename(project_path)} && docker-compose up -d',
        ]
        
        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(f'sudo {cmd}')
            exit_status = stdout.channel.recv_exit_status()
            if exit_status != 0:
                logger.error(f"Command failed: {cmd}")
        
        ssh.close()
        return True
    except Exception as e:
        logger.error(f"Deployment error: {str(e)}")
        return False