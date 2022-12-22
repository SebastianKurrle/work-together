from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WorkspaceSerializer, FileUploadSerializer, ChatMessageCreateSerializer
from .models import Workspace, FileUpload
from organization.models import Organization
from organization.permissons import IsMemberOfOrganization

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
    def get(self, request, org_id, format=None):
        org = Organization.objects.get(id=org_id)
        workspaces = Workspace.objects.filter(organization=org)
        serializer = WorkspaceSerializer(workspaces, many=True)

        return Response(serializer.data)

class GetWorkspace(APIView):
    permission_classes = [IsMemberOfOrganization]
    def get(self, request, org_slug, ws_slug, format=None):
        org = Organization.objects.get(org_slug=org_slug)
        self.check_object_permissions(request, org)
        workspace = Workspace.objects.get(slug=ws_slug, organization=org)
        serializer = WorkspaceSerializer(workspace)

        return Response(serializer.data)

class UploadFile(APIView):
    def post(self, request, ws_id, format=None):
        workspace = Workspace.objects.get(id=ws_id)
        serializer = FileUploadSerializer(data=request.data, context={
            'ws_id' : ws_id
        })
        serializer.is_valid()
        serializer.save()

        return Response(status=200)

    def get(self, request, ws_id, format=None):
        workspace = Workspace.objects.get(id=ws_id)
        files_uploads = FileUpload.objects.filter(workspace=workspace)
        serializer = FileUploadSerializer(files_uploads, many=True)

        return Response(serializer.data)

class ChatMesssageView(APIView):
    def post(self, request, format=None):
        print(request.data)
        serializer = ChatMessageCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=201)
