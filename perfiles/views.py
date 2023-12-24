from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from . forms import CustomUserCreationForm
from . models import PerfilUsuario
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.

class PerfilUsuarioCreateView(CreateView):
    model = PerfilUsuario
    template_name = "crear_perfil.html"
    sucess_url = reverse_lazy("ver perfil")
    fields = ["usuario","imagen", "rol"]
    login_url = "/usuarios/login"
   
def crear_usuario(request):
       return render(request, "crear_perfil.html")
       
    
class PerfilUsuarioUpdateView(LoginRequiredMixin, CreateView):
    model = PerfilUsuario
    template_name = "editar_perfil.html"
    success_url = reverse_lazy("ver perfil")
    fields = ["imagen", "rol"]
    login_url = "/usuarios/login"
    
@login_required(login_url="login")
def perfil_usuario(request):
    try:
        request.user.perfil
        return render(request, "usuarios/perfil.html")
    except:
        return redirect("crear perfil")