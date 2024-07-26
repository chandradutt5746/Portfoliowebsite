from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, index, ProjectDetailView, ContactMessageViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'contact-messages', ContactMessageViewSet)

urlpatterns = [
    # path('', index),
    path('api/', include(router.urls)),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]
