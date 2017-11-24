# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from votos.models import *


def resultado_global(request):
    """
    Generar la vista para devolver el resultado global de la elección.
    Tener en cuenta que tiene que tener:
    Cantidad total de votos por candidato
    Cantidad total de votos nulos
    Porcentaje de cada candidato
    Porcentaje de votos nulos
    Total de votos de la elección
    """
    context={}
    context['distritos'] = Distrito.objects.all()
    #TODO TU CODIGO AQUI
    candidatos= Candidato.objects.get(id)
    total_votos_candidatos = Votos.objects.filter(candidato= candidato)
    # porcentaje_candidato = (total_votos_candidatos/total_votos_eleccion)
    votos_nulos= Votos.objects.filter(candidato__isnull=True).count()
    total_votos_eleccion = Votos.objects.all().count()
    porcentaje_votos_nulos= (votos_nulos/total_votos_eleccion)
    return render(request,'global.html',context)


def resultado_distrital(request, id):
    """
    Generar la vista para devolver el resultado distrital de la elección
    Tener en cuenta que tiene que tener:
    Tamaño del padrón
    Porcentaje de votos del distrito (respecto al padron. Ejemplo: Si el distrito tiene 1000 votantes y hay 750 votos, el porcentaje es 75%)
    Total de votos del distrito
    Candidato ganador
    """
    context={}
    districtos = Distrito.objects.all()
    #TODO TU CODIGO 
    padron_districto = Distrito.objects.filter(id=id)
    for padron in padron_districto:
        tamanio_padron= padron.cantidad_votantes
    total_votantes = Votos.objects.filter(candidato__districto__id=id).count()
    porcentaje_votantes= (total_votantes/tamanio_padron)
    return render(request,'distrital.html',context,{'districtos':districtos})
