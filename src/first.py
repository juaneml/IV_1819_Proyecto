#!/usr/bin/python
# -*- coding: utf-8 -*-

# first.py

import urllib.request, json
import requests
import os


""" Clase Noticia para el microservicio
    Tiene los atributos titulo, descrip, url y published
    Para la clase Noticia optenemos los datos a través de la api del periódico El Mundo
    y almaceno los datos en un fichero que llamo datos.json
"""
class Noticia:
    titulo = []
    descrip =[]
    url = []
    published = []
    noticias = []
    num_noti = 0

    def __init__(self):
        self.titulo = []
        self.descrip = []
        self.url = []
        self.published = []
        self.num_noti
        with open('../json/datos_m.json','r') as noti:
                self.noticias = json.load(noti)#json.loads(open('../json/datos_m.json').read())
        self.Crea_noticia()
        self.num_noticias()

    def get_lista(self):
        return self.noticias

    """      Título     """

    """Devuelve el título de la noticia """
    def get_titulo(self,string):
        return self.titulo[string]

    """Cambia el título de la noticia"""
    def set_titulo(self,string):
        self.titulo = string

    """Añade el titulo a de la noticias """
    def add_titulo(self,string):
        self.titulo.append(string)

    """     Descripción     """

    """Devuelve la descripción de la noticia """
    def get_descrip(self,des):
        return self.descrip[des]

    """Cambia la descripción de la noticia """
    def set_descrip(self,string):
        self.descrip = string

    """Añade la descripción de la noticia """
    def add_descrip(self,string):
        self.descrip.append(string)

    """         Url         """

    """ Devuelve la url de la noticia"""
    def get_url(self,d_url):
        return self.url[d_url]

    """ Cambia la url de la noticia"""
    def set_url(self,string):
        self.url = string

    """ Añade la url de la noticia"""
    def add_url(self,string):
        self.url.append(string)

    """     Fecha publicación       """

    def get_publicado(self,publi):
        return self.published[publi]

    """ Cambia fecha publicado"""
    def set_publicaddo(self,string):
        self.published = string

    """ Añade fecha publicado """
    def add_publicado(self,string):
        self.published.append(string)

    def Crea_noticia(self):
        dic = self.noticias
        cont = 0 # contador noticias
        for i in dic:
            if(i['title'] != None):
                self.add_titulo(i['title'])
            else:
                self.add_titulo("")
            if(i['description']!=None):
                self.add_descrip(i['description'])
            else:
                self.add_descrip("")
            if(i['url'] != None):
                self.add_url(i['url'])
            else:
                self.add_url("")
            if(i['publishedAt']!=None):
                self.add_publicado(i['publishedAt'])
            else:
                self.add_publicado("")
            cont+=1
        self.num_noti = cont

    def num_noticias(self):
        return self.num_noti

"""Clase articulo que hereda de Noticia,  """

class Articulo:
    clase = Noticia()
    num_noti = 0

    def __init__(self):
         self.clase = Noticia()
         self.num_noti
         self.Imprime()
         self.Imprime_noti()

    """ Imprime los datos title,description, url y publishedAt"""

    def Imprime(self):
        tam = self.clase.num_noticias()# len(self.clase.get_titulo())-1 ## número de elementos
        self.Set_numNoti(tam)
        for i in range(tam-1):

            print("\nNoticia: \n")
            print(''.join(self.clase.get_titulo(i)) )
            print(''.join(self.clase.get_descrip(i)))
            print(''.join(self.clase.get_url(i)))
            print(''.join(self.clase.get_publicado(i)))

    def Imprime_noti(self):
        print("\nEl número de articulos son : " + str(self.clase.num_noticias()) )

    def Num_arti(self):
        return self.num_noti

    def Set_numNoti(self,num):
        self.num_noti = num

if __name__ == '__main__':
    Noticia.Crea_noticia(Noticia)
    Articulo.Imprime(Articulo)
    Articulo.Imprime_noti(Articulo)
