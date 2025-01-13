from django import forms
from .models import Profile, CustomUser

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'openai_api_key']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username', 'email']
    
    def __inti__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required=True
        self.fields['username'].required=False
        self.fields['email'].widget.attrs['readonly']=True