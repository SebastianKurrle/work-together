from rest_framework import serializers, validators
from .models import Organization
from django.contrib.auth.models import User

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            'id',
            'name',
            'description',
            'get_absolute_url',
        )

        extra_kwargs = {
            'name' : {
                'validators' : [
                    validators.UniqueValidator(
                        Organization.objects.all()
                    )
                ]
            },
        }

    def create(self, validated_data):
        name = validated_data.get('name')
        desc = validated_data.get('description')
        slug = name.lower()
        owner = self.context.get('request').user

        org = Organization.objects.create(name=name, description=desc, org_slug=slug, owner=owner)
        return org
