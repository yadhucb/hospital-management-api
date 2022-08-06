from django.db import models
from users.models import PatientProfile, DoctorProfile
from pharmacy.models import Medicine

class Patient(models.Model):
    patient_profile = models.OneToOneField(PatientProfile, on_delete=models.CASCADE)
    assigned_doctors = models.ManyToManyField(DoctorProfile, related_name='patient_doctors')
    diseases = models.CharField(max_length=250, null=True, blank=True)
    medicines = models.ManyToManyField(Medicine, related_name='patient_medicines', null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.patient_profile.first_name} {self.patient_profile.last_name}'