from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView


# Create your views here.
class Test(TemplateView):
    template_name = 'sprint8/index.html'

class ListaCategoriaProducto(ListView):
    model = Categoria
    template_name = 'sprint8/listar.html'

    def get_queryset(self, **kwargs):
        parametro = self.kwargs.get('id',None)
        queryset = Categoria.objects.filter(id=parametro) 
        return queryset

    def get_context_data(self, **kwargs):
        context=super(ListaCategoriaProducto, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('id', None)
        context['productos']=Producto.objects.filter(categorias=parametro)
        return context
        
