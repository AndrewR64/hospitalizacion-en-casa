from dataclasses import field
from pyexpat import model
from hosp_app.models import PSalud
from hosp_app.models.PSalud import Personal_salud
from rest_framework import serializers

class psaludserializer(serializers.ModelSerializer):

    class Meta:
        model = Personal_salud
        fields = ("UserName","Rol","Especialidad")
