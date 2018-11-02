#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import imp
import pytest
import unittest
sys.path.append('../src/')
from first import *

class TestMethods(unittest.TestCase):
    pruebaArt = Articulo()
    pruebaNot = Noticia()

    """ Test noticia """

    def test_noticia(self):
        self.assertEqual(str(self.pruebaNot.num_noticias()),str(self.pruebaArt.Num_arti()),"Coincide")
        self.assertEqual(self.pruebaNot.get_titulo("titulo"),False,"El indice debe ser un entero")

    """ Test titulo """
    def test_titulo(self):
        self.assertEqual(self.pruebaNot.get_titulo(0),str('German governing parties punished in state election'),"Titulo Correcto")
        self.assertEqual(self.pruebaNot.set_titulo(0),False,"Debe ser una cadena")

    """ Test titulo """
    
    def test_descrip(self):
        self.assertEqual(self.pruebaNot.get_descrip(0),str(''),"Descripcion vacia")
        self.assertEqual(self.pruebaNot.get_descrip(1),str('The deal was just announced.'),"Descripción valida")

if __name__ == '__main__':
    unittest.main()
