# from django.urls import path
# # from .views import (
# #     ProblemResearchListView,
# #     ProblemResearchDetailView,
# #     ProblemResearchUpdateView,
# #     ProblemResearchDeleteView,
# #     dashboard
# # )
# from ._views import ProjectStepView, complete_view, create_project

# urlpatterns = [
#     #path("", ProblemResearchListView.as_view(), name="problem_research_list"),
#     #path("<int:pk>/", ProblemResearchDetailView.as_view(), name="problem_research_detail"),
#     #path("<int:pk>/edit/", ProblemResearchUpdateView.as_view(), name="problem_research_edit"),
#     #path("<int:pk>/delete/", ProblemResearchDeleteView.as_view(), name="problem_research_delete"),
#     path('project/create', create_project, name='project-create'),
#     path('project/step/<int:step>/', ProjectStepView.as_view(), name='project-step'),
#     path('project/complete/', complete_view, name='project-complete'),
# ]

from django.urls import path
from .views import ProjectStepView, complete_view

urlpatterns = [
    path('step/<int:step>/', ProjectStepView.as_view(), name='project-step'),
    path('complete/', complete_view, name='project-complete'),
]