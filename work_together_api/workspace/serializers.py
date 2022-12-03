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

    
    def is_valid(self, *, raise_exception=False):
        super().is_valid(raise_exception=raise_exception)
        return Workspace.objects.filter(name=self.initial_data.get('name')).exists()

    def create(self, validated_data):
        name = validated_data.get('name').lower()
        desc = validated_data.get('description')
        slug = name
        org = validated_data.get('organization')

        workspace = Workspace.objects.create(name=name, description=desc, slug=slug, organization=org)
        return workspace
        
