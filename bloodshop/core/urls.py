from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView)
from .views import adminshoes, carrito, details, detailsgirl1, detailsgirl2, detailsgirl3, detailsgirl4, detailsgirl5, detailsgirl6, detailsmen1, detailsmen2, detailsmen3, detailsmen4, detailsmen5, detailsmen6, detailsninos1, detailsninos2, detailsninos3, detailsninos4, detailsninos5, detailsninos6, hombre, hombreadmin, iniciobloodshop, iniciobloodshopadmin, mujer, mujeradmin, ninos, ninosadmin, register, lista_zapatillas, editarshoes, ingresarzapatilla, eliminarZap, actualizarZapatilla, agregar_a_carrito, aumentar_cantidad, disminuir_cantidad, eliminar_zapatilla, inicio, ingresar_datos, confirmar_pago, signout, editarperfil, actualizarperfil, admin_dashboard, activate
from core import views

urlpatterns = [
    path('', iniciobloodshop, name="iniciobloodshop"),
    path('adminshoes/', adminshoes, name="adminshoes"),
    path('carrito/', carrito, name="carrito"),
    path('details/', details, name="details"),
    path('detailsgirl1/', detailsgirl1, name="detailsgirl1"),
    path('detailsgirl2/', detailsgirl2, name="detailsgirl2"),
    path('detailsgirl3/', detailsgirl3, name="detailsgirl3"),
    path('detailsgirl4/', detailsgirl4, name="detailsgirl4"),
    path('detailsgirl5/', detailsgirl5, name="detailsgirl5"),
    path('detailsgirl6/', detailsgirl6, name="detailsgirl6"),
    path('detailsmen1/<int:pk>', detailsmen1, name="detailsmen1"),
    path('detailsmen2/', detailsmen2, name="detailsmen2"),
    path('detailsmen3/', detailsmen3, name="detailsmen3"),
    path('detailsmen4/', detailsmen4, name="detailsmen4"),
    path('detailsmen5/', detailsmen5, name="detailsmen5"),
    path('detailsmen6/', detailsmen6, name="detailsmen6"),
    path('detailsninos1/', detailsninos1, name="detailsninos1"),
    path('detailsninos2/', detailsninos2, name="detailsninos2"),
    path('detailsninos3/', detailsninos3, name="detailsninos3"),
    path('detailsninos4/', detailsninos4, name="detailsninos4"),
    path('detailsninos5/', detailsninos5, name="detailsninos5"),
    path('detailsninos6/', detailsninos6, name="detailsninos6"), 
    path('inicio/', inicio, name="inicio"),  
    path('hombreadmin/', hombreadmin, name="hombreadmin"),
    path('hombre/', hombre, name="hombre"),
    path('confirmar_pago/', confirmar_pago, name="confirmar_pago"),
    path('iniciobloodshopadmin/', iniciobloodshopadmin, name="iniciobloodshopadmin"),
    path('ingresar_datos/', ingresar_datos, name="ingresar_datos"),
    path('lista_zapatillas', lista_zapatillas, name= "lista_zapatillas"),
    path('editarshoes/<int:idzap>', editarshoes, name= "editarshoes"),
    path('editarperfil/', editarperfil, name="editarperfil"),
    path('ingresarzapatilla/', ingresarzapatilla, name= "ingresarzapatilla"),
    path('eliminarZap/<int:idzap>', eliminarZap, name= "eliminarZap"),
    path('actualizarZapatilla', actualizarZapatilla, name= "actualizarZapatilla"),
    path('actualizarperfil', actualizarperfil, name= "actualizarperfil"),
    path('mujeradmin/', mujeradmin, name="mujeradmin"),
    path('mujer/', mujer, name="mujer"),
    path('ninosadmin/', ninosadmin, name="ninosadmin"),
    path('ninos/', ninos, name="ninos"),
    path('register/', register, name="register"),
    path('admin_dashboard/', admin_dashboard, name="admin_dashboard"),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('signout', signout, name='signout'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    

    path('agregar_a_carrito/<int:id_producto>/', agregar_a_carrito, name="agregar_a_carrito"),
    path('aumentar_cantidad/<int:id_producto>/', aumentar_cantidad, name="aumentar_cantidad"),
    path('disminuir_cantidad/<int:id_producto>/', disminuir_cantidad, name="disminuir_cantidad"),
    path('eliminar_zapatilla/<int:id_producto>/', views.eliminar_zapatilla, name="eliminar_zapatilla"),
] 