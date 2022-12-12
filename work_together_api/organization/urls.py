from django.urls import path
from . import views

urlpatterns = [
    path('orgs/', views.GetOrganizations.as_view()),
    path('org/create/', views.CreateOrganization.as_view()),
    path('org/search/', views.search),
    path('org/join-request/', views.JoinRequestsView.as_view()),
    path('org/<slug:org_slug>/', views.DetailOrganization.as_view()),
]
