from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from pydantic import BaseModel, Field
from typing import List, Union, Dict
from django.conf import settings

from pydantic import BaseModel, Field

# Required: Your API key for authentication
OPEN_AI_KEY=settings.OPENAI_API_KEY

# Optional: Default model selection
OPENAI_MODEL_NAME='gpt-4o-mini'  # Default if not set

class ProblemResearchOutput(BaseModel):
    detailed_report:str =Field(..., description="Comprehensive final report")
    project_name: str = Field(..., max_length=8, description="One-word project name (max 8 characters)")
    market_size: str = Field(..., description="Estimated market size (e.g., '10M users')")
    category: str = Field(..., description="Project category (e.g., 'Productivity', 'Healthcare')")


@CrewBase
class Crew:
    """Crew to Analyze and Simplify MVP"""

    # YAML configurations for agents and tasks
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def __init__(self, *args, **kwargs):
        # Explicitly handle initialization arguments
        # Call the parent class's initializer if needed
        super().__init__(*args, **kwargs)

    # Agent definitions
    @agent
    def problem_structurer(self) -> Agent:
        return Agent(
            config=self.agents_config["problem_structurer"],
        )

    @agent
    def market_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["market_analyst"],
        )

    @agent
    def competitor_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["competitor_analyst"],
        )
    
    @agent
    def feasibility_evaluator(self) -> Agent:
        return Agent(
            config=self.agents_config["feasibility_evaluator"],
        )

    @agent
    def analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["analyst_agent"],
        )
    # Task definitions
    @task
    def problem_structuring_task(self) -> Task:
        return Task(
            config=self.tasks_config["problem_structuring_task"],
            #output_file="outputs/idea_crew/simplified_mvp.md",
            #create_directory=True,
        )

    @task
    def market_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_analysis_task"],
            #output_file="outputs/idea_crew/simplified_mvp.md",
            #create_directory=True,
        )
    
    @task
    def competitor_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["competitor_analysis_task"],
            #output_file="outputs//idea_crew/validated_business_idea.md",
            #create_directory=True,
        )
    
    @task
    def technical_feasibility_task(self) -> Task:
        return Task(
            config=self.tasks_config["technical_feasibility_task"],
            #output_file="outputs/idea_crew/simplified_mvp.md",
            #create_directory=True,
        )
    @task
    def final_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["final_analysis_task"],
            #output_file="outputs/idea_crew/simplified_mvp.md",
            #create_directory=True,
            output_pydantic=ProblemResearchOutput
        )
    # Crew definition
    @crew
    def crew(self) -> Crew:
        """Creates the MVP Simplification Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,  # Tasks executed one after another
            verbose=True,
        )