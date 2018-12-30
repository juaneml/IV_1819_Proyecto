#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hug
import json


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

@hug.get('/una_noticia')
def una(noticia: hug.types.text,lugar: hug.types.text):

    return {"Noticia":noticia,"lugar":lugar}
if __name__ == '__main__':
    una.interface.cli()
