from rest_framework.permissions import BasePermission
from .models import OrganizationMember

class IsMemberOfOrganization(BasePermission):
    def has_object_permission(self, request, view, obj):
        # obj ist das angeforderte Organization-Objekt
        return OrganizationMember.objects.filter(org=obj, user=request.user).exists() or obj.owner == request.user
