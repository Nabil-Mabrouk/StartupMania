from .models import UserOnboarding
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

class OnboardingMixin:
    step_number = None
    template_name = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_step'] = self.step_number
        context['total_steps'] = 4
        return context

    def dispatch(self, request, *args, **kwargs):
        onboarding, created = UserOnboarding.objects.get_or_create(user=request.user)
        
        if onboarding.completed:
            return redirect('onboarding-complete')
        
        if self.step_number != onboarding.current_step:
            return redirect('onboarding-step', step=onboarding.current_step)
            
        return super().dispatch(request, *args, **kwargs)

class OnboardingStepView(LoginRequiredMixin, OnboardingMixin, TemplateView):
    def get_template_names(self):
        return [f'onboarding/step_{self.step_number}.html']

    def post(self, request, *args, **kwargs):
        onboarding = UserOnboarding.objects.get(user=request.user)
        action = request.POST.get('action')

        if action == 'next' and onboarding.current_step < 4:
            onboarding.current_step += 1
        elif action == 'previous' and onboarding.current_step > 1:
            onboarding.current_step -= 1
        elif action == 'complete':
            onboarding.completed = True
            
        onboarding.save()
        
        if onboarding.completed:
            return redirect('onboarding-complete')
            
        return redirect('onboarding-step', step=onboarding.current_step)

class OnboardingCompleteView(LoginRequiredMixin, TemplateView):
    template_name = 'onboarding/complete.html'
