from django.urls import path
from .views import *

urlpatterns = [
    path('create/', createTodo, name="create"),
    path('getAllTodo/', getAllTodo, name='getAllTodo')
]
