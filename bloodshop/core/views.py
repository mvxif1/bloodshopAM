from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Venta, Marca, Zapatilla


# Create your views here.
    
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
    
def detailsmen1(request):
    return render(request, 'core/detailsmen1.html')
    
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
    return render(request, 'core/hombre.html')
    
def hombreadmin(request):
    return render(request, 'core/hombreadmin.html')
    
def inicio(request):
    return render(request, 'core/inicio.html')
    
def inicioadmin(request):
    return render(request, 'core/inicioadmin.html')

def iniciobloodshop(request):
    return render(request, 'core/iniciobloodshop.html')
    
def iniciobloodshopadmin(request):
    return render(request, 'core/iniciobloodshopadmin.html')
    
def mujer(request):
    return render(request, 'core/mujer.html')
        
def mujeradmin(request):
    return render(request, 'core/mujeradmin.html')

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
        "signo": "$",
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
        marca = request.POST['marca']
        descripcion = request.POST['desczap']
        precio = request.POST['preciozap']

        marcaZapatilla = Marca.objects.get(codigoMarca = marca)

        zapatilla = Zapatilla.objects.create(
            id_producto = idZ, nombreproduct = nombre, marcaproduct = marcaZapatilla, descripcion = descripcion, foto = foto , precio = precio)
        messages.add_message(request, messages.SUCCESS, 'El registro se ha guardado correctamente.')
        return redirect('adminshoes')

def eliminarZap(request, idzap):
    zapatillaEliminar = Zapatilla.objects.get(id_producto = idzap)
    zapatillaEliminar.delete()

    messages.add_message(request, messages.SUCCESS, 'El registro se ha eliminado correctamente.')
    return redirect('lista_zapatillas')

def actualizarZapatilla(request):
    codigoZap = request.POST['idzap'] 
    nomZap  = request.POST['nombrezap'] 
    marcZap = request.POST['marcaZap'] 
    descripZap = request.POST['desczap'] 
    priceZap = request.POST['preciozap'] 

    zapatilla = Zapatilla.objects.get(id_producto = codigoZap)
    zapatilla.nombreproduct = nomZap

    registroMarca = Marca.objects.get(codigoMarca = marcZap) 
    zapatilla.marcaZap = registroMarca 
    
    zapatilla.descripcion = descripZap 
    zapatilla.precio = priceZap
    messages.add_message(request, messages.SUCCESS, 'El registro se ha actualizado correctamente.')
    return redirect('lista_zapatillas')