from django.db import models
from organization.models import Organization

class Workspace(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return f'/organization/{self.organization.org_slug}/{self.slug}'

    def __str__(self):
        return self.name

class FileUpload(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField()
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name
