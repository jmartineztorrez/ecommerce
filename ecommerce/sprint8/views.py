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

    def post(self,request,pk,*args,**kwargs):
        objects=Categoria.objects.get(id=pk).prefetch_related('productos')
        context['categorias']=objects
        return context
        
