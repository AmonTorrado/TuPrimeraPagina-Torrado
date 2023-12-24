from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate

# Create your views here.
def login_request(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            
            login(request, user)
            return render(request, "login.html", {"mensaje": f'Bienvenido {user.username}'})
        else:
            return render(request, "login.html", {"formulario": formulario})
    
    else:
        formulario = AuthenticationForm()
        return render(request, "login.html", {"formulario": formulario})