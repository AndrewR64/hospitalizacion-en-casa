from django.db import models
from.usuario import usuario

class familiar(models.Model):
    id_familiar = models.AutoField(primary_key=True)
    UserName = models.ForeignKey(usuario,related_name="Familiar",on_delete=models.CASCADE)
    parentesco = models.CharField("Parentesco",max_length=30)
    correo = models.CharField("Correo", max_length=30)
    
