from rest_framework import serializers
from .models import PatientProfile, DoctorProfile, NurseProfile, PharmacistProfile

class PatientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientProfile
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'profile_pic',
            'gender',
            'dob',
            'bio'
            ]
    
    def create(self, validated_data):
        return PatientProfile.objects.create(user = self.context.get('user'), **validated_data)

class DoctorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorProfile
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'profile_pic',
            'gender',
            'dob',
            'qualifications',
            'speciality',
            'department',
            'bio'
            ]

        depth = 1
    def create(self, validated_data):
        return DoctorProfile.objects.create(user = self.context.get('user'), **validated_data)

class NurseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseProfile
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'profile_pic',
            'gender',
            'dob',
            'qualifications',
            'bio'
            ]

    def create(self, validated_data):
        return NurseProfile.objects.create(user = self.context.get('user'), **validated_data)

class PharmacistProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacistProfile
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'profile_pic',
            'gender',
            'dob',
            'qualifications',
            'bio'
            ]

    def create(self, validated_data):
        return PharmacistProfile.objects.create(user = self.context.get('user'), **validated_data)