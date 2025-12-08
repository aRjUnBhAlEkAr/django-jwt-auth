# django required imports
from django.urls import path

# local imports
from auth_app.views import (
    UserRegistrationView,
    UserLoginView
)

urlpatterns = [
   path('register', UserRegistrationView.as_view(), name="user-registration"),
   path('login', UserLoginView.as_view(), name="user-login"),
]