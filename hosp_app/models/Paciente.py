from django.db import models
from.usuario import usuario
from.PSalud import Personal_salud

class paciente(models.Model):
    id_Paciente = models.AutoField(primary_key=True)
    UserName = models.ForeignKey(usuario,related_name="PSalud", on_delete=models.CASCADE)
    id_PersonalSalud = models.ForeignKey(Personal_salud,related_name="Paciente",on_delete=models.CASCADE)
    direccion = models.CharField("Direccion",max_length=30)
    ciudad = models.CharField("Ciudad", max_length=30)
    fecha_nacimiento = models.DateField()



