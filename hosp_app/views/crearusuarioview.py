from lib2to3.pgen2 import token
from logging import exception
from urllib import request, response
from rest_framework import status, views
from rest_framework_simplejwt import response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hosp_app import serializers

from hosp_app.serializers.usuarioserializer import Usuarioloserserializer

class Crearusuarioviews(views.APIview):
    def post(self,request,*args, **Kwargs):
        serializer = Usuarioloserserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {
            "username":request.data["username"],
            "password":request.data["password"]
        }

        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)

        return response(tokenSerializer._validate_data,status = status.HTTP_201_CREATED)

