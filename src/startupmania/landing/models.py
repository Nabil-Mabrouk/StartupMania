from django.db import models

# Create your models here.
class EmailCapture(models.Model):
    email = models.EmailField(unique=True)
    signed_up = models.BooleanField(default=False)  # Tracks if the user registered

    def __str__(self):
        return self.email