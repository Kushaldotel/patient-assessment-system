from django.contrib import admin
from .models import Patient,Assessment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'phone', 'date_of_birth', 'age', 'address', 'clinic_user')
    list_filter = ('full_name','age','gender',)
    search_fields = ('full_name', 'phone', 'clinic_user__email')

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('assessment_type','clinic', 'patient', 'assessment_date', 'final_score', 'created_at', 'updated_at')
    list_filter = ('assessment_type', 'patient', 'assessment_date')
    search_fields = ('assessment_type', 'patient__full_name')
    readonly_fields = ('created_at', 'updated_at')