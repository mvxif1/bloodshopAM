from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Zapatilla
from .serializers import ZapatillaSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_zapatillas2(request):
    if request.method == 'GET':
       Zapatillas = Zapatilla.objects.all()
       serializer = ZapatillaSerializer(Zapatillas, many=True)
       return Response(serializer.data)
    elif request.method == 'POST':
       data = JSONParser().parse(request)
       serializer = ZapatillaSerializers(data = data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status= status.HTTP_201_CREATED)
       else:
           return Responde(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_zapatilla(request, id):
    try:
        zapatilla = Zapatilla.objects.get(id_producto = id)
    except Zapatilla.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        serializer = ZapatillaSerializer(zapatilla)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ZapatillaSerializer(zapatilla, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        zapatilla.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


