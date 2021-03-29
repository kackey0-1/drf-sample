from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
# doctors/
router.register(r'doctors', views.DoctorsViewSet, 'doctors')
# mass_delete/mass_delete/
router.register(r'mass_delete', views.MassDeleteArtifactsViewSet, 'mass_delete')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/listing/', views.listing),
]
