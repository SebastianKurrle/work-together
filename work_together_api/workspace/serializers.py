from rest_framework import serializers
from .models import Workspace

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = (
            'id',
            'name',
            'description',
            'get_absolute_url'
        )
