#!/usr/bin/python
# -*- coding: utf-8 -*-
"""A simple API to enable adding two numbers together"""
import urllib.request, json
import os



class mi_service:
    """ Clase para el microservicio """
    def fun():
        with urllib.request.urlopen("https://newsapi.org/v2/top-headlines?sources=el-mundo&apiKey=3daa18d2a35747a4ab8a03b449c7e048") as url:
            data = json.loads(url.read().decode('utf-8'))

            # for date in data:
            #     print (date)
        leer = json.loads(open('datos.json').read())
        list=[]
        for i in leer:
            list.append(i['description'])


        return  '%s %s' % (list[0], list[1])
