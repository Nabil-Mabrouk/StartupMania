from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import os
from users.models import CustomUser

# Validators
def validate_app_directory(value):
    if not os.path.isdir(value):
        raise ValidationError(f"Invalid directory: {value}")

# Base Models
class TimestampedModel(models.Model):
    """Abstract base model with timestamps"""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AppTemplate(TimestampedModel):
    """Template model for Django app configurations"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=50)
    version = models.CharField(max_length=20, default="1.0.0")
    storage_path = models.CharField(
        max_length=255,
        help_text="Path to template files",
        validators=[validate_app_directory]
    )
    dependencies = models.JSONField(default=list, blank=True, null=True, help_text="List of required dependencies")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (v{self.version})"

class Project(TimestampedModel):
    """Main project model tracking user progress"""
    STEP_CHOICES = [
        (1, 'Business Concept'),
        (2, 'Market Analysis'),
        (3, 'MVP Configuration'),
        (4, 'Project Configuration'),
        (5, 'Final Review')
    ]

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='projects', null=True, blank=True
    )
    session_key = models.CharField(
        max_length=40, blank=True, null=True, db_index=True,
        help_text="Session key for anonymous users"
    )
    business_idea = models.TextField(help_text="The problem or idea of the business", null=True, blank=True)
    project_name = models.CharField(max_length=200, default="Unnamed Project")

    current_step = models.PositiveIntegerField(choices=STEP_CHOICES, default=1)
    completed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['session_key', '-created_at'])
        ]
        constraints = [
            models.CheckConstraint(
                check=models.Q(user__isnull=False) | models.Q(session_key__isnull=False),
                name='user_or_session_required'
            )
        ]

    def __str__(self):
        identifier = self.user.username if self.user else f"Session: {self.session_key}"
        return f"{identifier}'s Project ({self.created_at:%Y-%m-%d}) - Step {self.current_step}"

    # def save(self, *args, **kwargs):
    #     # if not self.user and not self.session_key:
    #     #     raise ValidationError("Project must have either a user or session key")
    #     super().save(*args, **kwargs)

class ProjectStepBase(TimestampedModel):
    """Abstract base model for project steps"""
    project = models.OneToOneField(
        Project, 
        on_delete=models.CASCADE, 
        related_name='%(class)s_step'  # Changed to avoid naming conflicts
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} for {self.project.project_name}"

class BusinessConcept(ProjectStepBase):
    """Step 1: Define business concept"""
    # Removed duplicate project_name field
    user_demand = models.TextField(default="")
    project_name=models.TextField(max_length=200, default="Unnamed Project")
    reformulated_idea = models.TextField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project'],
                name='unique_business_concept'
            )
        ]

class MarketAnalysis(ProjectStepBase):
    """Step 2: Analyze the market"""
    market_size = models.FloatField(help_text="Market Size in M€")
    competitors_analysis = models.TextField()
    mvp_features = models.TextField()
    innovation_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    complexity_rating = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project'],
                name='unique_market_analysis'
            )
        ]

class MVPConfiguration(ProjectStepBase):
    """Step 3: MVP setup with selected apps"""
    selected_apps = models.ManyToManyField(
        AppTemplate, 
        related_name='mvp_configurations',  # Fixed related name
        help_text="Selected applications for this project"
    )
    custom_features = models.TextField(help_text="List of custom features")
    frontend_description = models.TextField(blank=True, help_text="Frontend customization guidelines")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project'],
                name='unique_mvp_configuration'
            )
        ]

class ProjectConfiguration(ProjectStepBase):
    """Step 4: Configure project settings"""
    project_config = models.JSONField(null=True, blank=True, help_text="Project generation data")
    deployment_config = models.JSONField(null=True, blank=True, help_text="Deployment setup")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project'],
                name='unique_project_configuration'
            )
        ]

class FinalReview(ProjectStepBase):
    """Step 5: Final review before deployment"""
    approval_status = models.BooleanField(default=False)
    review_notes = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project'],
                name='unique_final_review'
            )
        ]