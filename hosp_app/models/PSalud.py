from tkinter import CASCADE
from django.db import models
from .usuario import usuario

class Personal_salud(models.Model):
    id_PersonSalud = models.AutoField(primary_key=True)
    UserName = models.ForeignKey(usuario,related_name='PSalud',on_delete=models.CASCADE)
    Rol = models.CharField("Rol", max_length=30)
    Especialidad = models.CharField("Especialidad", max_length=60)
