from django.db import models

# Create your models here.
class EmailCapture(models.Model):
    email = models.EmailField(unique=True)
    signed_up = models.BooleanField(default=False)  # Tracks if the user registered

    def __str__(self):
        return self.email


class LandingPageIdea(models.Model):
    """Model for storing initial business ideas submitted on the landing page."""
    #project_name=models.TextField(max_length=200, default="Unnamed Project")
    idea_text = models.TextField(help_text="Enter your business idea")
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Idea submitted on {self.created_at.strftime('%Y-%m-%d')}"

    def mark_as_processed(self):
        """Marks the idea as processed."""
        self.processed = True
        self.save()