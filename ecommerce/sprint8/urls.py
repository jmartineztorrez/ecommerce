from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('test/', Test.as_view(), name="test"),
    path('listar/<int:id>', ListaCategoriaProducto.as_view(), name="listar")
]