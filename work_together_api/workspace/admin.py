from django.contrib import admin
from .models import Workspace, FileUpload, ChatMessage

admin.site.register(Workspace)
admin.site.register(FileUpload)
admin.site.register(ChatMessage)
