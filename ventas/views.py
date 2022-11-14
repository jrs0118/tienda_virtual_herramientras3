from datetime import datetime
import smtplib
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from inventario.models import Productos
from ventas.models import Venta


def mostrar_venta(request):

    productos = Productos.objects.all().order_by('id_producto')
    return render(request,'ventas.html',{'productos':productos})

def agregar_venta(request):
    if request.method=="POST":
            costo = Productos.cost     
            id= Productos.id_producto
            nombreCom = request.POST["txt_nombres"]
            tipoDoc = request.POST["select_tipo_doc"]
            numDoc = request.POST["txt_num_doc"]
            correoDoc = request.POST["txt_correo"]
            direccionDoc = request.POST["txt_direccion"]
            deptoDoc = request.POST["select_depto"]
            ciudadDoc = request.POST["select_ciudad"]
            telefonoDoc = request.POST["txt_telefono"]
            data = Venta(nombres=nombreCom, tipo_doc=tipoDoc, num_doc=numDoc, 
                                correo= correoDoc, direccion=direccionDoc,depto=deptoDoc,ciudad=ciudadDoc,
                                telefono=telefonoDoc,total_venta=costo, id_producto= id)
            data.save()
            nombre_producto = Productos.name        
            Productos.cantidad_stock -= 1
            Productos.save()
            correo_venta (correoDoc,nombreCom,nombre_producto,costo,direccionDoc)
            print("Venta exitosa")
            return redirect('/agregar_venta')                  
    else:
        print("Venta no exitosa")
        return render (request, "add_venta.html")


def correo_venta(correoDoc,nombreCom,nombre_producto,costo,direccionDoc):
    today = datetime.now()
    fecha = today.strftime('%b %d, %Y')
    
    textoAsunto = "Compra realizada"
    textoMensaje = f"Gracias por comprar: {nombre_producto}, por valor de${costo} mil pesos"                    
    asunto = "Subject: %s\n"%(textoAsunto)
#buscar como enviar el correo
