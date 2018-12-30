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
    comentario = []

    def __init__(self):
        self.titulo = []
        self.descrip = []
        self.url = []
        self.published = []
        self.num_noti = 0
        self.comentario = []


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

        if(type(string) != int):
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

    """Add comentario """
    def add_coment(self,coment):
        if(type(coment)!= int):
            self.comentario.append(coment)
            return True
        else:
            return False

    """ get comentario """
    def get_comentario(self,coment):
        try:
            return self.comentario[coment]
        except:
            return " "

    """ set comentario """
    def set_comentario(self,id_coment,string):

        if(type(string)!= int):
            print("cambio en set_comentario",id_coment,string)
            self.comentario[id_coment] = string
            return True
        else:
            return False


    """ Imprime la noticia """
    def to_s(self,i):
        tam = self.num_noti
        print(" Titulo:",''.join(self.get_titulo(i)),"\n","Descripción:",''.join(self.get_descrip(i)),"\n",
        "Url:",''.join(self.get_url(i)),"\n","Fecha publicación:",''.join(self.get_publicado(i)),"\n",
        "Comentario:",'',self.get_comentario(i),"\n")



"""Clase Newsgroups, clase que crea varias noticias """
class Newsgroups():
    noticia = Noticia()

    def __init__(self):
        self.lista_noticias =[]
        self.noticia = Noticia()
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
                self.lista_noticias.append(self.noticia.add_url(" "))
            if(i['publishedAt']!=None):
                self.lista_noticias.append(self.noticia.add_publicado(i['publishedAt']))
            else:
                self.lista_noticias.append(self.noticia.add_publicado(" "))

            if(self.noticia.get_comentario(i) != None):
                self.lista_noticias.append(self.noticia.add_coment(self.noticia.get_comentario(i) ))
            else:
                self.lista_noticias.append(self.noticia.add_coment(" "))

            self.cont+=1

    """ Devuelve la noticia """

    def getNoticia(self):
        return self.noticia

    """ Devuelve el número de noticias """

    def getNumNot(self):
        return self.cont

    """ Busca noticia """
    def busca_not(self,id_not):
        noticia = self.getNoticia()
        cont = 0
        es = False
        exit = 0
        while cont in range(self.getNumNot()) and not exit:
            if(noticia.get_titulo(cont).find(id_not) != -1):
                es = True
                exit = cont
            
            cont=cont+1


        if(es == False):
            exit = -1

        return exit

    """ Add un comentario dado una subcadena """

    def Set_news(self,lista,id_not,comentario):
        lista = lista
        id_titulo = self.busca_not(id_not)
        for i in lista:

            if(i['title'].find(self.noticia.get_titulo(id_titulo)) != -1 ):
                self.lista_noticias.append(self.noticia.add_coment(comentario))
                self.noticia.set_comentario(id_titulo,comentario)
                print("Has añadido el comentario",self.noticia.get_comentario(id_titulo))

            else:
                self.lista_noticias.append(self.noticia.add_coment(""))


if __name__=='__main__':
    with open('../json/datos_m.json','r') as noti:
            lista_noticias = json.load(noti)

    newgroups = Newsgroups()
    newgroups.Crea_news(lista_noticias)
    num_groups = newgroups.getNumNot()


    for i in range(num_groups):

        print("***********  NOTICIA  *************")
        newgroups.getNoticia().to_s(i)
        print("******************************","\n")



    print("Numero de Noticias "," ",newgroups.getNumNot() )


    while True:
      print("¿Quieres añadir un comentario, SI o NO?")
      res = input()
      print("res", res)
      if (res == 'SI' or res == 'si'):
          print("Dame datos del titulo a buscar: ")
          tit_noticia = input()
          print("Ahora el comentario")
          comentario=input()
          newgroups.Set_news(lista_noticias,tit_noticia,comentario)
      else:
          break


    for i in range(num_groups):

        print("***********  NOTICIA  *************")
        newgroups.getNoticia().to_s(i)
        print("******************************","\n")
