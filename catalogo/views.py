from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro

# Create your views here.
def inicio(request):
    return render(request, 'catalogo/inicio.html')

def listar_libros(request):
    libros = Libro.objects.all()

    contexto = {
        'libros': libros
    }

    return render(request, 'catalogo/libros.html', contexto)