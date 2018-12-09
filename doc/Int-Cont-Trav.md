# Integración  Continua (Travis-CI)

Para la integración continua de nuestro proyecto del hacesmo uso de Travis-CI,
para ello seguimos los siguientes pasos:

## Paso 1:
Crear el repositorio y el código con las distintas funcionalidades:

## Paso 2:
Accedemos a la página de [Travis](https://travis-ci.org) y vinculamos nuestra cuenta de GitHub a Travis.

## Paso 3:
Seleccionamos el repositorio que queremos Travis haga el seguimiento y pase los test.

## Paso 4:

Añadimos al repositorio un archivo de configuración con el nombre .travis.yml en el describimo el lenguaje de programación y las distintas dependecias para nuestro proyecto, en mi caso uso python y la configuración es la siguiente:


language: python
python:
	- "3.6.6"
install:
	- pip install -r requirements.txt

script: cd ./test && pytest test_.py
	
## Ejemplo de salida:
![travis.png](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/images/travis.png)

## Test
Los [Test](https://github.com/juaneml/IV_1819_Proyecto/blob/master/test/test_.py) se han realizado para comprobar que los distintos métodos de la clase [first](https://github.com/juaneml/IV_1819_Proyecto/blob/master/src/first.py) funcionan correctamente.

* test_noticia: Comprueba que el número de noticias y artículos coincide, y que el índice para obtener el título es un entero

* test_titulo: Comprueba que la obtención del titulo es el deseado del indice 0, y que el cambio de un título debe ser una cadena de carácteres.

* test_descrip: Comprueba que la descripción del índice 0 es vacía y que la descripción del índice 1 es la deseada.
