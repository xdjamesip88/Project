from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    descripcion = models.CharField(max_length=100, default='',blank=True)
    local = models.CharField(max_length=100, default='')
    dni = models.IntegerField()
    fechaInicio = models.DateField()
    fechaFin    = models.DateField(blank=True, null=True)
    celular = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.user)

class producto(models.Model):

    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()

    def __str__(self):
        return self.nombre


class cuenta(models.Model):
    usuario = models.ForeignKey(UserProfile)
    fecha = models.DateField()
    internet = models.FloatField()
    golosinas = models.FloatField()
    gastos = models.FloatField()
    totalentrega = models.FloatField(verbose_name="Total Entregado")
    obs = models.CharField(max_length=300)

    class Meta:
        unique_together = ('usuario', 'fecha',)

    def __str__(self):
        return str(self.usuario) +" " + str(self.fecha)

# class stock(models.Model):
#     cuenta = models.ForeignKey(cuenta)
#     usuario = models.ForeignKey(UserProfile, default=None)
#     fecha = models.DateField(default=None)
#     bloquear = models.BooleanField(default=False)
#
#
#     class Meta:
#         unique_together = ('usuario', 'fecha',)
#
#     def __str__(self):
#         return str(self.usuario) +" " + str(self.fecha)

class stockdetalle(models.Model):
    cuenta  = models.ForeignKey(cuenta)
    producto = models.ForeignKey(producto)
    cantidad = models.IntegerField()
    vendidos = models.IntegerField()
    restante = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return str(self.producto)+" "+str(self.cuenta.usuario) +" "+str(self.cuenta.fecha)

