from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario, Venta, Marca, Zapatilla, Carrito
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token


# Create your views here.
def register(request):
    if request.method == "POST":
        nombreUser = request.POST['nombre']
        apellidoUser = request.POST['apellido']
        rutUser = request.POST['rut']
        fechaUser = request.POST['fechnac']
        telefonoUser = request.POST['telefono']
        emailUser = request.POST['email']
        claveUser = request.POST['clave']
        confemailUser = request.POST['confemail']
        confclaveUser = request.POST['confclave']
        
        if User.objects.filter(email=emailUser).exists():
            messages.error(request, "Este correo ya está registrado!")
            return redirect('register')
        
        if emailUser != confemailUser:
            messages.error(request, "El email no coincide!")
            return redirect('register')

        if claveUser != confclaveUser:
            messages.error(request, "La contraseña no coincide!")
            return redirect('register')
        
        if not (nombreUser and apellidoUser and rutUser and fechaUser and telefonoUser and emailUser and claveUser and confemailUser and confclaveUser):
            return JsonResponse({'success': False, 'message': 'Por favor, complete todos los campos.'})


        usuario = Usuario.objects.create(rut= rutUser, nombre= nombreUser, apellido= apellidoUser, fecha_nacimiento= fechaUser, telefono= telefonoUser, email= emailUser, contraseña= claveUser)    

        user = User.objects.create_user(username = emailUser, password= claveUser, first_name= nombreUser, last_name= apellidoUser, email = emailUser)
        user.is_active = False
        user.save()
        messages.success(request, 'Cuenta creada con exito. Le hemos enviado un correo de confirmación, porfavor confirma el correo para activar tu cuenta.')
        
        
        # Bienvenidos Email
        subject = "Bienvenidos a Bloodshop - Confirmacion de cuenta"
        message = "Hola " + user.first_name + "! \n" + "Bienvenidos a Bloodshop \n \n Gracias por visitar nuestro sitio web \n Le hemos enviado un correo electronico de confirmación, por favor confirme su dirección de correo electronico. \n \n Gracias."  
        from_email = settings.EMAIL_HOST_USER
        to_list = [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Confirmación Email
        current_site = get_current_site(request)
        email_subject = "Confirma tu Email - Bloodshop"
        message2 = render_to_string('core/email_confirmation.html',{
            
            'name': user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': generate_token.make_token(user)
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [user.email],
        )
        email.fail_silently = True
        email.send()
        return redirect('inicio')  # redirige a la página después del registro exitoso



    return render(request, 'core/register.html')
def activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Tu cuenta ha sido activada, puedes iniciar sesión!")
        return redirect('inicio')
    else:
        return render(request,'core/activation_failed.html')

def signout(request):
    logout(request)
    messages.success(request, "Cerraste Sesión!")
    return redirect('inicio')

def carrito(request):
    return render(request, 'core/carrito.html')
    
def details(request):
    return render(request, 'core/details.html')
    
def detailsgirl1(request):
    nombreZapatilla = "Nike Dunk Animal Instinct"
    marcaZapatilla = "Nike"
    descripcion= "Desde los tableros hasta el skateboard, la influencia del Nike Dunk es innegable. Aunque se presentó como un calzado de básquetbol en 1985, la suela plana y adherente es perfecta para una comunidad deportiva desatendida: los skaters. Al revelar una subcultura que anhela la creatividad tanto como la funcionalidad, el Dunk lanzó décadas de incontables gamas de colores que continúan capturando el alma de los skaters de costa a costa."
    precioZapatilla = 109990

    contexto = {
        "dato1" : nombreZapatilla,
        "dato2" : marcaZapatilla,
        "dato3" : descripcion,
        "dato4" : precioZapatilla
    }    
    return render(request, 'core/detailsgirl1.html', contexto)
    
def detailsgirl2(request):
    return render(request, 'core/detailsgirl2.html')
    
def detailsgirl3(request):
    return render(request, 'core/detailsgirl3.html')
    
def detailsgirl4(request):
    return render(request, 'core/detailsgirl4.html')
    
def detailsgirl5(request):
    return render(request, 'core/detailsgirl5.html')
    
def detailsgirl6(request):
    return render(request, 'core/detailsgirl6.html')

def ingresar_datos(request):
    if request.method == 'POST':
        form = DatosCompraForm(request.POST)
        if form.is_valid():
            # Aquí puedes procesar los datos de la compra, como guardarlos en la base de datos o enviar un correo electrónico de confirmación.
            return redirect('confirmar_pago')
    else:
        form = DatosCompraForm()
    return render(request, 'core/ingresar_datos.html', {'form': form})
  
def confirmar_pago(request):
    return render(request, 'core/confirmar_pago.html')

def detailsmen1(request, pk):
    zapatilla = get_object_or_404(Zapatilla, pk=pk)
    return render(request, 'core/detailsmen1.html', {'zapatilla': zapatilla})
    
def detailsmen2(request):
    return render(request, 'core/detailsmen2.html')

def detailsmen3(request):
    return render(request, 'core/detailsmen3.html')

def detailsmen4(request):
    return render(request, 'core/detailsmen4.html')

def detailsmen5(request):
    return render(request, 'core/detailsmen5.html')

def detailsmen6(request):
    return render(request, 'core/detailsmen6.html')
 
def detailsninos1(request):
    return render(request, 'core/detailsninos1.html')    

def detailsninos2(request):
    return render(request, 'core/detailsninos2.html')

def detailsninos3(request):
    return render(request, 'core/detailsninos3.html')

def detailsninos4(request):
    return render(request, 'core/detailsninos4.html')

def detailsninos5(request):
    return render(request, 'core/detailsninos5.html')

def detailsninos6(request):
    return render(request, 'core/detailsninos6.html')

@login_required
def hombre(request):
    zapatilla = Zapatilla.objects.filter(tipo = "Hombre")
    contexto = {
        "zapatillas" : zapatilla,
    }
    return render(request, 'core/hombre.html', contexto)

def carrito(request):
    carrito = []
    total_compra = 0
    if 'carrito' in request.session:
        carrito_ids = request.session['carrito']
        carrito = Zapatilla.objects.filter(id_producto__in=carrito_ids)
        total_compra = sum(zapatilla.precio * zapatilla.cantidad for zapatilla in carrito)
    return render(request, 'core/carrito.html', {'carrito': carrito, 'total_compra': total_compra})

def agregar_a_carrito(request, id_producto):
    if 'carrito' not in request.session:
        request.session['carrito'] = []
    carrito_ids = request.session['carrito']
    carrito_ids.append(id_producto)
    request.session['carrito'] = carrito_ids
    request.session.modified = True
    
    messages.add_message(request, messages.SUCCESS, 'Se añadió al carrito')
    return redirect('carrito')

def aumentar_cantidad(request, id_producto):
    if 'carrito' in request.session:
        carrito_ids = request.session['carrito']
        if id_producto in carrito_ids:
            producto = get_object_or_404(Zapatilla, id_producto=id_producto)
            producto.cantidad += 1
            producto.save()
    return redirect('carrito')

def disminuir_cantidad(request, id_producto):
    if 'carrito' in request.session:
        carrito_ids = request.session['carrito']
        if id_producto in carrito_ids:
            producto = get_object_or_404(Zapatilla, id_producto=id_producto)
            if producto.cantidad > 1:
                producto.cantidad -= 1
                producto.save()
            else:
                carrito_ids.remove(id_producto)
                request.session['carrito'] = carrito_ids
    return redirect('carrito')

def eliminar_zapatilla(request, id_producto):
    if 'carrito' in request.session:
        carrito_ids = request.session['carrito']
        if id_producto in carrito_ids:
            carrito_ids.remove(id_producto)
            request.session['carrito'] = carrito_ids
    return redirect('carrito')


def hombreadmin(request):
    return render(request, 'core/hombreadmin.html')

@login_required
def iniciobloodshop(request):
    return render(request, 'core/iniciobloodshop.html')
    
def iniciobloodshopadmin(request):
    return render(request, 'core/iniciobloodshopadmin.html')

@login_required   
def mujer(request):
    zapatilla = Zapatilla.objects.filter(tipo = "Mujer")
    contexto = {
        "zapatillas" : zapatilla
    }
    return render(request, 'core/mujer.html', contexto)
        
def mujeradmin(request):
    return render(request, 'core/mujeradmin.html')


def inicio(request):
    if request.method == 'POST':
        emailUser = request.POST['email']
        claveUser = request.POST['clave']
        
        user = authenticate(request, username=emailUser, password=claveUser)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Iniciaste sesión con exito!!")
            return render(request, "core/iniciobloodshop.html")
        else:
            messages.error(request, "Email o Contraseña incorrecta!")
            return redirect('inicio')
    return render(request, 'core/inicio.html')

@login_required
def ninos(request):
    return render(request, 'core/ninos.html')
    
def ninosadmin(request):
    return render(request, 'core/ninosadmin.html')


def lista_zapatillas(request):
    listaZapatilla = Zapatilla.objects.all()
    contexto = {
        "listasZapatillas": listaZapatilla,
    }
    return render(request,'core/lista_zapatillas.html',contexto)

def adminshoes(request):
    zapatillaListado = Zapatilla.objects.all()
    arregloZapatillas = Marca.objects.all()
    contexto = {
        "marcas": arregloZapatillas,
        "zapatillas": zapatillaListado
    }    
    return render(request, 'core/adminshoes.html', contexto)

def editarshoes(request,idzap):
    zapatilla = Zapatilla.objects.get(id_producto = idzap)
    Marcas = Marca.objects.all()
    contexto = {
        "datos": zapatilla,
        "listaMarcas": Marcas
    }
    return render(request,'core/editarshoes.html', contexto)

def ingresarzapatilla(request):
        foto = request.FILES['imgzap']
        idZ     = request.POST['idzap']
        nombre = request.POST['nombrezap']
        tipoz = request.POST['tipo']
        marca = request.POST['marca']
        descripcion = request.POST['desczap']
        talla2 = request.POST['tallazap']
        cantidad2 = request.POST['cantidadzap']
        precio = request.POST['preciozap']

        marcaZapatilla = Marca.objects.get(codigoMarca = marca)

        zapatilla = Zapatilla.objects.create(
            id_producto = idZ, nombreproduct = nombre, tipo = tipoz, marcaproduct = marcaZapatilla, descripcion = descripcion, talla = talla2, cantidad = cantidad2, foto = foto , precio = precio)
        messages.add_message(request, messages.SUCCESS, 'El registro se ha guardado correctamente.')
        return redirect('adminshoes')

def eliminarZap(request, idzap):
    zapatillaEliminar = Zapatilla.objects.get(id_producto = idzap)
    zapatillaEliminar.delete()

    messages.add_message(request, messages.SUCCESS, 'El registro se ha eliminado correctamente.')
    return redirect('lista_zapatillas')

@login_required
def editarperfil(request):
    user = request.user
    usuario = Usuario.objects.get(email=user.username)
    context = {
        'usuario': usuario
    }
    
    return render(request, 'core/editarperfil.html', context)

def mi_vista(request):
    ruta_archivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'core/js/validacionesregistro.js')
    with open(ruta_archivo, 'r') as archivo_js:
        contenido_js = archivo_js.read()
    
    return render(request, 'register.html', {'contenido_js': contenido_js})

@login_required
def actualizarperfil(request):
    user = request.user
    usuario = Usuario.objects.get(email=user.username)

    if request.method == "POST":
        nombreUser = request.POST['nombreS']
        apellidoUser = request.POST['apellido']
        emailUser = request.POST['email']
        fechaUser = request.POST['fechnac']
        telefonoUser = request.POST['telefono']
        
        usuario.nombre = nombreUser
        usuario.apellido = apellidoUser
        usuario.email = emailUser
        usuario.fecha_nacimiento = fechaUser
        usuario.telefono = telefonoUser
        usuario.save()
        
        user.first_name = nombreUser
        user.last_name = apellidoUser
        user.email = emailUser
        user.save()
        
        messages.add_message(request, messages.SUCCESS, 'Los datos se han guardado correctamente.')
        return redirect('editarperfil')

    context = {
        'usuario': usuario
    }

    return render(request, 'editarperfil.html', context)
    

def actualizarZapatilla(request):
    idS     = request.POST['idzap']
    tipoz2     = request.POST['tipo']
    nombreS = request.POST['nombrezap']
    marcaS = request.POST['marcaS']
    descripcionS = request.POST['desczap']
    tallaS = request.POST['tallazap']
    cantidadS = request.POST['cantidadzap']
    precioS = request.POST['preciozap']
    fotoS = request.FILES['imgzap']

    zapatilla = Zapatilla.objects.get(id_producto = idS)
    zapatilla.nombreproduct = nombreS

    marcaZapatilla = Marca.objects.get(codigoMarca = marcaS)
    zapatilla.tipo = tipoz2
    zapatilla.foto = fotoS
    zapatilla.marcaproduct = marcaZapatilla
    zapatilla.descripcion = descripcionS
    zapatilla.talla = tallaS 
    zapatilla.cantidad = cantidadS
    zapatilla.precio = precioS
    zapatilla.save()   
    return redirect('lista_zapatillas')

def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')