
#!/usr/bin/python
# -*- coding: utf-8 -*-

import hug
import json
import sys
from first import *
import jinja2
from jinja2 import FileSystemLoader, Environment
from jinja2 import Template

salida = {
    "status:" "OK"

}

template_engine = Environment(loader=FileSystemLoader("templates"))
def get_template(name):
    return template_engine.get_template(name)

@hug.cli()
@hug.local()
@hug.get('/')
def getEstado():
    return salida;
@hug.cli()
@hug.get('/inicio',output=hug.output_format.html)
def inicio():
    template = get_template("index.html")

    noticia = Noticia() #diccionario
    articulo = Articulo()
    tam = noticia.num_noticias()
    dic_noti ={}
    lista_noti =[]
    print (type(noticia.get_lista()))
    for i in range(tam):#noticia.get_lista(): #range(tam):

        # dic_noti.setdefault('Titulo_'+str(i),''.join(noticia.get_titulo(i)) )
        # lista_noti.append(dic_noti)
        # dic_noti.setdefault('Descripción_'+str(i),''.join(noticia.get_descrip(i)))
        # lista_noti.append(dic_noti)
        # dic_noti.setdefault('URL_'+str(i),''.join(noticia.get_url(i)))
        # lista_noti.append(dic_noti)
        # dic_noti.setdefault('Fecha_publicación_'+str(i), ''.join(noticia.get_publicado(i)))
        lista_noti.append(noticia.get_titulo(i))
        lista_noti.append(noticia.get_descrip(i))
        lista_noti.append(noticia.get_publicado(i))

    return template.render(dic_noti=lista_noti)

if __name__ == '__main__':
    inicio()
    #hug.API(__name__).http.output_format = hug.output_format.html
