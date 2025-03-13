from django import forms
from .models import BusinessConcept, MarketAnalysis, MVPConfiguration, ProjectConfiguration, FinalReview
from django.core.validators import MinValueValidator, MaxValueValidator
import json
from django.core.exceptions import ValidationError

def validate_json(value):
    try:
        json.loads(value)
    except json.JSONDecodeError:
        raise ValidationError("Invalid JSON format")


class BusinessConceptForm(forms.ModelForm):
    """Form for Step 1: Business Concept"""
    class Meta:
        model = BusinessConcept
        # Removed project_name since it's now in Project model
        fields = ['project_name', 'reformulated_idea', 'user_demand']
        
        widgets = {
            'project_name': forms.Textarea(attrs={
                'rows': 1,
                'placeholder': 'Enter your project name...',
                'readonly': True   # Additional protection
            }),
            'reformulated_idea': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Enter the refined version of your business idea...',
                'readonly': True   # Additional protection
            }),
                        'user_demand': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Enter your instructions to refine the business idea or to change the project name...'
            })
        }

class MarketAnalysisForm(forms.ModelForm):
    """Form for Step 2: Market Analysis"""
    class Meta:
        model = MarketAnalysis
        fields = ['market_size', 'competitors_analysis', 'mvp_features', 
                 'innovation_rating', 'complexity_rating']
        
        widgets = {
            'market_size': forms.NumberInput(attrs={'step': '0.1'}),
            'competitors_analysis': forms.Textarea(attrs={'rows': 4}),
            'mvp_features': forms.Textarea(attrs={'rows': 4}),
            'innovation_rating': forms.NumberInput(attrs={'min': 0, 'max': 100}),
            'complexity_rating': forms.NumberInput(attrs={'min': 0, 'max': 100})
        }
        
    def clean_market_size(self):
            market_size = self.cleaned_data.get('market_size')
            if market_size < 0:
                raise forms.ValidationError("Market size must be a positive number.")
            return market_size

class MVPConfigurationForm(forms.ModelForm):
    """Form for Step 3: MVP Configuration"""
    class Meta:
        model = MVPConfiguration
        fields = ['selected_apps', 'custom_features', 'frontend_description']
        
        widgets = {
            'selected_apps': forms.CheckboxSelectMultiple(),
            'custom_features': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'List custom features separated by commas...'
            }),
            'frontend_description': forms.Textarea(attrs={'rows': 3})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default value for selected_apps if it is empty
        if not self.instance.pk and not self.data:
            self.fields['selected_apps'].initial = [1]  # Example default selected app (ID 1)

class ProjectConfigurationForm(forms.ModelForm):
    """Form for Step 4: Project Configuration"""
    class Meta:
        model = ProjectConfiguration
        fields = ['project_config', 'deployment_config']
        
        widgets = {
            'project_config': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Enter JSON configuration for project setup...'
            }),
            'deployment_config': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Enter JSON configuration for deployment...'
            })
        }
    def clean_project_config(self):
            data = self.cleaned_data['project_config']
            validate_json(data)
            return data

    def clean_deployment_config(self):
            data = self.cleaned_data['deployment_config']
            validate_json(data)
            return data

class FinalReviewForm(forms.ModelForm):
    """Form for Step 5: Final Review"""
    approval_status = forms.BooleanField(
        required=True,
        label="I approve this configuration for deployment",
        help_text="You must check this box to proceed"
    )

    class Meta:
        model = FinalReview
        fields = ['approval_status', 'review_notes']
        
        widgets = {
            'review_notes': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Optional final notes or comments...'
            })
        }