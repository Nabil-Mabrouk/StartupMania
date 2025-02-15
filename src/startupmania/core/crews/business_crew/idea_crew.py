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

files = {
    'agents': os.path.join(settings.BASE_DIR, 'core/crews/business_crew/config/agents.yaml'),
    'tasks': os.path.join(settings.BASE_DIR, 'core/crews/business_crew/config/tasks.yaml')
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, 'r') as file:
        configs[config_type] = yaml.safe_load(file)

# Assign loaded configurations to specific variables
agents_config = configs['agents']
tasks_config = configs['tasks']

class ProblemResearchOutput(BaseModel):
    detailed_report:str =Field(..., description="Comprehensive final report in well formatted markdown")
    project_name: str = Field(..., max_length=8, description="One-word project name (max 8 characters)")
    market_size: str = Field(..., description="Estimated market size (e.g., '10M users')")
    category: str = Field(..., description="Project category (e.g., 'Productivity', 'Healthcare')")

problem_structurer= Agent(config=agents_config["problem_structurer"])
market_analyst=Agent(config=agents_config["market_analyst"])
competitor_analyst=Agent(config=agents_config["competitor_analyst"])
feasibility_evaluator=Agent(config=agents_config["feasibility_evaluator"])
analyst_agent=Agent(config=agents_config["analyst_agent"])


problem_structuring_task=Task(config=tasks_config["problem_structuring_task"], name="Problem Structuring task", agent=problem_structurer, callback=callback_function)
market_analysis_task=Task(config=tasks_config["market_analysis_task"], name="Market analysis task", agent=market_analyst,  callback=callback_function)
competitor_analysis_task=Task(config=tasks_config["competitor_analysis_task"],
                              agent=competitor_analyst,
                              name="Competition analysis task",
                              context= [problem_structuring_task],
                              callback=callback_function
                              )
technical_feasibility_task= Task(config=tasks_config["technical_feasibility_task"],
                                 agent=feasibility_evaluator,
                                 name="Technical feasability task",
                                 context= [problem_structuring_task],
                                 callback=callback_function)
final_analysis_task=Task(config=tasks_config["final_analysis_task"],
                         agent=analyst_agent, 
                         output_pydantic=ProblemResearchOutput,
                         name="Final report",
                         context= [problem_structuring_task, market_analysis_task, competitor_analysis_task, technical_feasibility_task],
                         callback=callback_function)

crew = Crew(
            agents=[problem_structurer,market_analyst, competitor_analyst, feasibility_evaluator, analyst_agent],  # Automatically created by the @agent decorator
            tasks=[problem_structuring_task, market_analysis_task, competitor_analysis_task, technical_feasibility_task, final_analysis_task ],  # Automatically created by the @task decorator
            process=Process.sequential,  # Tasks executed one after another
            verbose=False,
        )
