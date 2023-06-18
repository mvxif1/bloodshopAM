from django.urls import path
from rest_api import views
from rest_api.viewslogin import login
urlpatterns = [
    path('lista_zapatillas2', views.lista_zapatillas2, name= "lista_zapatillas2"),
    path('detalle_zapatilla/<id>', views.detalle_zapatilla, name="detalle_zapatilla"),
    path('login', login, name="login"),
]