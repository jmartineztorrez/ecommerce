from django.shortcuts import render,redirect
from .models import *

#from .forms import ProductoForm

from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from .forms import UserForm,FormularioLogin,CestaForm,UserCreationForm
from django.views.generic.edit import CreateView,FormView


# Create your views here.
class Test(ListView):
    model = Categoria
    template_name = 'sprint8/index.html'
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


class AgregarProductoCesta(CreateView):
    model = Cesta
    form_class = CestaForm
    template_name = 'sprint8/agregar_a_cesta.html'
    success_url= reverse_lazy('sprint8:index')

    def get_context_data(self, **kwargs):
        context=super(AgregarProductoCesta, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('pk', None)
        context['productos']=Producto.objects.filter(id=parametro)
        return context

    def form_valid(self,form):
        self.object = form.save(commit=False)
        producto= Producto.objects.get(pk = self.kwargs.get('pk',None))
        usuario = User.objects.get(pk = self.kwargs.get('id',None))
        self.object.productos = producto
        self.object.clientes = usuario
        self.object.save()
        return super(AgregarProductoCesta,self).form_valid(form)

class ListarCesta(ListView):
    model = Cesta
    template_name='sprint8/cesta.html'
    context_object_name = 'categorias'
    queryset = Categoria.objects.all()

    def get_context_data(self, **kwargs):
        context=super(ListarCesta, self).get_context_data(**kwargs)
        parametro = self.kwargs.get('pk', None)
        context['cestas']=Cesta.objects.filter(clientes=parametro)
        return context

#Usuario
class RegistroUsuario(CreateView):
        model = User
        template_name = "sprint8/register_usuario.html"
        form_class= UserForm
        context_object_name = 'categorias'
        queryset = Categoria.objects.all()
        success_url=reverse_lazy('sprint8:login')
        
class LoginUser(FormView):
        model = User
        template_name='sprint8/login.html'
        form_class=FormularioLogin
        context_object_name = 'categorias'
        queryset = Categoria.objects.all()
        success_url=reverse_lazy('sprint8:index')
        
        def dispatch(self, request, *args, **kwargs):
                if request.user.is_authenticated:
                        return HttpResponseRedirect(self.get_success_url())
                return super(LoginUser,self).dispatch(request, *args, **kwargs)

        def form_valid(self,form):
                login(self.request,form.get_user())
                return super(LoginUser,self).form_valid(form)

def logoutUsuario(request):
        logout(request)
        return HttpResponseRedirect('accounts/login/')

class eliminarCesta(DeleteView):
        model=Cesta
        success_url = reverse_lazy('sprint8:index')

        def get(self, request, *args, **kwargs):
                return self.post(request, *args, **kwargs)

class limpiarCesta(DeleteView):
        model=Cesta
        success_url = reverse_lazy('/')

        def get(self, request, *args, **kwargs):
                return self.post(request, *args, **kwargs)
  

class EditarCesta(UpdateView):
        model = Cesta
        form_class = CestaForm
        template_name = 'sprint8/agregar_a_cesta.html'
        success_url = reverse_lazy('sprint8:index')
        context_object_name = 'cestas'
        queryset = Cesta.objects.all()

        

        def get_context_data(self,**kwargs):
                context = super().get_context_data(**kwargs)
                context['cestas'] = Cesta.objects.filter(id = 'pk')
                return context

        

    
        def form_valid(self,form):

                self.object = form.save(commit=False)
                producto= Producto.objects.get(pk = self.kwargs.get('pk',None))
                usuario = User.objects.get(pk = self.kwargs.get('id',None))
                self.object.productos = producto
                self.object.clientes = usuario
                self.object.save()
                return super(AgregarProductoCesta,self).form_valid(form)