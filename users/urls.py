from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    DoctorProfileViewSet, PatientProfileViewSet, NurseProfileViewSet, PharmacistProfileViewSet
)

router = DefaultRouter()
router.register('doctor-profiles',DoctorProfileViewSet, basename='doctor-profiles')
router.register('patient-profiles',PatientProfileViewSet, basename='patient-profiles')
router.register('nurse-profiles', NurseProfileViewSet, basename='nurse-profile')
router.register('pharmacist-profiles', PharmacistProfileViewSet, basename='pharmacist-profile')
urlpatterns = [

]+ router.urls