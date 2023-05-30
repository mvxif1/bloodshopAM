from django.contrib import admin
from django.urls import path, include
from.views import home, iniciobloodshop, carrito,detailsgirl1, detailsgirl2, detailsgirl3,detailsgirl4,detailsgirl5,detailsgirl6,detailsmen1,detailsmen2,detailsmen3,detailsmen4,detailsmen5,detailsmen6,detailsninos1,detailsninos2,detailsninos3,detailsninos4,detailsninos5,detailsninos6,details,hombreadmin,hombre,inicioadmin,iniciobloodshopadmin, inicio, mujeradmin, mujer, ninosadmin,ninos, olvidepassword, pantallaprincadmin, register



urlpatterns = [
      
    path('', iniciobloodshop, name="home"),
    
    path('carrito', carrito, name="carrito"),


    path('detailsgirl1', detailsgirl1, name="detailsgirl1"),
    path('detailsgirl2', detailsgirl2, name="detailsgirl2"),
    path('detailsgirl3', detailsgirl3, name="detailsgirl3"),
    path('detailsgirl4', detailsgirl4, name="detailsgirl4"),
    path('detailsgirl5', detailsgirl5, name="detailsgirl5"),
    path('detailsgirl6', detailsgirl6, name="detailsgirl6"),
    
    
    path('detailsmen1', detailsmen1, name="detailsmen1"),
    path('detailsmen2', detailsmen2, name="detailsmen2"),
    path('detailsmen3', detailsmen3, name="detailsmen3"),
    path('detailsmen4', detailsmen4, name="detailsmen4"),
    path('detailsmen5', detailsmen5, name="detailsmen5"),
    path('detailsmen6', detailsmen6, name="detailsmen6"),
   
    
    
    
    path('detailsninos1', detailsninos1, name="detailsninos1"),
    path('detailsninos2', detailsninos2, name="detailsninos2"),
    path('detailsninos3', detailsninos3, name="detailsninos3"),
    path('detailsninos4', detailsninos4, name="detailsninos4"),
    path('detailsninos5', detailsninos5, name="detailsninos5"),
    path('detailsninos6', detailsninos6, name="detailsninos6"),

    
    
    path('details', details, name="details"),



    path('hombre-admin', hombreadmin, name="hombreadmin"),

    path('hombre', hombre, name="hombre"),
    path('inicioadmin', inicioadmin, name="inicioadmin"),
    path('iniciobloodshopadmin', iniciobloodshopadmin, name="iniciobloodshopadmin"),
    path('iniciobloodshop', iniciobloodshop, name="iniciobloodshop"),
    path('inicio', inicio, name="inicio"),
    path('mujeradmin', mujeradmin, name="mujeradmin"),
    path('mujer', mujer, name="mujer"),
    path('ninosadmin', ninosadmin, name="ninosadmin"),
    path('ninos', ninos, name="ninos"),
    path('olvidepassword', olvidepassword, name="olvidepassword"),
    path('pantallaprincadmin', pantallaprincadmin, name="pantallaprincadmin"),
    path('register', register, name="register"),
    
]