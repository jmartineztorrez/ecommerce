from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Test.as_view(), name="index"),
    path('listar/<int:id>', ListaCategoriaProducto.as_view(), name="listar"),
    path('cesta/', Cesta.as_view(), name="cesta"),
]