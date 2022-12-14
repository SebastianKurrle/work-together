from rest_framework.permissions import BasePermission

class OrganizationIsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(obj.owner == request.user)
        return obj.owner == request.user
