from django.shortcuts import render
from . models import Insumo, Producto
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

# Create your views here.
@login_required(login_url="login")
def crear_producto(request): 
    print("Mostrar request.post:")
    print(request.POST)
    
    if request.method == "POST":
        nuevo_producto = Producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            cantidad_en_stock = request.POST["cantidad_en_stock"]
        )
        nuevo_producto.save()
        return render(request, "inicio.html")
    
    return render(request, 'producto_formulario.html')

def inicio(request):
    return render(request, "inicio.html")

def index(request):
    return render(request,"inicio.html")

def crear_insumo(request):
    if request.method == "POST":
        nuevo_formulario = InsumoForm(request.POST)
        
        if nuevo_formulario.is_valid():
            informacion = nuevo_formulario.cleaned_data
            nuevo_insumo = Insumo(
                    nombre=informacion["nombre"],
                    descripcion=informacion["descripcion"],
                    unidad_de_medida=informacion["unidad_de_medida"],
                    cantidad_en_stock=informacion["cantidad_en_stock"]
                    )
                
            nuevo_insumo.save()
            return render(request, 'index.html')
    else:
        nuevo_formulario = InsumoForm()
        return render(request, 'nuevo_insumo.html', {"formulario": nuevo_formulario})
    
def busqueda_en_bd(request):
    if request.GET.get("nombre", False):
        busqueda = request.GET["nombre"]
        lista_productos = Producto.objects.filter(nombre__icontains=busqueda)
        return render(request, 'busqueda.html', {'lista': lista_productos})
    return render(request, 'busqueda.html')

def comprar_producto(request):
    # En esta vista estamos buscando un producto en específico y al comprarlo vamos a descontar la cantidad comprada
    # del stock.
    if request.method == "POST":
        busqueda = request.POST["nombre"]
        producto = Producto.objects.get(nombre=busqueda)
        cantidad_compra = int(request.POST["cantidad"])
        # Modificar el stock del producto y guardarlo en la base de datos:
        producto.cantidad_en_stock = producto.cantidad_en_stock - cantidad_compra
        producto.save()
        
        return render(request, 'comprar_producto.html', {'producto': producto.nombre, 'cantidad_stock': producto.cantidad_en_stock})
    
    return render(request, 'comprar_producto.html')

def crear_cliente(request):
    if request.method == "POST":
        mi_formulario = ClienteFormulario(request.POST) # Aqui me llega la informacion del html
        
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            cliente = Cliente(
                nombre=informacion["nombre"],
                nro_cuit=informacion["nro_cuit"],
                email=informacion["email"]
                )
            cliente.save()
            return render(request, "index.html")
        else:
            return render(request, 'crear_cliente.html', {"errors": mi_formulario.errors})
    else:
        mi_formulario = ClienteFormulario()
        return render(request, "crear_cliente.html", {"mi_formulario": mi_formulario})
    
class lista_ventas(ListView):
    model = Venta
    context_object_name = "ventas"
    template_name = "lista_ventas.html"
    
def leer_clientes(request):
    lista_clientes = Cliente.objects.all()
    return render(request, "lista_clientes.html", {"clientes": lista_clientes})
