# IV_1819_Proyecto

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/juaneml/IV_1819_Proyecto.svg?branch=master)](https://travis-ci.org/juaneml/IV_1819_Proyecto)


Repositorio para el Infraestructura Virtual.

## Descripción
El proyecto que se va a realizar es sobre un servicio web que nos notifique de las noticias más destacadas de actualidad de España.
Nos notificará del suceso y en la fecha que ha ocurrido.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://proyecto-iv.herokuapp.com/)

## Documentación del proyecto
[Documentación](https://github.com/juaneml/IV_1819_Proyecto/tree/master/doc)

## Descripción de la clase
En el proyecto hay dos clases Noticia y Articulo, se usa la lectura de un fichero con extensión json y la estructura es la siguiente.
- Para la clase Noticia se definen las funcionalidades de obtener el título de la noticia, la descripción, la url de la fuente, y la fecha de publicación, así como funcionalidades para cambiar los datos.
- Para la clase Articulo se definen funciones para mostrar las noticias con los parámetros, título, descripción, url, y la fecha de publicación.

## Test
- En el proyecto se hace uso de tests, se hace uso de [Pytest](https://docs.pytest.org/en/latest/), el nombre del test es [test_.py](https://github.com/juaneml/IV_1819_Proyecto/blob/master/test/test_.py)

- El proyecto se hace uso de un segundo test, [test_app.py](https://github.com/juaneml/IV_1819_Proyecto/blob/master/test/test_app.py) donde se testean las urls.

- Además los test pasan por el servicio de integración continua [Travis-CI](https://travis-ci.org/juaneml/IV_1819_Proyecto) que se ha configurado para el repositorio del proyecto.
- [Configuración](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/Int-Cont-Trav.md)

### Ejecutar los test
~~~
pytest test_.py
pytest test_app.py
~~~
## Herramientas a Usar

### Lenguaje
- El lenguaje que se va a usar es [Python](https://www.python.org/) un lenguaje que personalmente me gusta.

### Framework

- El framework que voy a usar es [hug](http://www.hug.rest/). Hug tiene como objetivo hacer que desarrollar API impulsadas por Python sea lo más simple posible, pero no más simple. Como resultado, simplifica drásticamente el desarrollo de la API de Python.

### Base de datos
- Para la base de datos voy a utilizar [Mysql](https://www.mysql.com/) .


## Instalación

- Para poder instalar este microservicio, clona el repositorio:

~~~
git clone https://github.com/juaneml/IV_1819_Proyecto.git
pip3 install -r requirements.txt
~~~


## Plataforma Heroku como servicio (PaaS) para la integración continua
- Para saber como configurar [ver](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/heroku.md)

## Docker
Contenedor:https://proyectoiv-docker.herokuapp.com/

[Imagen DockerHub](https://hub.docker.com/r/juaneml/iv-1819-proyecto)
- [Documentación](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/docker.md)

## Despliegue en Heroku
URL despliegue https://proyecto-iv.herokuapp.com/


## Despliegue azure

- Despliegue final: 23.97.233.73

- Para consultar la documentación [consulta](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/azurecloud.md)
