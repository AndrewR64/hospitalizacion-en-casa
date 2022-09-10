from lib2to3.pgen2 import token
from logging import exception
from urllib import request, response
from rest_framework import status, views
from rest_framework_simplejwt import response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hosp_app import serializers

from hosp_app.serializers.PSaludserializer import psaludserializer

class Crearpersonalview(views.APIView):
    def post(self,request):
        serializer = psaludserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data,status = status.HTTP_201_CREATED)
        return response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

