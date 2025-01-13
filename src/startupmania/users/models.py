from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Profile(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='_profile_pics')
    openai_api_key = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, **kwargs):
        super().save(**kwargs)
        img=Image.open(self.image.path)
        if img.height > 700 or img.width > 500:
            output_size = (700,500)
            img.thumbnail(output_size)
            img.save(self.image.path)

