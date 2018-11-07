#!/usr/bin/python
# -*- coding: utf-8 -*-

# first.py


import json
import os


""" Clase Noticia para el microservicio
    Tiene los atributos titulo, descrip, url y published
    Para la clase Noticia optenemos los datos a través de la api del periódico El Mundo
    y almaceno los datos en un fichero que llamo datos.json y datos_m.json
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
                self.noticias = json.load(noti)
        self.Crea_noticia()
        self.num_noticias()

    """ Devuelve la lista de noticas """

    def get_lista(self):
        return self.noticias

    """      Título     """

    """Devuelve el título de la noticia """
    def get_titulo(self,string):
        try:
            return self.titulo[string]
        except:
            return False

    """Cambia el título de la noticia"""
    def set_titulo(self,string):

        if (type(string) != int):
            self.titulo = string
            return True
        else:
            return False

    """Añade el titulo a de la noticias """
    def add_titulo(self,string):

        if (type(string) != int):
            self.titulo.append(string)
            return True
        else:
            return False

    """     Descripción     """

    """Devuelve la descripción de la noticia """
    def get_descrip(self,des):
        try:
            return self.descrip[des]
        except:
            return False

    """Cambia la descripción de la noticia """
    def set_descrip(self,string):

        if(type(string)!= int):
            self.descrip = string
            return True
        else:
            return False

    """Añade la descripción de la noticia """
    def add_descrip(self,string):

        if(type(string) != int):
            self.descrip.append(string)
            return True
        else:
            return False

    """         Url         """

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

    """ Añade la url de la noticia"""

    def add_url(self,string):

        if(type(string)!= int):
            self.url.append(string)
            return True
        else:
            return False

    """     Fecha publicación       """

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

    """ Añade fecha publicado """

    def add_publicado(self,string):
        if(type(string)!= int):
            self.published.append(string)
            return True
        else:
            return False

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

"""Clase Articulo que imprime las noticias e imprime el numero de artículos """

class Articulo:
    clase = Noticia()
    num_noti = 0

    def __init__(self):
         self.clase = Noticia()
         self.Num_arti()
         self.Imprime()
         self.Imprime_noti()

    """ Mofifica el numero de noticas almacenadas """

    def Set_numNoti(self,num):
        self.num_noti = num

    """ Imprime los datos title,description, url y publishedAt"""

    def Imprime(self):
        tam = self.clase.num_noticias()
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

