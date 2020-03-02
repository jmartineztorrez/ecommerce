from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView


# Create your views here.
class Test(ListView):
    model = Categoria
    template_name = 'sprint8/index.html'
    context_object_name = 'categorias'
    queryset = Categoria.objects.all()

class Cesta(ListView):
    model = Categoria
    template_name = 'sprint8/cesta.html'
    context_object_name = 'categorias'
    queryset = Categoria.objects.all()

class ListaCategoriaProducto(ListView):
    model = Categoria
    template_name = 'sprint8/listar.html'
    context_object_name = 'categorias'
    queryset = Categoria.objects.all()


    def get_context_data(self, **kwargs):
        context=super(ListaCategoriaProducto, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('id', None)
        context['productos']=Producto.objects.filter(categorias=parametro)
        context['categoriasId']=Categoria.objects.filter(id=parametro)
        return context
        
