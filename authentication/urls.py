from django.urls import path
from .views import RegistrationView

urlspatterns = [
    path('register',RegistrationView.as_view(), name='register'),
]
