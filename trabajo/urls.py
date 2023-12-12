from django.urls import path
from . import views

urlpatterns = [
    path("", views.home2),
    path("agregarCurso", views.agregar_curso, name='agregarCurso'),
    path("agregarProfesor", views.agregar_profesor, name='agregarProfesor'),
    path("agregarEntregable", views.agregar_entregable, name='agregarEntregable'),
    path("agregarEstudiante", views.agregar_estudiante, name='agregarEstudiante'),
    path('camada/<int:camada>', views.lista_cursos, name='lista_cursos'),
]