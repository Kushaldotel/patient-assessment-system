from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'phone', 'date_of_birth', 'age', 'address', 'clinic_user')
    list_filter = ('full_name','age','gender',)
    search_fields = ('full_name', 'phone', 'clinic_user__email')
