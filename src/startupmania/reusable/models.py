from django.db import models

class ReusableApp(models.Model):
    name = models.CharField(max_length=100, unique=True)
    version = models.CharField(max_length=20)
    description = models.TextField()
    structure_description = models.TextField()
    path = models.CharField(
        max_length=255,
        help_text="Relative path within reusable_apps directory (e.g., 'blog_app/v1.2')"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    dependencies = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='dependent_apps',
        help_text="Other apps in the library this app depends on"
    )

    def __str__(self):
        return f"{self.name} v{self.version}"

class RequiredLibrary(models.Model):
    app = models.ForeignKey(
        ReusableApp,
        on_delete=models.CASCADE,
        related_name='required_libraries'
    )
    name = models.CharField(max_length=100)
    version = models.CharField(
        max_length=50,
        blank=True,
        help_text="Optional version constraint (e.g., '>=2.1.0')"
    )

    class Meta:
        verbose_name_plural = "Required libraries"

    def __str__(self):
        return f"{self.name} {self.version}" if self.version else self.name

class AppSetting(models.Model):
    SETTING_TYPES = (
        ('INSTALLED_APP', 'Installed Apps'),
        ('MIDDLEWARE', 'Middleware'),
        ('CONTEXT_PROCESSOR', 'Context Processors'),
        ('OTHER', 'Other Setting'),
    )

    app = models.ForeignKey(
        ReusableApp,
        on_delete=models.CASCADE,
        related_name='required_settings'
    )
    setting_type = models.CharField(
        max_length=20,
        choices=SETTING_TYPES,
        default='OTHER'
    )
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.key} configuration for {self.app.name}"

class AppDocumentation(models.Model):
    app = models.OneToOneField(
        ReusableApp,
        on_delete=models.CASCADE,
        related_name='documentation'
    )
    quick_start = models.TextField(help_text="Quick start guide")
    detailed_docs = models.TextField(blank=True)
    example_code = models.TextField(blank=True)

    def __str__(self):
        return f"Documentation for {self.app.name}"

class AppTag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    apps = models.ManyToManyField(
        ReusableApp,
        related_name='tags',
        blank=True
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name