#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import imp
import pytest
import unittest
sys.path.append('../src/')
from principal import *

class TestMethods(unittest.TestCase):

    with open('../json/datos_m.json','r') as noti:
            lista_noticias = json.load(noti)

    pruebaNot = Newsgroups()
    pruebaNot.Crea_news(lista_noticias)

    """ Test noticia """

    def test_noticia(self):
        self.assertEqual(self.pruebaNot.getNumNot(),20,"Se han añadido correctamente las 20 noticias") 
        self.assertEqual(self.pruebaNot.getNoticia().get_titulo("titulo"),False,"El indice debe ser un entero")

    """ Test titulo """

    def test_titulo(self):
        self.assertEqual(self.pruebaNot.getNoticia().get_titulo(0),str('German governing parties punished in state election'),"Titulo Correcto")
        self.assertEqual(self.pruebaNot.getNoticia().set_titulo(0),False,"Debe ser una cadena")

    """ Test titulo """

    def test_descrip(self):
        self.assertEqual(self.pruebaNot.getNoticia().get_descrip(0),str(' '),"Descripcion vacia")
        self.assertEqual(self.pruebaNot.getNoticia().get_descrip(1),str('The deal was just announced.'),"Descripción valida")

if __name__ == '__main__':
    unittest.main()
