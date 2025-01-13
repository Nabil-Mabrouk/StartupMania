from django import forms
from users.models import CustomUser

class EmailForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields = ['email']