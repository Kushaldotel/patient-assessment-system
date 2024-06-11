from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, PatientDetailView,AssessmentViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'assessments', AssessmentViewSet, basename='assessment')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
]
