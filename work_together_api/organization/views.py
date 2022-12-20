from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrganizationSerializer, JoinRequestSerializer, OrganizationMemberSerializer
from users.serializers import UserSerializer
from .models import Organization, JoinRequest, OrganizationMember
from django.http import Http404
from .permissons import IsMemberOfOrganization

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

class OrganizationsFromUser(APIView):
    def get(self, request, format=None):
        user = request.user
        # gets all org member objects with the current user
        user_is_member_of = OrganizationMember.objects.filter(user=user)
        serializer = OrganizationMemberSerializer(user_is_member_of, many=True)

        return Response(serializer.data)

class DetailOrganization(APIView):
    permission_classes = [IsMemberOfOrganization]

    def get_object(self, org_slug):
        try:
            #print('test')
            return Organization.objects.get(org_slug=org_slug)
        except:
            raise Http404
    
    def get(self, request, org_slug, format=None):
        org = self.get_object(org_slug)
        self.check_object_permissions(request, org) # checks if the user is allowed for the organization
        serializer = OrganizationSerializer(org)
        is_owner = request.user.id == org.owner.id
        return Response(data={
            'org' : serializer.data,
            'is_owner' : is_owner
        })

class JoinRequestsUserView(APIView):
    def post(self, request, format=None):
        serializer = JoinRequestSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=200)

    def get(self, request, format=None):
        join_requests = JoinRequest.objects.filter(user=request.user)
        serializer = JoinRequestSerializer(join_requests, many=True)
        join_requests_serialized = []

        # Loops the join request to serialize the org and the user for the frontend
        for join_request in join_requests:
            org_serializer = OrganizationSerializer(join_request.org)

            join_requests_serialized.append({
                'join_request_id' : join_request.id,
                'org' : org_serializer.data,
            })

        return Response(join_requests_serialized)

    # delete an join request from the user
    def delete(self, request, req_id, format=None):
        join_request = JoinRequest.objects.get(id=req_id)
        join_request.delete() # delete the request from the database

        return Response(status=204)


class JoinRequestOwnerView(APIView):
    # To accept an join request
    def post(self, request, format=None):
        serializer = OrganizationMemberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        join_request = JoinRequest.objects.get(id=request.data.get('join_req_id'))
        join_request.delete()

        return Response(status=201)

    def get(self, request, org_id, format=None):
        org = Organization.objects.get(id=org_id)

        if org.owner == request.user:
            join_requests = JoinRequest.objects.filter(org=org)
            serializer = JoinRequestSerializer(join_requests, many=True)
            join_requests_serialized = []

            for join_request in join_requests:
                org_serializer = OrganizationSerializer(join_request.org)
                user_serializer = UserSerializer(join_request.user)

                join_requests_serialized.append({
                    'join_request_id' : join_request.id,
                    'org' : org_serializer.data,
                    'user' : user_serializer.data
                })

            return Response(join_requests_serialized)

        return Response({
            'error' : 'You have no permissions',
        }, status=405)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        organizations = Organization.objects.filter(name__icontains=query)
        orgs = []

        # filters the organizations where the user is already in ore have requested it
        for org in organizations:
            if not JoinRequest.objects.filter(org=org, user=request.user).exists() \
                    and not OrganizationMember.objects.filter(org=org, user=request.user).exists() \
                    and request.user != org.owner:
                orgs.append(org)


        serializer = OrganizationSerializer(orgs, many=True)
        return Response(serializer.data)

    return Response({'organizations': []})
