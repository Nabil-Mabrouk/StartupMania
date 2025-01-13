from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import EmailForm
from django.urls import reverse_lazy
from users.models import CustomUser
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
import logging
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from django import forms
from django.urls import reverse_lazy, reverse
from .models import EmailCapture


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def index(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Check if the email is already in the database
            if EmailCapture.objects.filter(email=email).exists():
                # Email already exists, redirect to welcome back page
                return redirect('welcome_back_page')
            else:
                # Email is new, save it to the database and redirect to thank you page
                EmailCapture.objects.create(email=email)
                return redirect('thank_you_page')
    else:
        form = EmailForm()

    return render(request, 'landing/index.html', {'form': form})

def thank_you_page(request):
    return render(request, 'landing/thank_you_page.html')

def welcome_back_page(request):
    return render(request, 'landing/welcome_back_page.html')


