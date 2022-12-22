from rest_framework import serializers, validators
from .models import Organization, JoinRequest, OrganizationMember
from users.serializers import UserSerializer

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'description',
            'get_absolute_url',
        )

    def create(self, validated_data):
        name = validated_data.get('name')
        desc = validated_data.get('description')
        slug = name.lower()
        owner = self.context.get('request').user

        org = Organization.objects.create(name=name, description=desc, org_slug=slug, owner=owner)
        return org

# Handles the serialization for the join requests
class JoinRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinRequest
        fields = (
            'org',
            'user'
        )

    def create(self, validated_data):
        org = validated_data.get('org')
        user = validated_data.get('user')
        join_request = JoinRequest.objects.create(org=org, user=user)
        return join_request

class OrganizationMemberCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationMember
        fields = (
            'org',
            'user'
        )

    def create(self, validated_data):
        org = validated_data.get('org')
        user = validated_data.get('user')
        org_member = OrganizationMember.objects.create(org=org, user=user)
        return org_member

class OrganizationMemberSerializer(serializers.ModelSerializer):
    org = OrganizationSerializer()
    user = UserSerializer()

    class Meta:
        model = OrganizationMember
        fields = (
            'org',
            'user'
        )

    def create(self, validated_data):
        org = validated_data.get('org')
        user = validated_data.get('user')
        org_member = OrganizationMember.objects.create(org=org, user=user)
        return org_member

