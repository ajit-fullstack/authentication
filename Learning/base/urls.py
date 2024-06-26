from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerUser, name="register"),
    path("logout/", views.logoutUser, name="logout"),
    path("home/", views.home, name="home"),
    path("room/<int:pk>/", views.room, name="room"),
    path("create-room/", views.createRoom, name="create-room"),
    path("update-room/<int:pk>/", views.updateRoom, name="update-room"),
    path("delete-room/<int:pk>/", views.deleteRoom, name="delete-room")
]

