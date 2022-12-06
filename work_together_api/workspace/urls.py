from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('workspace/create/', views.CreateWorkspace.as_view()),
    path('workspace/get/<str:org_slug>/<str:ws_slug>/', views.GetWorkspace.as_view()),
    path('org/<int:org_id>/workspace/get/', views.GetWorkspaces.as_view()),
    path('workspace/<int:ws_id>/file-upload/', views.UploadFile.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
