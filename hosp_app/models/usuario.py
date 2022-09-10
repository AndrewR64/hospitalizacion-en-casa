from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class usuarioManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Los usuarios deben tener nombre de usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


class usuario(AbstractBaseUser, PermissionsMixin):
    UserName = models.CharField(primary_key=True,max_length=15,unique=True)
    contraseña = models.CharField('Contraseña', max_length = 256)
    perfil = models.CharField('Perfil', max_length = 30)
    nombre = models.CharField('Nombre', max_length = 30)
    apellido = models.EmailField('Apellido', max_length = 30)
    telefono = models.CharField("Telefono", max_length=30)
    genero = models.CharField("Genero", max_length=30)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().sav(**kwargs)

object= usuarioManager()
USERNAME_FIELD="usuario"

