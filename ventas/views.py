from datetime import datetime
import smtplib
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from inventario.models import Productos
from ventas.models import Venta


def ventas_view(request):
    productos = Productos.objects.all().order_by('id_producto')
    return render(request,'ventas.html',{'productos':productos})

def obtenerAdmin():
    correos_superusuarios = User.objects.filter(is_superuser=True).values_list('email')
    if correos_superusuarios.__len__() > 0:
        return True
    else:
        return False

def guardar_venta(request,pk): 
    producto = Productos.objects.get(id_producto=pk)
    estado = obtenerAdmin()
    if request.method == 'POST': 
        if estado == True:       
            id = producto.id_producto   
            costo = producto.cost     
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
                                telefono=telefonoDoc,id_producto_id = id ,total_venta=costo)
            data.save()
            nomProducto = producto.name        
            producto.cantidad_stock -= 1
            producto.save()
            enviarCorreoAdmin(nombreCom,nomProducto,costo)
            enviarCorreoComprador(correoDoc,nombreCom,nomProducto,costo,direccionDoc)
            print("Se guardo la venta")
            return redirect('ventas')
        else:
            print("NO se guardo la venta no hay admin")
            return redirect('ventas')

    else:
        context = {
        'productos': producto,
        }
        return render(request,'guardarVenta.html',context)
def enviarCorreoComprador(correoDoc,nombreCom,nomProducto,costo,direccionDoc):
    today = datetime.now()
    fecha = today.strftime('%b %d, %Y')
    
    textoAsunto = "GRACIAS POR TU COMPRA EN TIENDAS D&J:"
    textoMensaje = f"Gracias por comprar: {nomProducto}, con un costo de: ${costo} mil pesos, se ha aplicado un descuento para tu proxima compra del 15%. En los proximos dias sera enviado el paquete a la direccion: {direccionDoc}, no olvides seguirnos en instagram y facebook como tiendas_d&j"
                    
    asunto = "Subject: %s\n"%(textoAsunto)
    # MANDANDO CORREO
    try:
        message= asunto + """

        Medellin, %s

        Hola %s, 

        %s    


        Que tenga una feliz dia.


        Atentamente,


        TIENDAS D&J

        """% (fecha,nombreCom,textoMensaje)
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('jorgecorreos9412@gmail.com','coke24838014')
        server.sendmail('jorgecorreos9412@gmail.com',correoDoc,message)
        server.quit()

    except NameError :
        print("Ocurrio un error enviando correo al cliente")


        #CREO QUE HASTA ACA
        
def enviarCorreoAdmin(nombreCom,nomProducto,costo):
    correos_superusuarios = User.objects.filter(is_superuser=True).values_list('email')
    nombres_superusuarios = User.objects.filter(is_superuser=True).values_list('username') 
    correoAdmin = correos_superusuarios[0] 
    nombreAdmin = nombres_superusuarios[0]  
    today = datetime.now()
    fecha = today.strftime('%b %d, %Y')
    
    textoAsunto = f"NUEVA COMPRA CLIENTE: {nombreCom}"
    textoMensaje = f"El cliente {nombreCom} acaba de comprar un {nomProducto} con un valor de ${costo} mil pesos. En TIENDAS D&J" 
    asunto = "Subject: %s\n"%(textoAsunto)
    # MANDANDO CORREO
    try:
        message= asunto + """

        %s

        Hola Admin %s, 

        %s    

        

        """% (fecha,nombreAdmin,textoMensaje)
        #correos_superusuarios = User.objects.filter(is_superuser=True).values_list('email')
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('jorgecorreos9412@gmail.com','coke24838014')
        server.sendmail('jorgecorreos9412@gmail.com',correoAdmin,message)
        server.quit()
    except:
        print("Ocurrio un error enviando a correo al admin")
