
#!/usr/bin/python
# -*- coding: utf-8 -*-

import hug
import json
import sys
from principal import *


template_engine = Environment(loader=FileSystemLoader("templates"))
def get_template(name):
    return template_engine.get_template(name)

@hug.cli()
@hug.local()
@hug.get('/')
def getEstado():
    salida = {"status": "OK"}
    return salida

@hug.get('/status')
def getStatus():
    status = {"status:": "OK",
              "noticias" :
              {
               "ruta": "/noticias",
               "valor": "HTML: devuelto"

              }
            }
    return status

@hug.cli()
@hug.get('/noticias',output=hug.output_format.html)
def inicio():
    template = get_template("index.html")

    noticia = Noticia() #diccionario
    articulo = Articulo()
    tam = noticia.num_noticias()
    dic_noti ={}
    lista_noti =[]

    for i in range(tam):

        lista_noti.append(noticia.get_titulo(i))
        lista_noti.append(noticia.get_descrip(i))
        lista_noti.append(noticia.get_url(i))
        lista_noti.append(noticia.get_publicado(i))

    return template.render(dic_noti=lista_noti)

if __name__ == '__main__':
    inicio()
