#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src')
from first import *

class Test(unittest.TestCase):

    pruebaArt = Articulo()#.Imprime(Articulo)
    pruebaNot = Noticia()#.fun()
    """ Test Nocicias """
    def testNoticias(self):
        self.assertEqual(self.pruebaNot.num_noticias(),self.pruebaArt.Num_arti(),"Numeros iguales")
    	self.assertEqual(self.pruebaNot.get_titulo(0),str('German governing parties punished in state election'),"Titulo Correcto")

if __name__ == '__main__':
    unittest.main()
