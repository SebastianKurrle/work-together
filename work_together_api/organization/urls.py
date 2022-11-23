from django.urls import path
from . import views

urlpatterns = [
    path('org/create/', views.CreateOrganization.as_view()),
    path('orgs/', views.GetOrganizations.as_view()),
]
