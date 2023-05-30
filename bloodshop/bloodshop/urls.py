"""bloodshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import adminshoes, carrito, details, detailsgirl1, detailsgirl3, detailsgirl4, detailsgirl5, detailsgirl6,
detailsmen1, detailsmen2, detailsmen3, detailsmen4, detailsmen5, detailsmen6, detailsninos1, detailsninos2, detailsninos3,
detailsninos4, detailsninos5, detailsninos6, hombre, hombreadmin, inicio, inicioadmin, iniciobloodshop, iniciobloodshopadmin,
mujer, mujeradmin, ninos, ninosadmin, olvidepassword, register

urlpatterns = [
    path('admin/', admin.site.urls),
]
