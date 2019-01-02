#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hug
import json



import api_function
import requests

@hug.cli()
@hug.get('/')
def getEstado():
    salida = {"status": "OK"}
    return salida

@hug.get('/status')
def status():
    status = {"status": "OK",
        "noticias":{
        "ruta": "/noticias",
        "valor": "{'Titulo': 'Granada, una ciudad con encanto',json: devuelto} }"
    }
    }
    return status

@hug.get('/noticias')
def noticias():
    noticia = {
        "Noticia":{

        "Titulo": "Granada, una ciudad con encanto",
        "Descrip": "Granada tiene cada vez más visitantes para ver la Alhambra",
        "url": "www.ideal/es_un_ejemplo",
        "publicado": "7/11/2018",
        "json":"devuelto"
        }
    }
    return noticia
api = hug.get(on_invalid=hug.redirect.not_found)

@hug.get('/una_noticia')
def una(i: hug.types.number):

    salida = api_function.get_dato(i)
    return str(salida)

@hug.get('/varias_noticias')
def varias(num: hug.types.number):

    salida = api_function.get_varias(num)
    return str(salida)

# @hug.format.content_type('../json/datos_m.json')
@hug.get()
def all():

    salida = api_function.get_all()

    return salida

@hug.get()
def busca(dato):
    salida = api_function.busca(dato)

    return salida

@hug.post()
def method_post():
    salida={'publicacion': 'noticia'}
    return salida

@hug.put()
def method_put(noticia,anterior,nuevo):
    salida = {"Noticia": noticia ,"Modificado el Título...": anterior, "Nuevo título": nuevo}
    return salida

@hug.get()
def sustituir_dato(i: hug.types.number,new: hug.types.text):
    salida = api_function.get_dato(i)

    salida = str(method_put(salida,salida['Titulo'],new))
    return str(salida)

@hug.get()
def comment(titulo,comentario):
    salida = api_function.add_comen(titulo,comentario)
    return salida


if __name__ == '__main__':

    una.interface.cli()
    all.interface.cli()
