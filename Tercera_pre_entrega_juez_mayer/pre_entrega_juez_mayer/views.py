from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    return render(request, 'index.html')

def about(request):

    return render(request, 'about.html')

def contact(request):

    return render(request, 'contact.html')

def buscar_libro(request):

    return render(request, 'buscar_libro.html')

def agregar_libro(request):

    return render(request, 'agregar_libro.html')