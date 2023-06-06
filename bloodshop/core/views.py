from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import Usuario, Venta, Marca, Zapatilla


# Create your views here.

def adminshoes(request):
    return render(request, 'core/adminhoes.html')
    
def carrito(request):
    return render(request, 'core/carrito.html')
    
def details(request):
    return render(request, 'core/details.html')
    
def detailsgirl1(request):
    return render(request, 'core/detailsgirl1.html')
    
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
    listaMascota = Mascota.objects.all()
    contexto = {
        "listaZap": listaMascota
    }
    return render(request,'core/lista_zapatillas',contexto)

def adminshoes(request):
    arregloZap = Marca.objects.all()
    contexto = {
        "marcas": arregloZap
    }
    return render(request, 'core/adminshoes.html')

def editarshoes(request,idzap):
    zapatilla = Zapatilla.objects.get(id_producto = idzap)
    marcas = Marca.objects.all()
    contexto = {
        "datos": zapatilla,
        "listaMarcas": marcas
    }
    return render(request,'core/editarshoes.html', contexto)

def ingresarzapatilla(request):
    idZ     = request.POST['idzap']
    nombreZ = request.POST['nombrezap']
    marcaZ = request.POST['marcazap']
    descZ = request.POST['desczap']
    fotoZ = request.FILES['imgzap']
    precioZ = request.POST['preciozap']

    marcaZapatilla = Zapatilla.object.get(codigo = marcaZ)

    Zapatilla.objects.create(id_producto= idZ, nombreproduct= nombrezap, marcaproduct= marcazap, descripcion= desczap, foto= imgzap , precio= preciozap)
    return redirect('agregarzapatilla')

def eliminarZap(request, idzap):
    zapatilla = Zapatilla.objects.get(id_producto = idzap)
    zapatilla.delete()

    return redirect('lista_zapatilla')

def actualizarZapatilla(request):
    codigoZap     = request.POST['idzap']
    nomZap  = request.POST['nombrezap']
    marcZap = request.POST['marcazap']
    descripZap = request.POST['desczap']
    priceZap = request.POST['preciozap']

    zapatilla = Zapatilla.objects.get(id_producto = codigoZap)
    zapatilla.nombreproduct = nomZap
    
    registroMarca = marcaproduct.objects.get(codigoMarca = marcZap)
    zapatilla.marcazap = registroMarca

    zapatilla.descripcion = desczap
    zapatilla.precio = priceZap

    zapatilla.save()
    return redirect('core/lista_zapatillas')