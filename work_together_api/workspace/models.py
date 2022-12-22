from django.db import models
from organization.models import Organization
from django.contrib.auth.models import User
import os

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

    def get_file(self):
        return 'http://127.0.0.1:8000/media/' + str(self.file)

    def get_file_name(self):
        return os.path.basename(self.file.name)

class ChatMessage(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} sends message in {self.workspace}'
