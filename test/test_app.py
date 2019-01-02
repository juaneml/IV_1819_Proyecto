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

    def test_post_noticias(self):
        response = requests.post(url+'/method_post')
        assert(response.status_code == 200)

    def test_put_noticias(self):
        response = requests.put(url+'method_put?noticia=una noticia&anterior=es anterior&nuevo=es nuevo')
        assert(response.status_code == 200)



if __name__ == '__main__':
	unittest.main()
