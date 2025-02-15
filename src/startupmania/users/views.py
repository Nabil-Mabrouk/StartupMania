from django.shortcuts import render, redirect
from allauth.account.views import LoginView, SignupView, LogoutView, PasswordChangeView, PasswordResetView 
from allauth.account.views import PasswordResetDoneView, PasswordResetFromKeyView, PasswordResetFromKeyDoneView
from .forms import ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        return context

class CustomSignupView(SignupView):
    template_name = 'account/signup.html'

    def form_valid(self, form):
        # Add a print or log here to check if form validation is successful
        print("Form is valid")
        return super().form_valid(form)

    def form_invalid(self, form):
        # Check why the form might be invalid
        print(form.errors)
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    template_name = 'account/logout.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Log logout activity
        # Log logout activity only once
        return context

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'account/password_change.html'  # Use your custom template

    def form_valid(self, form):
        # Log password change activity
        messages.success(self.request, 'Your password has been updated!')
        return super().form_valid(form)

class CustomPasswordResetView(PasswordResetView):
    template_name = 'account/password_reset.html'  # Custom template path
    
    def form_valid(self, form):
        # Log password reset initiation
        messages.success(self.request, 'Password reset link sent! Check your email.')
        return super().form_valid(form)

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'account/password_reset_done.html'  # Custom template path

class CustomPasswordResetConfirmView(PasswordResetDoneView):
    template_name = 'account/password_reset_confirm.html'  # Custom template path
    
    def form_valid(self, form):
        # Log password reset confirmation
        messages.success(self.request, 'Your password has been reset successfully!')
        return super().form_valid(form)

class CustomPasswordResetCompleteView(PasswordResetDoneView):
    template_name = 'account/password_reset_complete.html'  # Custom template path

class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    template_name = "account/password_reset_from_key.html"  # Use your custom template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add your custom context data here
        return context
    
class CustomPasswordResetFromKeyDoneView(PasswordResetFromKeyDoneView):
    template_name = 'account/password_reset_from_key_done.html'  # Custom template
    # Optionally, you can define a success URL
    #success_url = reverse_lazy('landing-view')  # Redirect to login page or anywhere you prefer
    def get_template_names(self):
        print(f"Using template: {self.template_name}")
        return super().get_template_names()
    
@login_required
def Profile(request):
    if request.method=='POST':
        
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been Updated.')
            return redirect('landing-page')
    else:
        print("post else")
        u_form= UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
            'u_form':u_form,
            'p_form':p_form
        }
    return render(request, 'users/profile.html', context)

@login_required
def edit_profile(request):
    """To edit a users profile when he logs in and chooses to edit."""
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)

        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been Updated.')
            return redirect('profile')
        else:
            messages.error(request, f'Error occured during updating your account')

    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'p_form': p_form,
    }
    return render(request, 'users/edit_profile.html', context)