# django required imports
from django.urls import path

# local imports
from auth_app.views import (
    UserRegistrationView
)

urlpatterns = [
   path('register', UserRegistrationView.as_view(), name="user-registration")
]