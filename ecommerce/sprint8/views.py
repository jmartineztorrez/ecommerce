from django.shortcuts import render
from .models import *
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DeleteView


# Create your views here.
class Test(TemplateView):
    template_name = 'sprint8/index.html' 