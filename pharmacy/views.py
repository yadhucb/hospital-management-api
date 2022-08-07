from rest_framework import viewsets
from rest_framework import authentication, permissions
from .serializers import MedicineSerializer
from .models import Medicine

class MedicineViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = MedicineSerializer
    queryset = Medicine.objects.all()


