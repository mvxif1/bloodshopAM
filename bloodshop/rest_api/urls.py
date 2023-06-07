from django.urls import path
from rest_api.views import lista_zapatillas

urlpatterns = [
    path('lista_zapatillas2', lista_zapatillas, name= "lista_zapatillas2"),
]