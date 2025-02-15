from django import forms
from users.models import CustomUser
from .models import LandingPageIdea
class EmailForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields = ['email']


class LandingPageIdeaForm(forms.ModelForm):
    """Form for submitting a business idea on the landing page."""
    class Meta:
        model = LandingPageIdea
        fields = ['idea_text']
        widgets = {
            'idea_text': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Describe Your Idea or Problem...'
            })
        }
        labels = {
            'idea_text': "Describe Your Idea or Problem"
        }