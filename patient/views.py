from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient,Assessment
from .serializers import PatientSerializer,PatientDetailSerializer,AssessmentSerializer,AssessmentCreateSerializer
from .utils import CustomPageNumberPagination
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Specify the custom pagination class
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['full_name', 'gender', 'age']
    search_fields = ['full_name']
    ordering_fields = ['full_name', 'age']
    ordering = ['age']

    def get_queryset(self):
        return Patient.objects.filter(clinic_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(clinic_user=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    permission_classes = [IsAuthenticated]

class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['assessment_type', 'assessment_date']
    search_fields = ['assessment_type']
    ordering_fields = ['assessment_date']
    ordering = ['-assessment_date']

    def get_queryset(self):
        user = self.request.user
        return self.queryset.filter(clinic=user)

    def get_serializer_class(self):
        if self.action == 'create':
            return AssessmentCreateSerializer
        return AssessmentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        patient_id = self.request.data.get('patient')
        patient = Patient.objects.get(pk=patient_id)
        if patient.clinic_user == user:
            serializer.save(clinic=user)
        else:
            raise serializers.ValidationError("You can only create assessments for your own patients.")