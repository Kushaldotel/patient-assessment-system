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
        exclude = ['clinic']

    def validate_patient(self, value):
        user = self.context['request'].user
        if value.clinic_user != user:
            raise serializers.ValidationError("You can only create assessments for your own patients.")
        return value

    def create(self, validated_data):
        # Automatically set the clinic field to the current logged-in user
        validated_data['clinic'] = self.context['request'].user
        return super().create(validated_data)

class AssessmentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'

    def validate_patient(self, value):
        user = self.context['request'].user
        if value.clinic_user != user:
            raise serializers.ValidationError("You can only update assessments for your own patients.")
        return value


class NestedAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['assessment_type', 'assessment_date', 'questions_and_answers', 'final_score']

class PatientWithAssessmentSerializer(serializers.ModelSerializer):
    assessments = NestedAssessmentSerializer(many=True)

    class Meta:
        model = Patient
        fields = ['full_name', 'gender', 'phone', 'date_of_birth', 'address', 'assessments']

    def create(self, validated_data):
        assessments_data = validated_data.pop('assessments')
        patient = Patient.objects.create(**validated_data, clinic_user=self.context['request'].user)
        for assessment_data in assessments_data:
            Assessment.objects.create(patient=patient, clinic=self.context['request'].user, **assessment_data)
        return patient