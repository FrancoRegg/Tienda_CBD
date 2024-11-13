from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def productos(request):
    if request.method == 'GET':
        return Response ({'message':'PRODUCTOS'})

