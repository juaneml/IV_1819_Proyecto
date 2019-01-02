import hug
import sys
import datetime
sys.path.append('../src/')

from principal import *

with open('../json/datos_m.json','r') as noti:
        lista_noticias = json.load(noti)

newgroups = Newsgroups()
newgroups.Crea_news(lista_noticias)
num_groups = newgroups.getNumNot()

@hug.get()
def get_dato(i):

    dic = newgroups.getNoticia().to_s(i)
    return dic

@hug.get()
def get_varias(num):

    lista = []

    if(num > num_groups):
        return {"Número no permitido, debe ser como máximo " : num_groups}
    else:
        for i in range(num):
            lista.append("Noticia")
            lista.append(newgroups.getNoticia().to_s(i))
    return lista

@hug.get()
def get_all():
    lista = []
    for i in range(num_groups):
        lista.append("Noticia")
        lista.append(newgroups.getNoticia().to_s(i))

    return lista

@hug.get()
def busca(dato):
    resultado = newgroups.busca_not(dato)

    if(resultado > -1):
        return {"Salida":{ "Exito": newgroups.getNoticia().to_s(resultado)}}
    return resultado


@hug.get()
def add_comen(titulo,comentario):
    resultado = newgroups.getNoticia().add_coment(comentario)

    if (resultado == True):
        newgroups.Set_news(lista_noticias,titulo,comentario)

        return {"Salida" : {"Comentario añadido":{"Time" : datetime.datetime.now(), "Noticia" : newgroups.getNoticia().to_s(int(titulo))}}}
    else:
        return {"Salida" : "no ha sido añadido ningun comentario"}
