from django.contrib import admin
from .models import Project, AppTemplate, BusinessConcept, MarketAnalysis, MVPConfiguration, ProjectConfiguration, FinalReview

class BusinessConceptInline(admin.StackedInline):
    model = BusinessConcept
    extra = 0
    fields = ('project_name', 'user_demand', 'reformulated_idea')
    can_delete = False

class MarketAnalysisInline(admin.StackedInline):
    model = MarketAnalysis
    extra = 0
    fields = ('market_size', 'competitors_analysis', 'mvp_features', 'innovation_rating', 'complexity_rating')
    can_delete = False

class MVPConfigurationInline(admin.StackedInline):
    model = MVPConfiguration
    extra = 0
    fields = ('selected_apps', 'custom_features', 'frontend_description')
    can_delete = False

class ProjectConfigurationInline(admin.StackedInline):
    model = ProjectConfiguration
    extra = 0
    fields = ('project_config', 'deployment_config')
    can_delete = False

class FinalReviewInline(admin.StackedInline):
    model = FinalReview
    extra = 0
    fields = ('approval_status', 'review_notes')
    can_delete = False

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [BusinessConceptInline, MarketAnalysisInline, MVPConfigurationInline, ProjectConfigurationInline, FinalReviewInline]
    list_display = ('id', 'user_display', 'current_step', 'completed')

    def user_display(self, obj):
        return obj.user.username if obj.user else "Anonymous"
    user_display.short_description = "User"

@admin.register(AppTemplate)
class AppTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'version', 'is_active')
    search_fields = ('name', 'category')
