from django.contrib import admin
from .models import DoctorProfile, PatientProfile, NurseProfile, PharmacistProfile

admin.site.register(DoctorProfile)
admin.site.register(PatientProfile)
admin.site.register(NurseProfile)
admin.site.register(PharmacistProfile)
