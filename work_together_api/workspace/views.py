from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WorkspaceSerializer
from .models import Workspace
from organization.models import Organization

class CreateWorkspace(APIView):
    def post(self, request, format=None):
        serializer = WorkspaceSerializer(data=request.data)
        serializer.is_valid()
        workspace_name = serializer.validated_data.get('name')
        org = serializer.validated_data.get('organization')
        if Workspace.objects.filter(name=workspace_name.lower(), organization=org).exists():
            return Response({'error' : 'A workspace with this name already exists'})

        serializer.save()
        return Response(status=200)

class GetWorkspaces(APIView):
    def get(self, request, org_id, form=None):
        org = Organization.objects.get(id=org_id)
        workspaces = Workspace.objects.filter(organization=org)
        serializer = WorkspaceSerializer(workspaces, many=True)

        return Response(serializer.data)
