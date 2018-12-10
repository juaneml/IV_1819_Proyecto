# Despliegue de aplicación en heroku

En el siguiente documento veremos los pasos para desplegar nuestra apliación.

## Paso 1:
- Nos registramos en [Heroku](https://www.heroku.com/)
- Elegimos el nombre de nuestra apliación, en mi caso proyecto-iv
![create](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/images/create_new_app.png)

## Paso 2:
- Conectamos nuestra aplicación con nuestro repositorio eh Github
![connect](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/images/conect_github.png)

## Paso 3:
- Activamos la opción Wait for CI to pass before deploy, ya que tenemos a Travis para
la ejecución de los tests.
![automatic_desploy](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/images/automatic_deploys.png)

# Adaptamos el proyecto para la ejecución de heroku
- Añadimos los requerimientos en el arquivo requirements.txt necesarios en mi caso son los siguientes :
   ~~~
    Hug==2.4.1
    pytest==3.9.3
    gunicorn
   ~~~
# Añadimos un nuevo archivo con nombre Procfile con el contenido siguiente:
  ~~~ 
   web: cd src && gunicorn proyecto-dep-app:__hug_wsgi__ --log-file -
  ~~~
 - Este archivo es necesario para indicarle a Heroku como ejecutar nuestra aplicacion, indica que se mueva al directorio donde está la aplicación, directorio src, con el servidor web gunicorn ejecute la aplicación de python que usa como framework hug  con los parámetros __hug_wsgi__ como nos indica la documentación [hug](https://www.hug.rest/website/quickstart) y así integre nuestra aplicación de microservicio.

 - Así ya tendremos a nuestra aplicación en la nube:
 
 Para acceder a la aplicación podemos hacerlo mediante el enlace: [https://proyecto-iv.herokuapp.com/](https://proyecto-iv.herokuapp.com/)


 # Comprobamos que todo ha ido bien:
  - En la ruta / de nuesta apliación abrimos el terminal y hacemos uso del comando curl y accedemos a la url que nos proporciona Heroku de    nuestra aplicación.
   ~~~
   $curl https://proyecto-iv.herokuapp.com/
   {"status": "OK"}
   ~~~
   - Se ha añadido /status a nuestra aplicación y ejecutando el comando curl obtenemos la siguiente salida:
   ~~~
   {"status": "OK", "noticias": {"ruta": "/noticias", "valores": {"Titulo": "Granada, una ciudad con encanto", "Descrip":        "Granada tiene cada vez más visitantes para ver la Alhambra", "url": "www.ideal/es_un_ejemplo", "publicado": "7/11/2018",      "json": "devuelto"}}}
   ~~~
  - Se ha añadido /noticias a nuestra aplicación y el resultado de salida es el siguiente:
  ~~~
   {"Noticia": {"Titulo": "Granada, una ciudad con encanto", "Descrip": "Granada tiene cada vez más visitantes para ver la        Alhambra", "url": "www.ideal/es_un_ejemplo", "publicado": "7/11/2018", "json": "devuelto"}}
  ~~~
