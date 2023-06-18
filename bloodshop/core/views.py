from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Usuario, Venta, Marca, Zapatilla, Carrito
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        rut = request.POST['rut']
        fechnac = request.POST['fechnac']
        telefono = request.POST['telefono']
        email = request.POST['email']
        clave = request.POST['clave']
        confemail = request.POST['confemail']
        confclave = request.POST['confclave']

        # Realiza las validaciones que necesites aquí
        # ...

        # Crea un nuevo usuario en la base de datos
        usuario = User.objects.create_user(username=rut, password=clave, email=email, first_name=nombre, last_name=apellido)
        
        # Puedes asignar otros atributos personalizados al usuario si lo deseas
        usuario.telefono = telefono
        usuario.fecha_nacimiento = fechnac
        usuario.save()
        
        return redirect('iniciobloodshop')  # redirige a la página después del registro exitoso

    return render(request, 'core/register.html')
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
    
def iniciobloodshop(request):
    return render(request, 'core/iniciobloodshop.html')
    
def iniciobloodshopadmin(request):
    return render(request, 'core/iniciobloodshopadmin.html')
    
def mujer(request):
    zapatilla = Zapatilla.objects.filter(tipo = "Mujer")
    contexto = {
        "zapatillas" : zapatilla
    }
    return render(request, 'core/mujer.html', contexto)
        
def mujeradmin(request):
    return render(request, 'core/mujeradmin.html')

def login(request):
    return render(request, 'core/login.html')

def ninos(request):
    return render(request, 'core/ninos.html')
    
def ninosadmin(request):
    return render(request, 'core/ninosadmin.html')
    
def olvidepassword(request):
    return render(request, 'core/olvidepassword.html')


def register(request):
    return render(request, 'core/register.html')

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

    