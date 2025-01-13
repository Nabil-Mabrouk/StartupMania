import json
import os
import sys
import subprocess
import shutil
import logging
from string import Template
import re

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def run_psql_command(command, admin_user, admin_password):
    """
    Run a psql command using subprocess.

    Args:
        command (str): The psql command to execute.
        admin_user (str): The PostgreSQL admin user.
        admin_password (str): The password for the admin user.

    Returns:
        str: The stdout output of the command if successful.
    """
    logger.info(f"Executing psql command: {command} ...")
    env = os.environ.copy()
    if admin_password:
        env["PGPASSWORD"] = admin_password

    try:
        result = subprocess.run(
            ["psql", "-U", admin_user, "-h", "127.0.0.1", "-p", "5432", "-c", command],
            capture_output=True,
            text=True,
            env=env,
            check=True
        )
        logger.info(f"Command executed successfully. Output:\n{result.stdout.strip()}")
        return result.stdout
    except subprocess.CalledProcessError as e:
        logger.error(f"Error executing command: {e.stderr.strip()}")
        return None

def create_database_and_user(project_name="startupmania", admin_user='postgres', admin_password='HindiBechouk18!'):
    """
    Create a PostgreSQL database, a user, set a password, and write to .env.

    Args:
        project_name (str): The base name for database and user.
        admin_user (str): PostgreSQL admin user.
        admin_password (str): PostgreSQL admin password.
    """
    db_name = f"{project_name}_db"
    user_name = f"{project_name}_user"
    password = f"{project_name}_pass"
    logger.info("Setting up PostgreSQL database and user...")

    try:
        # Step 1: Check if database exists
        db_exists_cmd = f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';"
        db_exists_output = run_psql_command(db_exists_cmd, admin_user, admin_password)

        if db_exists_output and "1 row" in db_exists_output:
            choice = input(f"Database '{db_name}' already exists. Drop and recreate? (yes/no): ").strip().lower()
            if choice == "yes":
                run_psql_command(f"DROP DATABASE {db_name};", admin_user, admin_password)
                logger.info(f"Database '{db_name}' dropped.")
            else:
                logger.info(f"Keeping existing database '{db_name}'.")
                return

        # Step 2: Create the database
        run_psql_command(f"CREATE DATABASE {db_name};", admin_user, admin_password)
        logger.info(f"Database '{db_name}' created successfully.")

        # Step 3: Check if user exists
        user_exists_cmd = f"SELECT 1 FROM pg_roles WHERE rolname = '{user_name}';"
        user_exists_output = run_psql_command(user_exists_cmd, admin_user, admin_password)

        if user_exists_output and "1 row" in user_exists_output:
            choice = input(f"User '{user_name}' already exists. Drop and recreate? (yes/no): ").strip().lower()
            if choice == "yes":
                run_psql_command(f"DROP USER {user_name};", admin_user, admin_password)
                logger.info(f"User '{user_name}' dropped.")
            else:
                logger.info(f"Keeping existing user '{user_name}'.")
                return

        # Step 4: Create the user and grant privileges
        # Step 4: Create the user and grant privileges
        run_psql_command(f"CREATE USER {user_name} WITH PASSWORD '{password}';", admin_user, admin_password)

        # Grant all privileges on the database
        run_psql_command(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {user_name};", admin_user, admin_password)

        # Set the user as the database owner
        run_psql_command(f"ALTER DATABASE {db_name} OWNER TO {user_name};", admin_user, admin_password)

        # Grant schema-level permissions to allow table creation
        run_psql_command(f"GRANT USAGE, CREATE ON SCHEMA public TO {user_name};", admin_user, admin_password)

        logger.info(f"User '{user_name}' created, privileges granted, and schema permissions set.")

        # Step 5: Write connection details to .env file
        # env_file = os.path.join(project_name, ".env")
        # add_to_env_file(
        #     env_file,
        #     DB_NAME=db_name,
        #     DB_USER=user_name,
        #     DB_PASSWORD=password,
        #     DB_HOST="127.0.0.1",
        #     DB_PORT="5432"
        # )
        # logger.info("Database connection details saved to .env file.")
        logger.info(f"DN_NAME :  {db_name}")
        logger.info(f"DN_USER :  {user_name}")
        logger.info(f"DN_PASSWORD :  {password}")


    except Exception as e:
        logger.error(f"An error occurred: {e}")



def text_psycopg2():
    import psycopg2
    import sys

    print(sys.getdefaultencoding())

    try:
        conn = psycopg2.connect(
            dbname="startupmania_db",
            user="startupmania_user",
            password="startupmania_pass",
            host="localhost",
            port=5432
        )
    except UnicodeDecodeError as e:
        print(f"Unicode error: {e}")
