from rest_framework.routers import DefaultRouter
from .views import (MedicineViewSet)

router = DefaultRouter()

router.register('medicines', MedicineViewSet, basename='medicines')

urlpatterns = [

] + router.urls