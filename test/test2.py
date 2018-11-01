#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('../src')
from first import *

class Test(unittest.TestCase):

    #pruebaArt = Articulo()
    #pruebaNot = Noticia()

    """Test noticias """
    def TestNoticias(self):
        self.assertEqual(str(self.pruebaNot.num_noticias()),str(self.pruebaArt.Num_arti()),"Coincide")
        self.assertEqual(self.pruebaNot.get_titulo(0),str('German governing parties punished in state election'),"Titulo Correcto")

if __name__ == '__main__':
    unittest.main()
