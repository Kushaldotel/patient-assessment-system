from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Patient
from .serializers import PatientSerializer,PatientDetailSerializer
from .utils import CustomPageNumberPagination
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

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