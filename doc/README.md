# Documentación para el proyecto.
El proyecto que se va a realizar es sobre un microservicio que de las noticias
más relevantes, partimos de una primera versión en la que a partir de un fichero
con extensión .json que se optienen a partir de la [API del periódico del mundo] (https://newsapi.org/s/el-mundo-api)

# Herramientas que van a ser usadas

* [Hug](https://www.hug.rest) como micro-framework web.
  * Se va a usar porque me parece intuitivo y sencillo para la creación del microservicio y como he usado [Flask](flak.pocoo.org) quería experimentar con otro tipo de micro-framework web.

* [Travis-CI](http://travis-ci.org) servicio que proporciona la integración continua.
  * Permite el servicio de ejecutar tests de nuestro repositorio en Github, solo tenemos que registrarnos y elegir el repositorio al que queremos hacer el seguimiento.

* [Mysql](https://www.mysql.com) para el almacenamiento y gestión de las base de datos.
  * Herramienta conocida y extendida, sencilla de manejar, gratuita y documentación extensa.

* [Heroku](https://www.heroku.com/), plataforma como servicio (PaaS) para integración continua.
  * Plataforma de servicio en la Nube, integración del proyecto en pocos pasos, soporta amplia gama de lenguajes para distintos tipos de necesidades.


* Clases del proyecto
  * Clase Noticia, en esta clase se definen métodos para la gestión de datos obtenidos de un fichero con extensión .json, tales datos son el título de una noticia, la descripción, la url de la fuente de la noticia y la fecha de la publicación.

  * Clase Articulo, con esta clase se hizo para la impresión de noticias así como comprobar que los datos almacenados en una lista han  sido correctos.
