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

- Necesitamos crear un fichero con nombre Dockerfile en nuestro repositorio de github, para que docker pueda construir nuestro contenedor, tenemos que especificarle la imagen que vamos a usar así como las depencencias y requisitos necesarios.

El Dockerfile quedaría tal que así:

~~~~
FROM python:3
LABEL maintainer="juaneml@correo.ugr.es"
WORKDIR src/
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD cd src && gunicorn proyecto-dep-app:__hug_wsgi__ --log-file -
~~~~


- Se usa FROM python:3, la imagen oficial de python ya que está optimizada. Con RUN pip instalamos el lenguaje, así como los requisitos que se necesiten. Se copia todo el trabajo realizado y se expone, usando EXPOSE, un puerto.

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

- Para hacer el desplieque hacemos uso de la [documentación](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml) disponible en heroku.

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
- Por último actuliazamos ejecutando el comando:
~~~
git push heroku master
~~~

<<<<<<< HEAD
### Ejemplos
[Ejemplo](http://localhost:8000/una_noticia?noticia=Es%20una%20noticia%20interesante%20&lugar=Espa%C3%B1a)
=======
### Contenedor heroku
[heroku docker](https://proyectoiv-docker.herokuapp.com/) nos devuelve 
~~~
{"status": "OK"}
~~~
>>>>>>> afe7dd79d30bfcfc76dc157c5eb9a3935fa52d48
