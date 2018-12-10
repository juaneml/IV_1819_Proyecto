#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hug
import json
import sys
#sys.path.append('../src/')
from principal import *


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
if __name__ == '__main__':
    add.interface.cli()
