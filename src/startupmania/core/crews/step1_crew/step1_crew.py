import os
import yaml
from pathlib import Path
from pydantic import BaseModel, Field
from crewai import Agent, Crew, Task, Process
from crewai.tasks.task_output import TaskOutput
from django.conf import settings
# Required: Your API key for authentication
OPEN_AI_KEY=settings.OPENAI_API_KEY

# Optional: Default model selection
OPENAI_MODEL_NAME='gpt-4o-mini'  # Default if not set


class BusinessIdeaOutput(BaseModel):
    """Pydantic model for the AI-generated business idea."""
    project_name: str = Field(..., max_length=8, description="One-word project name (max 8 characters)")
    reformulated_idea: str = Field(..., description="A refined and structured version of the business idea")


class CrewAIService:
    """Handles CrewAI execution and task management."""
    
    def __init__(self):
        self._set_openai_key()
        self.agents_config, self.tasks_config = self._load_yaml_configs()
        self.crew = self._initialize_crew()

    def _set_openai_key(self):
        """Ensures the OpenAI API key is set for CrewAI."""
        os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

    def _load_yaml_configs(self):
        """Loads agent and task configurations from YAML files."""
        base_dir = Path(settings.BASE_DIR)
        files = {
            'agents': base_dir / 'core/crews/step1_crew/config/agents.yaml',
            'tasks': base_dir / 'core/crews/step1_crew/config/tasks.yaml'
        }
        
        configs = {}
        for config_type, file_path in files.items():
            with open(file_path, 'r') as file:
                configs[config_type] = yaml.safe_load(file)

        return configs['agents'], configs['tasks']

    def _initialize_crew(self):
        """Initializes CrewAI agents and tasks."""
        business_idea_architect = Agent(config=self.agents_config["business_idea_architect"])
        
        business_idea_structuring_task = Task(
            config=self.tasks_config["business_idea_structuring_task"], 
            name="Business idea structuring task", 
            agent=business_idea_architect,
            output_pydantic=BusinessIdeaOutput,
            callback=self._task_callback
        )

        return Crew(
            agents=[business_idea_architect],
            tasks=[business_idea_structuring_task],
            verbose=True
        )

    def _task_callback(self, output: TaskOutput):
        """Handles post-task completion actions."""
        print(f"Task completed! Task: {output.name}")

    def process_business_idea(self, user_input: str) -> BusinessIdeaOutput:
        """Executes CrewAI and returns structured output."""
        result = self.crew.kickoff(inputs={"user_problem": user_input})
        return result  # Pydantic v2 format
