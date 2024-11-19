from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Address
from .serializers import AddressSerializer, UsersSerializer

#USUARIOS
@api_view(['GET'])
def get_users(request):
    if request.method == "GET":
        users = User.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return Response(users_serializer.data)

#USUARIO POR ID
@api_view(['GET'])
def get_user_id(request, pk):
    if request.method == "GET":

        user = User.objects.filter(id=pk).first()
        user_serializer = UsersSerializer(user)
        return Response(user_serializer.data)

#CREAR USUARIO
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':

        user_serializer = UsersSerializer(data = request.data)
        print(request.data, "DATA")
        if user_serializer.is_valid():
            user_serializer.save()
            
            return Response(user_serializer.data)
        return Response(user_serializer.errors)