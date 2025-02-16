from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib import messages
import logging
from django.db import transaction
from .forms import LandingPageIdeaForm
from .models import LandingPageIdea
from core.models import Project, BusinessConcept
from core.crews.step1_crew.step1_crew import CrewAIService

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LandingFormView(FormView):
    template_name = 'landing/index.html'
    form_class = LandingPageIdeaForm
    success_url = reverse_lazy('project-step', kwargs={'step': 1})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.crew_ai_service = CrewAIService()  # Initialize CrewAI service

    def form_valid(self, form):
        """Handles form submission and project creation."""
        try:
            with transaction.atomic():
                # Ensure session has a key for anonymous users
                if not self.request.session.session_key:
                    self.request.session.save()

                idea = form.save()
                project = self.process_idea(idea)

                # Link project to session
                self.request.session['project_id'] = project.id

                messages.success(self.request, "Your business idea has been processed successfully!")
                return super().form_valid(form)
        except Exception as e:
            logger.error("Error processing idea: %s", str(e), exc_info=True)
            messages.error(self.request, "An error occurred while processing your request. Please try again.")
            return self.form_invalid(form)

    def process_idea(self, idea):
        """Creates Project and BusinessConcept from the idea."""
        project = Project.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            session_key=self.request.session.session_key,
            business_idea=idea.idea_text
        )

        # TODO: Replace placeholders with actual generated content

        # Parse the result into a Pydantic model
        structured_idea = self.crew_ai_service.process_business_idea(idea.idea_text)['reformulated_idea ']

        BusinessConcept.objects.create(
            project=project,
            user_demand=idea.idea_text,
            reformulated_idea=structured_idea
        )

        idea.processed = True
        idea.save()
        return project

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('instance', None)  # Safely remove instance if present
        return kwargs