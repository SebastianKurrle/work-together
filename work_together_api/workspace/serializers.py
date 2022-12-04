from rest_framework import serializers
from .models import Workspace
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
        
