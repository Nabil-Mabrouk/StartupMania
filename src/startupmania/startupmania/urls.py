"""
URL configuration for startupmania project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import CustomLoginView, CustomSignupView, CustomLogoutView
from django.conf import settings
from django.conf.urls.static import static
from users.views import CustomPasswordChangeView, CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView
from users.views import CustomPasswordResetFromKeyView
from users.views import CustomPasswordResetFromKeyDoneView, Profile, edit_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('core/', include('core.urls')),
    path('profile/', Profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='custom_logout'),
    path('accounts/login/', CustomLoginView.as_view(), name='custom_login'),
    path('accounts/signup/', CustomSignupView.as_view(), name='custom_signup'),
    path('accounts/password/set/', CustomPasswordChangeView.as_view(), name='custom_password_set'),  # This seems to be for setting the password
    path('accounts/password/change/', CustomPasswordChangeView.as_view(), name='custom_password_change'),
    path('accounts/password/reset/', CustomPasswordResetView.as_view(), name='custom_password_reset'),
    path('accounts/password/reset/done/', CustomPasswordResetDoneView.as_view(), name='custom_password_reset_done'),  # Add done view after reset
    path('accounts/password/reset/confirm/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='custom_password_reset_confirm'),  # Allauth URL for confirming password reset
    path('accounts/password/reset/complete/', CustomPasswordResetCompleteView.as_view(), name='custom_password_reset_complete'),  # Password reset complete view
    path('accounts/password/reset/key/<uidb64>/<token>/', CustomPasswordResetFromKeyView.as_view(), name='custom_reset_password_from_key'),
    path('accounts/password/reset/key/done/', CustomPasswordResetFromKeyDoneView.as_view(), name='account_reset_password_from_key_done'),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('blog.urls')),
    path('onboarding/', include('onboarding.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
