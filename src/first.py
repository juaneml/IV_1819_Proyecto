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
class Noticia(object):
    def __init__(self):
        self.titulo = []
        self.descrip = []
        self.url = []
        self.published = []


    """      Título     """

    """Devuelve el título de la noticia """
    def get_titulo(self):
        return self.titulo

    """Cambia el título de la noticia"""
    def set_titulo(self,string):
        self.titulo = string

    """Añade el titulo a de la noticias """
    def add_titulo(self,string):
        self.titulo.append(string)

    """     Descripción     """

    """Devuelve la descripción de la noticia """
    def get_descrip(self):
        return self.descrip

    """Cambia la descripción de la noticia """
    def set_descrip(self,string):
        self.descrip = string

    """Añade la descripción de la noticia """
    def add_descrip(self,string):
        self.descrip.append(string)

    """         Url         """

    """ Devuelve la url de la noticia"""
    def get_url(self):
        return self.url

    """ Cambia la url de la noticia"""
    def set_url(self,string):
        self.url = string

    """ Añade la url de la noticia"""
    def add_url(self,string):
        self.url.append(string)

    """     Fecha publicación       """

    def get_publicado(self):
        return self.published

    """ Cambia fecha publicado"""
    def set_publicaddo(self,string):
        self.published = string

    """ Añade fecha publicado """
    def add_publicado(self,string):
        self.published.append(string)

    """ Obtiene los datos de la api y los almacena en un fichero con extensión json """
    def fun():
        with urllib.request.urlopen("https://newsapi.org/v2/top-headlines?sources=el-mundo&apiKey=3daa18d2a35747a4ab8a03b449c7e048") as url:
            data = json.loads(url.read().decode('utf-8'))
        leer = json.loads(open('datos_m.json').read())

        return  leer

"""Clase articulo que hereda de Noticia,  """

class articulo(Noticia):
    clase = Noticia()

    def __init__(self):
         self.clase
         self.num_noti

    """ Imprime los datos title,description, url y publishedAt """
    def Imprime(self):
        dic = self.fun()
        cont = 0 # contador noticias
        for i in dic:
            if(i['title'] != None):
                self.clase.add_titulo(i['title'])
            else:
                self.clase.add_titulo("")
            if(i['description']!=None):
                self.clase.add_descrip(i['description'])
            else:
                self.clase.add_descrip("")
            if(i['url'] != None):
                self.clase.add_url(i['url'])
            else:
                self.clase.add_url("")
            if(i['publishedAt']!=None):
                self.clase.add_publicado(i['publishedAt'])
            else:
                self.clase.add_publicado("")
            cont+=1

        tam = len(self.clase.get_titulo())-1 ## número de elementos

        for i in range(len(dic)-1):

            print("\nNoticia: \n")
            print(''.join(self.clase.get_titulo()[i]))
            print(''.join(self.clase.get_descrip()[i]))
            print(''.join(self.clase.get_url()[i]))
            print(''.join(self.clase.get_publicado()[i]))

        self.num_noti = cont


    def num_noticias(self):
        return self.num_noti

    def Imprime_noti(self):
        print("\nEl número de articulos son : " + str(self.num_noticias(self)) )



if __name__ == '__main__':
    articulo.Imprime(articulo)
    articulo.Imprime_noti(articulo)

