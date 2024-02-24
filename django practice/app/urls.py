from django.urls import path
from .views import *

urlpattern = [
    path('create/', createTodo, name="create"),
    path('getAllTodo/', getAllTodo, name='getAllTodo')
]
