from django.urls import path
from . import views

urlpatterns = [
    path('workspace/create/', views.CreateWorkspace.as_view())
]
