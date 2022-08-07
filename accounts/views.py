from django.shortcuts import render
from .models import User
from .serializers import UserRegistrationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserRegistrationView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(data = serializer.data)

    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)
        return Response(data = serializer.errors)
        
