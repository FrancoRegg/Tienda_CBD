from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Address
from .serializers import AddressSerializer, UsersSerializer

#CREAR USUARIO
@api_view(['POST'])
def create_user(request):

    user_serializer = UsersSerializer(data = request.data)
    print(request.data, "DATA")
    if user_serializer.is_valid():
        user_serializer.save()
        
        return Response(user_serializer.data)
    return Response(user_serializer.errors)

#USUARIOS
@api_view(['GET'])
def get_users(request):
    
    users = User.objects.all()
    users_serializer = UsersSerializer(users, many=True)
    return Response(users_serializer.data)

#USUARIO POR ID
@api_view(['GET'])
def get_user_id(request, pk):
    user = User.objects.filter(id=pk).first()
    
    if not user.is_active:
        return Response({"message":"non-existent user"}, status=status.HTTP_404_NOT_FOUND)
    
    user_serializer = UsersSerializer(user)
    return Response(user_serializer.data)

#ACTUALIZAR DATOS DE USUARIO
@api_view(['PUT'])
def update_user(request, pk):
    user = User.objects.filter(id=pk).first()
    user_serializer = UsersSerializer(user, data=request.data)
    if  user_serializer.is_valid():
        user_serializer.save()
        
        return Response(user_serializer.data)
    
    return Response(user_serializer.errors)

#ACTUALIZAR SOLO CONTRASEÑA DE USUARIO

#RECUPERAR CONTRASEÑA DE USUARIO

#ELIMINAR USUARIO
@api_view(['DELETE'])
def delete_user(request, pk):
    user = User.objects.filter(id=pk).first()
    if user is None:
        return Response({"message":"User not found"}, status=status.HTTP_404_NOT_FOUND)
        
    if not user.is_active:
        return Response({"message":"User is deleted"}, status=status.HTTP_400_BAD_REQUEST)
    
    user.is_active = False
    user.save()
    return Response({"message":"User successfully deleted"}, status=status.HTTP_200_OK)

#######

#CREAR DIRECCION PARA USUARIO

#MOSTRAR DIRECCION DE USUARIO

#ACTUALIZAR DIRECCION