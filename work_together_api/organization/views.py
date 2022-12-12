from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrganizationSerializer, JoinRequestCreateSerializer
from .models import Organization, JoinRequest
from django.http import Http404

class CreateOrganization(APIView):
    def post(self, request, format=None):
        serializer = OrganizationSerializer(
            data=request.data,
            context = {
                'request' : request
            }
        )
        serializer.is_valid(raise_exception=True)

        org_slug = serializer.validated_data.get('name').lower()

        if Organization.objects.filter(org_slug=org_slug).exists():
            return Response({'error' : 'This name already exists'})

        serializer.save()
        return Response(status=200)

class GetOrganizations(APIView):
    def get(self, request, format=None):
        user = request.user
        orgs = Organization.objects.filter(owner=user)
        serializer = OrganizationSerializer(orgs, many=True)
        return Response(serializer.data)

class DetailOrganization(APIView):
    def get_object(self, org_slug):
        try:
            return Organization.objects.get(org_slug=org_slug)
        except:
            raise Http404
    
    def get(self, request, org_slug, format=None):
        org = self.get_object(org_slug)
        serializer = OrganizationSerializer(org)
        is_owner = request.user.id == org.owner.id
        return Response(data={
            'org' : serializer.data,
            'is_owner' : is_owner
        })

class JoinRequestsView(APIView):
    def post(self, request, format=None):
        serializer = JoinRequestCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=200)

    def get(self, request, format=None):
        pass



@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        organizations = Organization.objects.filter(name__icontains=query)
        orgs = []

        # filters the organizations where the user is already in ore have requested it
        for org in organizations:
            if not JoinRequest.objects.filter(org=org, user=request.user).exists() and request.user != org.owner:
                orgs.append(org)


        serializer = OrganizationSerializer(orgs, many=True)
        return Response(serializer.data)

    return Response({'organizations': []})
