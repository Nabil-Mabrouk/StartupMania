


from pydantic import BaseModel, Field
from typing import List, Dict

# Required: Your API key for authentication
OPEN_AI_KEY=settings.OPENAI_API_KEY

# Optional: Default model selection
OPENAI_MODEL_NAME='gpt-4o-mini'  # Default if not set

class File(BaseModel):
    name: str = Field(..., description="Name of the file (e.g., 'models.py')")
    instructions: str = Field(..., description="Instructions for the file (e.g., 'Define database models here.')")

class App(BaseModel):
    name: str = Field(..., description="Name of the Django app (e.g., 'app1')")
    files: List[File] = Field(..., description="List of files within the app, with instructions")

class Project(BaseModel):
    name: str = Field(..., max_length=50, description="Name of the project (e.g., 'MyDjangoProject', max 50 characters)")
    description: str = Field(..., description="Short description of the project")
    requirements: List[str] = Field(..., description="List of required Python packages")
    env: Dict[str, str] = Field(..., description="Environment variables for the project")
    apps: List[App] = Field(..., description="List of apps in the project, each with its own files")
