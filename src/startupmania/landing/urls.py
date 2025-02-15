from django.urls import path
from .views import LandingFormView

urlpatterns = [
    path('', LandingFormView.as_view(), name='landing-page'),
]
