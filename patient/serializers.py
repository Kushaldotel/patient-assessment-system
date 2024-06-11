from rest_framework import serializers
from .models import Patient, Assessment

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'full_name', 'gender', 'phone', 'date_of_birth', 'age', 'address']
        read_only_fields = ['age', 'clinic_user']

class PatientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Assessment
        fields = '__all__'

class AssessmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'