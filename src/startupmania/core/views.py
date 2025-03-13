from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import BusinessConceptForm, MarketAnalysisForm, MVPConfigurationForm, ProjectConfigurationForm, FinalReviewForm
from .project_generator import generate_project
from .deployer import deploy_project
from .models import Project, BusinessConcept, MarketAnalysis, MVPConfiguration, ProjectConfiguration,FinalReview
from core.crews.step1_crew.step1_crew import CrewAIService, CrewAIServiceRefine
import logging

logger = logging.getLogger(__name__)

class ProjectStepView(FormView):
    step_templates = {
        1: 'core/step1.html',
        2: 'core/step2.html',
        3: 'core/step3.html',
        4: 'core/step4.html',
        5: 'core/step5.html'
    }
    step_forms = {
        1: BusinessConceptForm,
        2: MarketAnalysisForm,
        3: MVPConfigurationForm,
        4: ProjectConfigurationForm,
        5: FinalReviewForm
    }
    step_titles = {
        1: "Business Concept",
        2: "Market Analysis",
        3: "MVP Configuration",
        4: "Project Configuration",
        5: "Final Review"
    }
    step_descriptions = {
        1: "Refine your initial idea",
        2: "Analyze your market potential",
        3: "Select your MVP features and specifications",
        4: "Configure and prepare for deployment",
        5: "Review everything before submission"
    }
    total_steps = 5

    def get_template_names(self):
        return [self.step_templates.get(self.step)]

    def dispatch(self, request, *args, **kwargs):
        self.step = kwargs.get('step', 1)
        self.project = self.get_project()

        if not self.project:
            messages.error(request, "Please start a new project first")
            return redirect('landing-page')

        if not self.validate_step_progression():
            return redirect('project-step', step=self.get_first_incomplete_step())

        return super().dispatch(request, *args, **kwargs)

    def get_form_class(self):
        return self.step_forms[self.step]

    def get_project(self):
        project_id = self.request.session.get('project_id')
        if not project_id:
            return None
        try:
            return Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return None

    def form_valid(self, form):
        try:
            project = self.get_project()
            if not project:
                messages.error(self.request, "No project found. Please start a new project.")
                return redirect('landing-page')

            # if action == 'previous':
            #     # Navigate back without validating the form
            #     new_step = max(1, self.step - 1)
            #     project.current_step = new_step
            #     project.save()
            #     return redirect('project-step', step=new_step)

            # Save step data
            step_data = form.save(commit=False)
            step_data.project = project
            step_data.save()
            
            action = self.request.POST.get('action')
            new_step = self.step  # Default to current step

            if action == 'process':
                self.reprocess_step()
                #messages.success(self.request, f"Step {self.step}: Processed successfully!")
                return redirect('project-step', step=self.step)
            elif action == 'previous':
                new_step = max(1, self.step - 1)
            elif action == 'next':
                self.process_current_step()
                new_step = min(self.total_steps, self.step + 1)
            elif action == 'submit' and self.step == self.total_steps:
                return self.complete_submission()

            # Update project state before redirect
            project.current_step = new_step
            project.completed = (new_step == self.total_steps)
            project.save()

            return redirect('project-step', step=new_step)

        except Exception as e:
            logger.error(f"Error in step {self.step}: {str(e)}", exc_info=True)
            messages.error(self.request, f"An error occurred in step {self.step}: {str(e)}. Please try again.")
            return self.form_invalid(form)

    def validate_step_progression(self):
        """Allow access to any completed step when moving backward"""
        if self.step == 1:
            return True
        
        # Check if all previous steps up to requested step are complete
        step_map = {
            1: 'businessconcept_step',
            2: 'marketanalysis_step',
            3: 'mvpconfiguration_step', 
            4: 'projectconfiguration_step',
            5: 'finalreview_step'
        }
    
        for s in range(1, self.step):
            if not getattr(self.project, step_map.get(s, ''), None):
                messages.warning(self.request, f"Please complete step {s} before accessing step {self.step}.")
                return False
        return True

    def get_form_kwargs(self):
        """Pass existing instance to form if it exists"""
        kwargs = super().get_form_kwargs()
    
        # Map steps to their related names
        step_map = {
            1: 'businessconcept_step',
            2: 'marketanalysis_step',
            3: 'mvpconfiguration_step',
            4: 'projectconfiguration_step',
            5: 'finalreview_step'
        }
    
        step_data = getattr(self.project, step_map.get(self.step, ''), None)
        if step_data:
            kwargs['instance'] = step_data
        
        # Add initial data from previous step processing
        step_initial = self.process_previous_step()
        if step_initial:
            kwargs['initial'] = step_initial
        
        # Set default values for Step 2, Step 3, and Step 4
        if self.step == 2:
            # Default values for MarketAnalysisForm
            kwargs.setdefault('initial', {}).update({
                'market_size': 1.0,  # Default market size
                'competitors_analysis': 'No significant competitors identified.',
                'mvp_features': 'Basic feature set',
                'innovation_rating': 50,  # Default innovation rating
                'complexity_rating': 50,  # Default complexity rating
            })

        # Set default values for Step 3 and Step 4
        if self.step == 3:
            # Default values for MVPConfigurationForm
            kwargs.setdefault('initial', {}).update({
                'selected_apps': [1],  # Example default selected app (ID 1)
                'custom_features': 'Feature 1, Feature 2',
                'frontend_description': 'Default frontend description'
            })
        elif self.step == 4:
            # Default values for ProjectConfigurationForm
            kwargs.setdefault('initial', {}).update({
                'project_config': '{}',  # Default empty JSON
                'deployment_config': '{}',  # Default empty JSON
            })



        return kwargs

    def get_step_data(self):
        """
        Fetch the related step data based on the current step.
        """
        step_models = {
            1: BusinessConcept,
            2: MarketAnalysis,
            3: MVPConfiguration,
            4: ProjectConfiguration,
            5: FinalReview,
        }

        step_model = step_models.get(self.step)
        if not step_model:
            return None

        try:
            return step_model.objects.get(project=self.project)
        except step_model.DoesNotExist:
            return None

    def process_previous_step(self):
        if self.step > 1:
            previous_step_data = getattr(self.project, f'step{self.step - 1}_data', None)
            if previous_step_data:
                return previous_step_data.generate_defaults()
        return {}

    def process_current_step(self):
        step_data = self.get_step_data()
        if step_data:
            # Process the step data
            if self.step == 1: 
                messages.warning(self.request, f"Processing data of step {self.step}.")
                print("processing step 1")
                print(step_data)
            elif self.step == 2:
                messages.warning(self.request, f"Processing data of step {self.step}.")
                print("processing step 2")
            elif self.step == 3:
                messages.warning(self.request, f"Processing data of step {self.step}.")
                print("processing step 3")
            elif self.step == 4:
                messages.warning(self.request, f"Processing data of step {self.step}.")
                print("processing step 4")
            elif self.step == 5:
                messages.warning(self.request, f"Processing data of step {self.step}.")
                print("processing step 5")
            else:
                # Handle the case where step data does not exist
                messages.warning(self.request, f"No data found for step {self.step}.")

        # if step_data:
        #     step_data.process()

    def reprocess_step(self):
        step_data = self.get_step_data()
        if step_data:
            # Process the step data
            if self.step == 1: 
                messages.warning(self.request, f"Re-Processing data of step {self.step}.")
                print("reprocessing step 1")
                self.reprocess_business_concept(step_data)
            elif self.step == 2:
                messages.warning(self.request, f"Re-Processing data of step {self.step}.")
                print("reprocessing step 2")
            elif self.step == 3:
                messages.warning(self.request, f"Re-Processing data of step {self.step}.")
                print("reprocessing step 3")
            elif self.step == 4:
                messages.warning(self.request, f"Re-Processing data of step {self.step}.")
                print("reprocessing step 4")
            elif self.step == 5:
                messages.warning(self.request, f"Re-Processing data of step {self.step}.")
                print("reprocessing step 5")
            else:
                # Handle the case where step data does not exist
                messages.warning(self.request, f"No data found for step {self.step}.")
        
    def complete_submission(self):
        try:
            project = self.get_project()
            if not project:
                messages.error(self.request, "No project found. Please start a new project.")
                return redirect('landing-page')

            # Save the project as completed
            project.completed = True
            project.save()

            # Trigger the deployment process
            deploy_project(project)

            messages.success(self.request, "Project successfully submitted and ready for deployment!")
            return redirect('project-complete')
        except Exception as e:
            logger.error(f"Error during project submission: {str(e)}", exc_info=True)
            messages.error(self.request, "An error occurred during project submission. Please try again.")
            return redirect('project-step', step=self.step)

    def get_first_incomplete_step(self):
        for step in range(1, 6):
            if not getattr(self.project, f'step{step}_data', None):
                return step
        return 1

    def get_next_step(self, action):
        if action == 'next':
            return min(self.step + 1, self.total_steps)
        elif action == 'previous':
            return max(self.step - 1, 1)
        return self.step

    def is_step_complete(self):
        step_data = getattr(self.project, f'step{self.step}_data', None)
        return step_data is not None
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    
        step_map = {
            1: 'businessconcept_step',
            2: 'marketanalysis_step',
            3: 'mvpconfiguration_step',
            4: 'projectconfiguration_step',
            5: 'finalreview_step'
        }
    
        current_step_data = getattr(self.project, step_map.get(self.step, ''), None)
    
        context.update({
            'step': self.step,
            'total_steps': self.total_steps,
            'step_title': self.step_titles.get(self.step, "Step"),
            'step_description': self.step_descriptions.get(self.step, ""),
            'project': self.project,
            'is_step_complete': current_step_data is not None,
            'step_data': current_step_data
        })
        return context
    def reprocess_business_concept(self, concept):
        """Example: Generate initial technical requirements based on business concept"""
        reformulated_idea = f"""
        Project Idea: {concept.reformulated_idea}
        """
        crew_ai_service = CrewAIServiceRefine()
        result=crew_ai_service.process_business_idea(concept.reformulated_idea, concept.user_demand)
        structured_idea = result.reformulated_idea
        project_name=result.project_name

        # Update the project
        self.project.project_name = project_name
        self.project.business_idea = structured_idea
        self.project.save()

        # Update or create the BusinessConcept
        business_concept, created = BusinessConcept.objects.get_or_create(
            project=self.project,
            defaults={
                'reformulated_idea': structured_idea,
                'project_name': project_name,
            }
        )
        if not created:
            business_concept.reformulated_idea = structured_idea
            business_concept.project_name = project_name
            business_concept.save()



def complete_view(request):
    return render(request, 'core/complete.html') 

