from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegestrationView.as_view(), name="register")
]