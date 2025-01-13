from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Write content in Markdown")
    slug = models.SlugField(unique=True, blank=True)
    published_date = models.DateTimeField(default=now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Image(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/')
    description = models.CharField(max_length=200, blank=True, help_text="Optional description for the image")

    def get_image_url(self):
        if self.image:
            return self.image.url
        return ""