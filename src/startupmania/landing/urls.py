from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landing_page'),
    path('thank-you/', views.thank_you_page, name='thank_you_page'),
    path('welcome-back/', views.welcome_back_page, name='welcome_back_page'),
]