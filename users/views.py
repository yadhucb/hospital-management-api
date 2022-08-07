from django.shortcuts import render
from .serializers import (DoctorProfileSerializer, PatientProfileSerializer, 
NurseProfileSerializer, PharmacistProfileSerializer)
from .models import DoctorProfile, PatientProfile, NurseProfile, PharmacistProfile
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions,authentication

class DoctorProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = DoctorProfileSerializer
    queryset = DoctorProfile.objects.all()

    def create(self,request,*args,**kwargs):
        serializer=DoctorProfileSerializer(data=request.data, context = {'user' : request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class PatientProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = PatientProfileSerializer
    queryset = PatientProfile.objects.all()

    def create(self,request,*args,**kwargs):
        serializer=PatientProfileSerializer(data=request.data, context = {'user' : request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class NurseProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    serializer_class = NurseProfileSerializer
    queryset = NurseProfile.objects.all()

    def create(self,request,*args,**kwargs):
        serializer=NurseProfileSerializer(data=request.data, context = {'user' : request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class PharmacistProfileViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    serializer_class = PharmacistProfileSerializer
    queryset = PharmacistProfile.objects.all()

    def create(self,request,*args,**kwargs):
        serializer=PharmacistProfileSerializer(data=request.data, context = {'user' : request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
