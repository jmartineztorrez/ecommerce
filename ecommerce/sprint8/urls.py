from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', Test.as_view(), name="index"),
    path('listar/<int:id>', ListaCategoriaProducto.as_view(), name="listar"),
    path('cesta/<int:pk>', ListarCesta.as_view(), name="cesta"),
    path('agregar_cesta/<int:pk>/<int:id>',AgregarProductoCesta.as_view(), name ='agregar_cesta'),
    path('editar_cesta/<int:pk>/<int:id>', EditarCesta.as_view(), name="editar_cesta"),
    path('registro/', RegistroUsuario.as_view(), name="registro"),
    path('accounts/login/',LoginUser.as_view(), name ='login'),
    path('logout',login_required(logoutUsuario), name ='logout'),
]