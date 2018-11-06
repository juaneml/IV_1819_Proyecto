# IV_1819_Proyecto

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/juaneml/IV_1819_Proyecto.svg?branch=master)](https://travis-ci.org/juaneml/IV_1819_Proyecto)


Repositorio para el Infraestructura Virtual.

## Descripción
El proyecto que se va a realizar es sobre un servicio web que nos notifique de las noticias más destacadas de actualidad de España.
Nos notificará del suceso y en la fecha que ha ocurrido.

## Descripción de la clase
En el proyecto hay dos clases Noticia y Articulo, se usa la lectura de un fichero con extensión json y la estructura es la siguiente.
- Para la clase Noticia se definen las funcionalidades de obtener el título de la noticia, la descripción, la url de la fuente, y la fecha de publicación, así como funcionalidades para cambiar los datos.
- Para la clase Articulo se definen funciones para mostrar las noticias con los parámetros, título, descripción, url, y la fecha de publicación.

## Test
- En el proyecto se hace uso de tests, se hace uso de [Pytest](https://docs.pytest.org/en/latest/), el nombre del test es [test_.py](https://github.com/juaneml/IV_1819_Proyecto/blob/master/test/test_.py)
- Además los test pasan por el servicio de integración continua [Travis-CI](https://travis-ci.org/juaneml/IV_1819_Proyecto) que se ha configurado para el repositorio del proyecto.

## Herramientas a Usar

### Lenguaje
- El lenguaje que se va a usar es [Python](https://www.python.org/) un lenguaje que personalmente me gusta.

### Framework

- El framework que voy a usar es [hug](http://www.hug.rest/). Hug tiene como objetivo hacer que desarrollar API impulsadas por Python sea lo más simple posible, pero no más simple. Como resultado, simplifica drásticamente el desarrollo de la API de Python.

### Base de datos
- Para la base de datos voy a utilizar [Mysql](https://www.mysql.com/) .
