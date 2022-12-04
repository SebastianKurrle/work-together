from django.urls import path
from . import views

urlpatterns = [
    path('workspace/create/', views.CreateWorkspace.as_view()),
    path('org/<int:org_id>/workspace/get/', views.GetWorkspaces.as_view())
]
