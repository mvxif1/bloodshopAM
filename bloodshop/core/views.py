from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario, Venta, Marca, Zapatilla, Carrito
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
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
            return redirect('inicio')
        
        if claveUser != confclaveUser:
            messages.error(request, "La contraseña no coincide!")
            return redirect('register')
        
        if not (nombreUser and apellidoUser and rutUser and fechaUser and telefonoUser and emailUser and claveUser and confemailUser and confclaveUser):
            return JsonResponse({'success': False, 'message': 'Por favor, complete todos los campos.'})

        Usuario.objects.create(rut= rutUser, nombre= nombreUser, apellido= apellidoUser, fecha_nacimiento= fechaUser, telefono= telefonoUser, email= emailUser, contraseña= claveUser)    
        
        user = User.objects.create_user(username = emailUser, password= claveUser, first_name= nombreUser, last_name= apellidoUser, email = emailUser)
        messages.success(request, 'Cuenta creada con exito')
        
        
        return redirect('inicio')  # redirige a la página después del registro exitoso

    return render(request, 'core/register.html')

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
            # messages.success(request, "Logged In Sucessfully!!")
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
    
def olvidepassword(request):
    return render(request, 'core/olvidepassword.html')

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

def editarperfil(request):
    usuario = request.user

    if request.method == 'POST':
        nombre = request.POST('nombre')
        apellido = request.POST('apellido')
        rut = request.POST('rut')
        fechnac = request.POST('fechnac')
        telefono = request.POST('telefono')
        email = request.POST('email')
        contraseña = request.POST('clave')

        # Validar campos
        if not (nombre and apellido and rut and fechnac and telefono and email and contraseña):
            return render(request, 'editarperfil.html', {'usuario': usuario, 'error': 'Todos los campos son requeridos'})

        # Actualizar perfil del usuario
        usuario.usuario.nombre = nombre
        usuario.usuario.apellido = apellido
        usuario.usuario.rut = rut
        usuario.usuario.fecha_nacimiento = fechnac
        usuario.usuario.telefono = telefono
        usuario.email = email
        usuario.set_password(contraseña)

        usuario.save()
        usuario.usuario.save()

        return redirect('inicio')
    return render(request, 'core/editarperfil.html', {'usuario': usuario})

def actualizarperfil(request):
    return redirect('iniciobloodshop')

def actualizarZapatilla(request):
    idS     = request.POST['idzap']
    tipoz2     = request.POST['tipo']
    nombreS = request.POST['nombrezap']
    marcaS = request.POST['marcaS']
    descripcionS = request.POST['desczap']
    tallaS = request.POST['tallazap']
    cantidadS = request.POST['cantidadzap']
    precioS = request.POST['preciozap']

    zapatilla = Zapatilla.objects.get(id_producto = idS)
    zapatilla.nombreproduct = nombreS

    marcaZapatilla = Marca.objects.get(codigoMarca = marcaS)
    zapatilla.tipo = tipoz2
    zapatilla.marcaproduct = marcaZapatilla
    zapatilla.descripcion = descripcionS
    zapatilla.talla = tallaS 
    zapatilla.cantidad = cantidadS
    zapatilla.precio = precioS
    zapatilla.save()   
    return redirect('lista_zapatillas')