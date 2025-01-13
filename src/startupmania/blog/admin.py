from django.contrib import admin
from .models import BlogPost, Image

class ImageInline(admin.TabularInline):
    model = Image
    fields = ('image', 'description', 'get_image_url')
    readonly_fields = ('get_image_url',)  # Display image URL
    extra = 1  # Allow adding new images directly

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return "No image uploaded"
    get_image_url.short_description = "Image URL"

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'slug')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ImageInline]  # Add inline images