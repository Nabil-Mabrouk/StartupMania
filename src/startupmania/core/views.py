from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class CoreView(TemplateView):
    template_name = 'core/core.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Welcome to the core view!"
        return context