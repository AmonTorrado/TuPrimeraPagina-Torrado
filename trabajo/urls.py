from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name='Index'),
    path("listaClientes", views.leer_clientes, name='listaClientes'),
    path("listaVentas", views.lista_ventas.as_view(), name='listaVentas'),
    path("crearCliente", views.crear_cliente, name='crearCliente'),
    path("comprarProducto", views.comprar_producto, name='comprarProducto'),
    path("nuevoInsumo", views.crear_insumo, name='nuevoInsumo'),
    path("busquedaBD", views.busqueda_en_bd, name='busquedaBD'),
    path('inicio', views.inicio, name='inicio'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)