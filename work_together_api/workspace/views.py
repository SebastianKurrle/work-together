from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WorkspaceSerializer
from .models import Workspace

class CreateWorkspace(APIView):
    def post(self, request, format=None):
        serializer = WorkspaceSerializer(data=request.data)
        serializer.is_valid()
        workspace_name = serializer.validated_data.get('name')
        if Workspace.objects.filter(name=workspace_name.lower()).exists():
            return Response({'error' : 'A workspace with this name already exists'})

        serializer.save()
        return Response(status=200)
