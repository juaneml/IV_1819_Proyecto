#!/usr/bin/env python
# -*- coding: utf-8 -*-
# first.py


import json
import os


""" Clase Noticia para el microservicio
    Tiene los atributos titulo, descrip, url y published
    Para la clase Noticia optenemos los datos a traves de la api del periodico El Mundo
    y almaceno los datos en un fichero que llamo datos.json y datos_m.json
"""

class Noticia:
    titulo = []
    descrip =[]
    url = []
    published = []
    num_noti = 0

    def __init__(self):
        self.titulo = []
        self.descrip = []
        self.url = []
        self.published = []
        self.num_noti


    """   ***  Título  ***   """

    """Devuelve el titulo de la noticia """
    def get_titulo(self,string):
        try:
            return self.titulo[string]
        except:
            return False

    """Cambia el titulo de la noticia"""
    def set_titulo(self,string):

        if (type(string) != int):
            self.titulo = string
            return True
        else:
            return False

    """Add el titulo a las noticias """
    def add_titulo(self,string):

        if (type(string) != int):
            self.titulo.append(string)
            return True
        else:
            return False

    """  ***  Descripción  ***   """

    """Devuelve la descripcion de la noticia """
    def get_descrip(self,des):
        try:
            return self.descrip[des]
        except:
            return False

    """Cambia la descripcion de la noticia """
    def set_descrip(self,string):

        if(type(string)!= int):
            self.descrip = string
            return True
        else:
            return False

    """Add la descripcion de la noticia """
    def add_descrip(self,string):

        if(type(string) != int):
            self.descrip.append(string)
            return True
        else:
            return False

    """    ***    Url  ****       """

    """ Devuelve la url de la noticia"""
    def get_url(self,d_url):
        try:
            return self.url[d_url]
        except:
            return False

    """ Cambia la url de la noticia"""
    def set_url(self,string):

        if(type(strin) != int):
            self.url = string
            return True
        else:
            return False

    """ Add la url de la noticia"""
    def add_url(self,string):

        if(type(string)!= int):
            self.url.append(string)
            return True
        else:
            return False

    """   ***  Fecha publicacion  ***    """

    """  get fecha publicación"""
    def get_publicado(self,publi):
        try:
            return self.published[publi]
        except:
            return False

    """ Cambia fecha publicado"""
    def set_publicaddo(self,string):
        if(type(string)!= int):
            self.published = string
            return True
        else:
            return False

    """ Add fecha publicado """
    def add_publicado(self,string):
        if(type(string)!= int):
            self.published.append(string)
            return True
        else:
            return False


    """ Imprime la noticia """
    def to_s(self,i):
        tam = self.num_noti
        print(''.join(self.get_titulo(i)),''.join(self.get_descrip(i)),
        ''.join(self.get_url(i)),''.join(self.get_publicado(i)))


"""Clase Newsgroups, clase que crea varias noticias """
class Newsgroups():
    noticia = Noticia()

    def __init__(self):
        self.lista_noticias =[]
        self.noticia
        self.cont = 0

    """Crea una noticia y se añade a la lista de noticicas """

    def Crea_news(self,lista):
        dic = lista
        self.cont = 0 # contador noticias

        for i in dic:
            if(i['title'] != None):
                self.lista_noticias.append(self.noticia.add_titulo(i['title']))
            else:
                self.lista_noticias.append(self.noticia.add_titulo(" "))
            if(i['description']!=None):
                self.lista_noticias.append(self.noticia.add_descrip(i['description']))
            else:
                self.lista_noticias.append(self.noticia.add_descrip(" "))
            if(i['url'] != None):
                self.lista_noticias.append(self.noticia.add_url(i['url']))
            else:
                self.lista_noticias.append(self.noticia.add_url( ""))
            if(i['publishedAt']!=None):
                self.lista_noticias.append(self.noticia.add_publicado(i['publishedAt']))
            else:
                self.lista_noticias.append(self.noticia.add_publicado(" "))
            self.cont+=1

    """ Devuelve la noticia """

    def getNoticia(self):
        return self.noticia

    """ Devuelve el número de noticias """

    def getNumNot(self):
        return self.cont


if __name__=='__main__':
    with open('../json/datos_m.json','r') as noti:
            lista_noticias = json.load(noti)

    titular = Newsgroups()
    titular.Crea_news(lista_noticias)
    num_titular = titular.getNumTit()


    for i in range(num_titular):

        print("***********  NOTICIA  *************")
        titular.getNoticia().to_s(i)
        print("******************************","\n")

    print("Numero de Noticias "," ",titular.getNumTit() )
