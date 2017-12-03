from django.shortcuts import render
from . models import Prato, Requisitado, Imagem

def prato_list(request):
    lista_pratos = Prato.objects.all()
    lista_requisitados = Requisitado.objects.all()
    return render(request, 'chef/prato_list.html', {'lista_pratos':lista_pratos, 'lista_requisitados':lista_requisitados})

def home(request):
    lista_requisitados = Requisitado.objects.all()
    return render(request, 'chef/home.html', {'lista_requisitados':lista_requisitados})

def galeria(request):
    lista_imagens = Imagem.objects.all()
    return render(request, 'chef/galeria.html', {'lista_imagens':lista_imagens})
