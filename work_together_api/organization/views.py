from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrganizationSerializer
from .models import Organization

class CreateOrganization(APIView):
    def post(self, request, format=None):
        serializer = OrganizationSerializer(
            data=request.data,
            context = {
                'request' : request
            }
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(status=200)

class GetOrganizations(APIView):
    def get(self, request, format=None):
        user = request.user
        orgs = Organization.objects.filter(owner=user)
        serializer = OrganizationSerializer(orgs, many=True)
        return Response(serializer.data)
