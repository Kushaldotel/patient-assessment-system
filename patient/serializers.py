from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'gender', 'phone', 'date_of_birth', 'age', 'address', 'clinic_user']
        read_only_fields = ['age', 'clinic_user']

class PatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'