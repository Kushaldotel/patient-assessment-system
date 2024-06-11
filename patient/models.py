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
