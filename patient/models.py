from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    clinic_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    full_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Calculate age based on date_of_birth
        from datetime import date
        today = date.today()
        self.age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))
        super(Patient, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class Assessment(models.Model):
    ASSESSMENT_TYPES = [
        ('cognitive', 'Cognitive Status'),
        ('physical', 'Physical Health'),
        ('mental', 'Mental Health'),
        ('emotional', 'Emotional Well-being'),
        ('social', 'Social Functioning'),
        ('nutrition', 'Nutritional Status'),
        ('functional', 'Functional Ability'),
        ('pain', 'Pain Assessment'),
        ('medication', 'Medication Adherence'),
        ('substance', 'Substance Use'),
        ('sleep', 'Sleep Quality'),
        ('environmental', 'Environmental Safety'),
        ('financial', 'Financial Stability'),
        # Add more assessment types as needed
    ]

    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPES)
    clinic = models.ForeignKey(User, on_delete=models.CASCADE, related_name='clinic')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient')
    assessment_date = models.DateTimeField()
    questions_and_answers = models.JSONField(default=list)  # JSON field to store questions and answers
    final_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Assessment"
        verbose_name_plural = "Assessments"

    def __str__(self):
        return f"{self.assessment_type} Assessment for {self.patient.full_name}"