# -*- coding: utf-8 -*-
import unittest, json, requests
import sys
from requests import *
sys.path.append('../src/')
url = 'https://proyecto-iv.herokuapp.com/'

class testProyecto(unittest.TestCase):
    def test_url_raiz(self):
        response = requests.get(url)
        self.assertEqual(response.json()['status'],'OK', "Aplicación con status OK")

    def test_url_status(self):
        response = requests.get(url+'/status')
        self.assertEqual(response.json()["noticias"]["ruta"],"/noticias", "Correcto")
    def test_url_noticias(self):
        response = requests.get(url+'/noticias')
        self.assertEqual(response.json()['Noticia']['Titulo'],"Granada, una ciudad con encanto","titulo correcto")

if __name__ == '__main__':
	unittest.main()
