from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientListCreateAPIView, PatientDetailView,AssessmentListCreateAPIView,AssessmentDetailAPIView,PatientWithAssessmentCreateAPIView


urlpatterns = [
    path('patients/', PatientListCreateAPIView.as_view(), name='patient-list-create',),
    path('patients/create_with_assessment/', PatientWithAssessmentCreateAPIView.as_view(), name='patient-create-with-assessment'),
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),\
    path('assessments/', AssessmentListCreateAPIView.as_view(), name='assessment-list-create'),
    path('assessments/<int:pk>/', AssessmentDetailAPIView.as_view(), name='assessment-detail'),
]
