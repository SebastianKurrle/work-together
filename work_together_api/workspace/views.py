from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import WorkspaceSerializer

class CreateWorkspace(APIView):
    def post(self, request, format=None):
        serializer = WorkspaceSerializer(data=request.data)
        print(serializer.is_valid(raise_exception=True))
        serializer.save()

        return Response(status=200)