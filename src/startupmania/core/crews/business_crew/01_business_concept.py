from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from typing import List, Union, Dict
from crewai.tasks.task_output import TaskOutput
from django.conf import settings
import yaml
from pydantic import BaseModel, Field
import os
# Required: Your API key for authentication
OPEN_AI_KEY=settings.OPENAI_API_KEY

# Optional: Default model selection
OPENAI_MODEL_NAME='gpt-4o-mini'  # Default if not set

from django.conf import settings

def callback_function(output: TaskOutput):
    # Do something after the task is completed
    # Example: Send an email to the manager
    print(f"""
        Task completed!
        Task: {output.name}
    """)

class BusinessConcept(BaseModel):
    project_name: str = Field(..., max_length=8, description="One-word project name (max 8 characters)")
    reformulated_idea: str = Field(..., description="Estimated market size (e.g., '10M users')")

files = {
    'agents': os.path.join(settings.BASE_DIR, 'core/crews/01_business_concept/config/agents.yaml'),
    'tasks': os.path.join(settings.BASE_DIR, 'core/crews/01_business_concept/config/tasks.yaml')
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, 'r') as file:
        configs[config_type] = yaml.safe_load(file)

# Assign loaded configurations to specific variables
agents_config = configs['agents']
tasks_config = configs['tasks']

# 
problem_structurer= Agent(config=agents_config["problem_structurer"])
problem_structuring_task=Task(config=tasks_config["problem_structuring_task"], 
                              name="Problem Structuring task", 
                              agent=problem_structurer,
                              output_pydantic=BusinessConcept, 
                              callback=callback_function)

crew = Crew(
            agents=[problem_structurer],  # Automatically created by the @agent decorator
            tasks=[problem_structuring_task],  # Automatically created by the @task decorator
            verbose=False,
        )