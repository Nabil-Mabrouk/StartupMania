from django.urls import path
from . import views

urlpatterns = [
    path('step/<int:step>/', views.OnboardingStepView.as_view(step_number=1), 
         name='onboarding-step'),
    path('complete/', views.OnboardingCompleteView.as_view(), 
         name='onboarding-complete'),
]