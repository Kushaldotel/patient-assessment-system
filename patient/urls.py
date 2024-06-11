from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientDetailView

router = DefaultRouter()
router.register(r'', PatientViewSet, basename='patient')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
]
