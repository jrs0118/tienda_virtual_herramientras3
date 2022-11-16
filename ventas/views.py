from datetime import datetime
from django.shortcuts import redirect, render
from inventario.models import Productos
from ventas.models import Venta
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import smtplib

def mostrar_venta(request):
 productos = Productos.objects.all() 
 return render(request,'ventas.html',{'productos':productos})
 
def agregar_venta(request,pk):
 productos = Productos.objects.get(id_producto=pk)
 return render(request,'add_venta.html',{'productos':productos})

def agregar_venta2(request,pk):
    producto = Productos.objects.get(id_producto=pk)    
    if request.method=="POST":
            costo = producto.cost     
            id= producto.id_producto
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
                                telefono=telefonoDoc,total_venta=costo)
            data.save()
            nombre_producto = producto.name        
            producto.cantidad_stock -= 1
            producto.save()
         #   correo_venta (correoDoc)
            print("Venta exitosa")
            return redirect('/mostrar_venta/')                  
    else:
        print("Venta no exitosa")
        return render (request, "add_venta.html")

def correo_venta(request, correoDoc):
    try:

        mensaje = request.GET.get('COMPRA REALIZADA')
        correoDoc= request.GET.get("txt_correo")
        asunto = request.GET.get('COMPRA REALIZADA')

        body = 'Compra: {}\n\n{}'.format(asunto, mensaje)
        server = smtplib.SMTP('smtp.gmail.com','587')
        server.starttls()
        server.login('juanitars@gmail.com','juanita1801')
        server.sendmail('juanitars@gmail.com', correoDoc, body)
        server.quit()
        return JsonResponse({'status':True, 'mensaje':'Correo enviado exitosamente'})

    except Exception as e:
        return JsonResponse({'status':False, 'mensaje':'Ocurrio un error al momento de enviar el correo', 'error':e.__str__()})

#def correo_venta(correoDoc):
 #   subject = 'Compra realizada'
  #  template = get_template('add_venta.html')
#
 #   content = template.render({
  #      'txt_correo': correoDoc,
   # })

    #message = EmailMultiAlternatives(subject, #Titulo
     #                               'COMPRA REALIZADA' ,
      #                              settings.EMAIL_HOST_USER, #Remitente
       #                             [agregar_venta.correoDoc]) #Destinatario

    #message.attach_alternative(content, '/mostrar_venta/')
    #message.send()