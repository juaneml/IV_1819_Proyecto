
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hug
import json
import sys
from first import *
import jinja2
from jinja2 import FileSystemLoader, Environment
from jinja2 import Template



template_engine = Environment(loader=FileSystemLoader("src/templates"))
def get_template(name):
    return template_engine.get_template(name)

@hug.cli()
#@hug.local()
@hug.get('/')
def getEstado():
    salida = {"status": "OK"}
    salida = salida.decode('utf-8')
    return salida

@hug.get('/status')
def status():
    status = {"status": "OK"}
    status = status.decode('utf-8')          
    return status

if __name__ == '__main__':
    add.interface.cli()
