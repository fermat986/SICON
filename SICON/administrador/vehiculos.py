from django.db import models
from .sucursal import Sucursal
from .repuesto import Marca

class Vehiculo(models.Model):

    cilindraje = models.IntegerField()
    marca = models.ForeignKey(Marca,blank=True)
    linea = models.CharField(max_length=50)
    modelo = models.IntegerField()
    #TIPOS DE COMBUSTIBLE
    GASOLINA='Gasolina'
    GAS= 'Gas'
    COMB_CHOICES = ((GASOLINA, 'Gasolina'), (GAS, 'Gas'))
    tipo_combustible = models.CharField(choices=COMB_CHOICES, max_length=50)
    color = models.CharField(max_length=50)
    sucursal = models.ForeignKey(Sucursal, null=True)
    activo = models.BooleanField(default=True)
    def __str__(self):
        return self.linea

class VehiculoNuevo(Vehiculo):

    valor = models.IntegerField()
    codigo = models.CharField(max_length=10)
    vendido = models.BooleanField(default=False)
    fecha_ingreso = models.DateField(null=True,blank=True)
    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("listar_Vehiculo_Nuevo",       "Se permite editar, activar , desactivar" ),
        )
    def __str__(self):
        return self.codigo

class VehiculoUsado(Vehiculo):


    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("listar_Vehiculo_Usado",       "Se permite editar, activar , desactivar" ),
        )
    #TIPOS DE SERVICIO
    PUBLICO= 'Publico'
    PRIVADO= 'Prviado'
    SERVICIO_CHOICES = ((PUBLICO,'Publico'), (PRIVADO,'Privado'))
    servicio = models.CharField(choices= SERVICIO_CHOICES, max_length=50)
    placa = models.CharField(max_length=6,unique=True)
    def __str__(self):
        return self.placa
