from dataclasses import field
from pyexpat import model
from hosp_app.models.usuario import usuario
from rest_framework import serializers

class Usuarioloserserializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ("UserName","contraseña","perfil","nombres","apellido","telefono","genero")
