from users.models import CustomUser
from django.db import models

class UserOnboarding(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    current_step = models.PositiveIntegerField(default=1)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Step {self.current_step}"

class TemporarySubmission(models.Model):
    session_key = models.CharField(max_length=40, unique=True)
    user_problem = models.TextField()
    current_step = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)