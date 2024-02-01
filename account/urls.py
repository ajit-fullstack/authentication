from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegestrationView.as_view(), name="register"), 
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('changePass/', UserChangePassView.as_view(), name="changePass"),
]