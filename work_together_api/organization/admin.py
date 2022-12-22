from django.contrib import admin
from .models import Organization, JoinRequest, OrganizationMember

admin.site.register(Organization)
admin.site.register(JoinRequest)
admin.site.register(OrganizationMember)
