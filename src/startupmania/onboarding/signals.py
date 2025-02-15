# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from users.models import CustomUser
# from .models import UserOnboarding

# @receiver(post_save, sender=CustomUser)
# def create_user_onboarding(sender, instance, created, **kwargs):
#     if created:
#         UserOnboarding.objects.create(user=instance)