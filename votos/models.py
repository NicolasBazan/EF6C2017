# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.conf import settings
class Distrito(models.Model):
    """
    Se decide utilizar este modelo para la clase distrito porque es
    necesario el nombre y la cantidad de votantes,
    y en un futuro se mostrara un mapa con un marker por cada distrito
    que contenga los resultados del mismo.
    """
    nombre = models.CharField('Nombre del distrito', max_length=128)
    cantidad_votantes = models.IntegerField('Cantidad de votantes', default=0)
    latitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)
    longitude = models.DecimalField('Latitud', max_digits=14, decimal_places=10, default=0)


    def __str__(self):
        return 'Distrito {}'.format(self.nombre)

class Candidato(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase
    """
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    districto = models.ForeignKey(Distrito)
    'Necesito saber los datos del candidato, tanto el nombre como el apellido. Por otro lado necesito saber que de districto es cada candidato'

class Votos(models.Model):
    """
    #TODO Completar segun consideraciones del desarrollador
    En este comentario escribir por que se decide modelar de esta
    forma la clase
    """
    candidato = models.ForeignKey(Candidato, null=True)
    'Necesto saber de que candidato son los votos'
    
