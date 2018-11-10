
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hug
import json
import sys
from first import *
import jinja2
from jinja2 import FileSystemLoader, Environment
from jinja2 import Template


@hug.cli()
@hug.get('/')
def getEstado():
    salida = {"status": "OK"}
    return salida

@hug.get('/status')
def status():
    status = {"status": "OK"}      
    return status

if __name__ == '__main__':
    add.interface.cli()
