from django.urls import path
from .views import (
    UserRegistrationView
)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('token/', obtain_auth_token),


]