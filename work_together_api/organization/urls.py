from django.urls import path
from . import views

# Urls for Organizations

urlpatterns = [
    path('orgs/', views.GetOrganizations.as_view()),
    path('org/create/', views.CreateOrganization.as_view()),
    path('org/search/', views.search),
    path('org/user/join-request/', views.JoinRequestsUserView.as_view()),
    path('org/user/delete-request/<int:req_id>/', views.JoinRequestsUserView.as_view()),
    path('org/owner/<int:org_id>/join-requests/', views.JoinRequestOwnerView.as_view()),
    # is for the dession if the join request ist accepted or not
    path('org/owner/decide/join-request/', views.JoinRequestOwnerView.as_view()),
    path('org/<slug:org_slug>/', views.DetailOrganization.as_view()),
]
