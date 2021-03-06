# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import smart_unicode
from .sucursal import Sucursal

__author__ = 'nelson'

class Empleado(models.Model):

    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("listar_Empleados",       "Se permite editar, activar , desactivar" ),
        )

    emp_id = models.AutoField(primary_key=True)
    no_documento = models.CharField(unique=True, max_length=40)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    
    OMAS= 'O+'
    OMENOS= 'O-'
    AMAS= 'A+'
    AMENOS= 'A-'
    BMAS= 'B+'
    BMENOS= 'B-'
    ABMAS= 'AB+'
    ABMENOS= 'AB-'
    TIPO_CHOICES = ((OMAS, 'O+'), (OMENOS, 'O-'), (AMAS, 'A+'), (AMENOS, 'A-'), 
    (BMAS, 'B+'), (BMENOS, 'B-'), (ABMAS, 'AB+'), (ABMENOS, 'AB-'))
    tipo_sangre = models.CharField(choices=TIPO_CHOICES, max_length=20)
    
    experiencia = models.IntegerField()
    
    MANANA= 'Manana'
    TARDE= 'Tarde'
    NOCHE= 'Noche'
    JORNADA_CHOICES = ((MANANA, 'Mañana'), (TARDE, 'Tarde'), (NOCHE, 'Noche'))
    jornada = models.CharField(choices=JORNADA_CHOICES, max_length=15, default='Manana')
    
    fecha_vinculacion = models.DateField(blank=True)
    
    VEND='Vendedor'
    JT='Jefe de taller'
    GER='Gerente'
    MEC='Mecanico'
    CARGO_CHOICES = ((VEND, 'Vendedor'), (JT, 'Jefe de taller'), (GER, 'Gerente'), (MEC,'Mecánico')) 
    cargo = models.CharField(choices= CARGO_CHOICES, max_length=150, null=True, blank=True)
    telefono = models.CharField(max_length=150)
    
    MASC= 'Masculino'
    FEM= 'Femenino'
    GEN_CHOICES = ((MASC, 'Masculino'), (FEM, 'Femenino'))
    genero = models.CharField(choices=GEN_CHOICES, max_length=15)
    
    fecha_nacimiento = models.DateField()
    

    estado_empleado = models.BooleanField(default=True)
    #models.ForeignKey(Departamento)
    sucursal = models.ForeignKey(Sucursal, null=True, blank=True)
    jefe = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return self.nombre+" "+self.apellido
