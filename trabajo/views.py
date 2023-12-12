from django.shortcuts import render, HttpResponse,redirect
from .models import Curso
from .forms import EstudianteForm,ProfesorForm,CursoForm,EntregableForm

# Create your views here.
"""def home(request):
    return render(request, "home.html")"""


def home2(request):    
    return render(request, 'index.html', {})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = EstudianteForm()

    return render(request, 'agregar_estudiante.html', {'form': form})

def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = ProfesorForm()

    return render(request, 'agregar_profesor.html', {'form': form})

def agregar_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = CursoForm()

    return render(request, 'agregar_curso.html', {'form': form})

def agregar_entregable(request):
    if request.method == 'POST':
        form = EntregableForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = EntregableForm()

    return render(request, 'agregar_entregable.html', {'form': form})

def lista_cursos(request,camada):
    lista_cursos = Curso.objects.filter(camada=camada)
    return render(request, 'camada.html', {'lista_cursos': lista_cursos})