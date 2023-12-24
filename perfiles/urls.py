from django.urls import path, include
from . views import perfil_usuario, PerfilUsuarioCreateView, PerfilUsuarioUpdateView, crear_usuario
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('perfilUsuario', perfil_usuario, name='ver perfil'),
    path('/crear_perfil', PerfilUsuarioCreateView.as_view()),# crear_usuario, name = "crear perfil"),
    path('<pk>/editar_perfil', PerfilUsuarioUpdateView.as_view(), name='editar perfil')
]