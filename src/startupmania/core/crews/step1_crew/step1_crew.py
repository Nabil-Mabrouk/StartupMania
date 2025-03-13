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

class MarketData(BaseModel):
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
        print(result.pydantic.reformulated_idea)
        return result.pydantic  # Pydantic v2 format

class CrewAIServiceRefine:
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
        business_idea_refiner = Agent(config=self.agents_config["business_idea_refiner"])
        
        business_idea_refinement_task = Task(
            config=self.tasks_config["business_idea_refinement_task"], 
            name="business idea refinement task", 
            agent=business_idea_refiner,
            output_pydantic=BusinessIdeaOutput,
            callback=self._task_callback
        )

        return Crew(
            agents=[business_idea_refiner],
            tasks=[business_idea_refinement_task],
            verbose=True
        )

    def _task_callback(self, output: TaskOutput):
        """Handles post-task completion actions."""
        print(f"Task completed! Task: {output.name}")

    def process_business_idea(self, structured_idea:str, user_input: str) -> BusinessIdeaOutput:
        """Executes CrewAI and returns structured output."""
        result = self.crew.kickoff(inputs={"structured_idea":structured_idea, "user_modifications": user_input})
        print(result.pydantic.reformulated_idea)
        return result.pydantic  # Pydantic v2 format

class CrewAIMarketAnalysis:
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
        market_sizer = Agent(config=self.agents_config["market_sizer"])
        competitor_analyst = Agent(config=self.agents_config["competitor_analyst"])
        mvp_architect = Agent(config=self.agents_config["mvp_architect"])
        ratings_specialist = Agent(config=self.agents_config["ratings_specialist"])
        validation_agent = Agent(config=self.agents_config["validation_agent"])

        market_size_calculation = Task(
            config=self.tasks_config["market_size_calculation"], 
            name="market size calculation", 
            agent=market_sizer,
            callback=self._task_callback
        )
        competitor_analysis_task = Task(
            config=self.tasks_config["competitor_analysis_task"], 
            name="competitor_analysis_task", 
            agent=competitor_analyst,
            callback=self._task_callback
        )

        mvp_definition_task = Task(
            config=self.tasks_config["mvp_definition_task"], 
            name="mvp definition task", 
            agent=mvp_architect,
            callback=self._task_callback
        )

        ratings_calculation_task = Task(
            config=self.tasks_config["ratings_calculation_task"], 
            name="ratings_calculation_task", 
            agent=ratings_specialist,
            callback=self._task_callback
        )
        
        validation_task = Task(
            config=self.tasks_config["validation_task"], 
            name="validation_task", 
            agent=validation_agent,
            callback=self._task_callback
        )

        return Crew(
            agents=[market_sizer, competitor_analyst, mvp_architect, ratings_specialist, validation_agent],
            tasks=[market_size_calculation, competitor_analysis_task, 
                   mvp_definition_task, ratings_calculation_task,
                   validation_task],
            verbose=True
        )

    def _task_callback(self, output: TaskOutput):
        """Handles post-task completion actions."""
        print(f"Task completed! Task: {output.name}")

    def process_business_idea(self, structured_idea:str, project_name: str) -> MarketData:
        """Executes CrewAI and returns structured output."""
        result = self.crew.kickoff(inputs={"structured_idea":structured_idea, "project_name": project_name})
        #print(result.pydantic.reformulated_idea)
        return result.pydantic  # Pydantic v2 format