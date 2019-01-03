# El despliegue en Docker

- Nos dirigimos a create Repository  y creamos un repositorio.
![create](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/images/create_repository.png)
- Elegimos el nombre de nuestro contenedor y la descripción, dejamos la visibilidad pública.
- Para la configuración de compilación, build settings, nos conectamos a nuestro repositorio de github. Seleccionamos nuestro usuario y el repositorio que queremos usar.
- Para las reglas de compilación dejamos la que nos viene por defecto, latest, y finalmente create and build.
![docker_create](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/images/docker_create.png)

- Para automatizar la creación de la imagen cada vez que hacemos push en github,
seleccionamos nuestro respositorio, nos vamos a builds, configure automated builds y seleccionamos autobuild y build caching.
![autobuild](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/images/autobuild.png)

- Necesitamos crear un fichero con nombre Dockerfile en nuestro repositorio de github, para que docker pueda construir nuestro contenedor, tenemos que especificarle la imagen que vamos a usar, así como las dependencias y requisitos necesarios, para la creación del DockerFile hemos visitado la [documentación](https://hub.docker.com/_/python/).

El Dockerfile quedaría tal que así:

~~~~
FROM python:3
LABEL maintainer="juaneml@correo.ugr.es"
WORKDIR src/

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 80
CMD cd src && gunicorn proyecto-dep-app:__hug_wsgi__
~~~~


- Se usa FROM python:3, uso esta imagen y no otra porque tiene una gran cantidad de paquetes Debian comunes y así pueda ahorrarme que tenga problemas de dependencias. Con RUN pip instalamos el lenguaje, así como los requisitos que se necesiten. Se copia todo el trabajo realizado y se expone, usando EXPOSE, un puerto.

- También creamos otro fichero .dockerignore para evitar que se copien ficheros innecesarios tales como los test y la configuraciones tanto para travis y heroku, tal fichero quedaría tal que así:

~~~~
# Excluimos los archivos que no consideramos necesarios
*git
*doc
*test*
*.yml
Procfile
~~~~
## Imagen de docker
[docker](https://hub.docker.com/r/juaneml/iv-1819-proyecto)
## Desplegamos el contenedor en Heroku

- Para hacer el despliegue hacemos uso de la [documentación](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml) disponible en heroku.

- Necesitamos crear el fichero heroku.yml, este nos permite decirle a Heroku que vamos a crear una imagen a partir del fichero DockerFile.

Especificamos la imagen de Docker para compilar el proceso web de la aplicación, tanto heroku.yml como Dockerfile están en el mismo directorio. Si no se incluye run, Heroku usa el CMD especificado en el Dockerfile.

~~~~
build:
  docker:
  web: DockerFile
run:
 web: cd src && gunicorn proyecto-dep-app:__hug_wsgi__ --log-file -
~~~~

- Una vez añadido el fichero heroku.yml, ejecutamos la orden:
~~~
heroku stack:set container -a proyectoiv-docker
~~~

- Indicamos a heroku que es un contenedor y el nombre de la aplicación proyectoiv-docker.
- Por último, actualizamos ejecutando el comando:

~~~
git push heroku master
~~~


### Ejemplos

[Ejemplo get](https://proyectoiv-docker.herokuapp.com/una_noticia?i=2)
[Ejemplo put](https://proyectoiv-docker.herokuapp.com/sustituir_dato?i=2&new=nuevo)

### Contenedor heroku
[heroku docker](https://proyectoiv-docker.herokuapp.com/) nos devuelve
~~~
{"status": "OK"}
~~~
