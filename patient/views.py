from rest_framework import viewsets
from rest_framework import permissions ,authentication
from rest_framework.response import Response
from .serializers import PatientSerializer
from .models import Patient
from pharmacy.models import Medicine
from users.models import PatientProfile, DoctorProfile

class PatientViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication]

    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

    def create(self, request):
        data = request.data
        patient_profile = data.pop("patient_profile")
        assigned_doctors = data.pop('assigned_doctors')
        medicines = data.pop('medicines')
        patient_profile = PatientProfile.objects.get(id = patient_profile["id"])
        patient = Patient.objects.create(patient_profile = patient_profile, **data) 

        for assigned_doctor in assigned_doctors:
            doctor = DoctorProfile.objects.get(id = assigned_doctor['id'])
            patient.assigned_doctors.add(doctor)
            patient.save()

        for medicine in medicines:
            medicine = Medicine.objects.get(id = medicine['id'])
            patient.medicines.add(medicine)
            patient.save()

        serializer = PatientSerializer(patient)
        return Response(data=serializer.data)

    def update(self, request, **kwargs):
        patient = Patient.objects.get(id = kwargs.get('pk'))
        data = request.data
        patient_profile = data.pop("patient_profile")
        assigned_doctors = data.pop('assigned_doctors')
        medicines = data.pop('medicines')
        patient_profile = PatientProfile.objects.get(id = patient_profile["id"])
        patient.patient_profile = patient_profile
        patient.diseases = request.data['diseases']
        patient.notes = request.data['notes']
        patient.assigned_doctors.clear()
        patient.medicines.clear()
        patient.save()

        for assigned_doctor in assigned_doctors:
            doctor = DoctorProfile.objects.get(id = assigned_doctor['id'])
            patient.assigned_doctors.add(doctor)
            patient.save()

        for medicine in medicines:
            medicine = Medicine.objects.get(id = medicine['id'])
            patient.medicines.add(medicine)
            patient.save()

        serializer = PatientSerializer(patient)
        return Response(data=serializer.data)

