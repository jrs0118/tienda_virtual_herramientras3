"""tienda_virtual URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventario.views import  editar_producto, eliminar_producto, mostrar_productos, vista_busqueda_productos, obtener_producto, agregar_producto, mostrar_productos, editar_producto, eliminar_producto
from ventas.views import agregar_venta, agregar_venta2, mostrar_venta


urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_productos/', vista_busqueda_productos),
    path('obtener_producto/', obtener_producto),
    path('agregar_producto/', agregar_producto,name='add-prods'),
    path('mostrar_productos/', mostrar_productos, name='show-prods'),
    path('editar_producto/<int:pk>', editar_producto, name='edit-prods'),
    path('eliminar_producto/<int:pk>', eliminar_producto, name="del-prods"),
    path('agregar_venta/<int:pk>', agregar_venta, name="add-venta"),
    path('agregar_venta2/<int:pk>', agregar_venta2),
    path('mostrar_venta/', mostrar_venta, name ="ventas"),
]

    