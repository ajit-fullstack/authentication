from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegestrationView.as_view(), name="register"), 
    path('login/', UserLoginView.as_view(), name="login"),
    path('profile/', UserProfileView.as_view(), name="profile"),
    path('changePass/', UserChangePassView.as_view(), name="changePass"),
    path('reset-pass-link/', SendPassResetEmailView.as_view(), name="reset-pass-link"),
    path('reset-password/<uid>/<token>', UserPassResetView.as_view(), name="reset-password"),
]
