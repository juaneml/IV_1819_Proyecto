
import sys
import imp

import unittest
sys.path.append('../src/')
from first import *

class TestMethods(unittest.TestCase):
    pruebaArt = Articulo()
    pruebaNot = Noticia()
    def test_noticia(self):
        self.assertEqual(str(self.pruebaNot.num_noticias()),str(self.pruebaArt.Num_arti()),"Coincide")

    def test_titulo(self):
        self.assertEqual(self.pruebaNot.get_titulo(0),str('German governing parties punished in state election'),"Titulo Correcto")


    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
