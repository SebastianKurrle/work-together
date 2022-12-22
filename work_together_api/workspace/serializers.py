from rest_framework import serializers
from .models import Workspace, FileUpload, ChatMessage
from organization.models import Organization

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = (
            'id',
            'name',
            'description',
            'organization',
            'get_absolute_url'
        )

    def create(self, validated_data):
        name = validated_data.get('name').lower()
        desc = validated_data.get('description')
        slug = name
        org = validated_data.get('organization')

        workspace = Workspace.objects.create(name=name, description=desc, slug=slug, organization=org)
        return workspace

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = (
            'id',
            'file',
            'description',
            'get_file',
            'get_file_name'
        )

    def create(self, validated_data):
        file = validated_data.get('file')
        desc = validated_data.get('description')
        ws_id = self.context.get('ws_id')
        workspace = Workspace.objects.get(id=ws_id)

        file_upload = FileUpload.objects.create(file=file, description=desc, workspace=workspace)
        return file_upload

# For the creation from chat messages
class ChatMessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = (
            'message',
            'user',
            'workspace'
        )

    def create(self, validated_data):
        message = validated_data.get('message')
        user = validated_data.get('user')
        workspace = validated_data.get('workspace')

        print(user)

        chat_message = ChatMessage.objects.create(message=message, user=user, workspace=workspace)
        return chat_message
