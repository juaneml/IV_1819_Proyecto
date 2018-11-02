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

script: cd ./test && pytest
	
## Ejemplo de salida:
![travis.png](https://github.com/juaneml/IV_1819_Proyecto/tree/master/doc/travis.png)

##Test