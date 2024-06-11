from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient,Assessment
from .serializers import PatientSerializer,PatientDetailSerializer,AssessmentSerializer,AssessmentCreateSerializer,AssessmentDetailSerializer,PatientWithAssessmentSerializer
from .utils import CustomPageNumberPagination
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from django.db import transaction

class PatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['full_name', 'gender', 'age']
    search_fields = ['full_name']
    ordering_fields = ['full_name', 'age']
    ordering = ['age']

    def get_queryset(self):
        return self.queryset.filter(clinic_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(clinic_user=self.request.user)


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientDetailSerializer
    permission_classes = [IsAuthenticated]


class AssessmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Assessment.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['assessment_type', 'assessment_date']
    search_fields = ['assessment_type']
    ordering_fields = ['assessment_date']
    ordering = ['-assessment_date']

    def get_queryset(self):
        return self.queryset.filter(clinic=self.request.user)

    def perform_create(self, serializer):
        # Assign the current logged-in user as the clinic for the new assessment
        serializer.save(clinic=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AssessmentCreateSerializer
        return AssessmentSerializer

    def get_serializer(self, *args, **kwargs):
        # Pass the request context to the serializer
        kwargs['context'] = self.get_serializer_context()
        return super().get_serializer(*args, **kwargs)


class AssessmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(clinic=self.request.user)


class PatientWithAssessmentCreateAPIView(generics.CreateAPIView):
    serializer_class = PatientWithAssessmentSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            with transaction.atomic():
                self.perform_create(serializer)
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)