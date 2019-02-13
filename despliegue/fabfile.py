from fabric.api import *

# Muestra el estado del DNS de nuestra app

def StatusDns():
    run('curl http://iv1819noticias.westeurope.cloudapp.azure.com/status')

# Funcion para mantener la version anterior del microservicio

def GuardaVersionAnterior():
    run('cp -r ./iv1819proyecto oldiv1819proyecto')

# Funcion para eliminar la version anterior
def EliminarVersionAnterior():
    run('rm -rf ./oldiv1819proyecto')

# Funcion para eliminar el microservicio
def EliminarVersion():
    run('rm -rf ./iv1819proyecto')

# Funcion para instalar requirements
def InstallReq():
    run('pip3 install -r ./iv1819proyecto/requirements.txt')

# Funcion para clonar el repositorio
def ClonRepo():
    run('git clone https://github.com/juaneml/IV_1819_Proyecto.git iv1819proyecto/')

# Funcion que actualiza el microservicio guardando una version anterior
# Para ello hacemos la llamada de la funcion GuardaVersionAnterior
# Posteriormente clonamos el repositorio del microservicio con la funcion ClonRepo
# Por ultimo instalamos requirements haciendo uso de la funcion InstallReq

def MicroservicioSecure():
    ## Se guarda la version anterior
    GuardaVersionAnterior()
    # Eliminamos contenido
    EliminarVersion()
    # Clonamos nuestro respositorio de github
    ClonRepo()
    ## Instalamos requirements.txt
    InstallReq()

# Funcion que actualiza el microservicio  sin la version anterior
# Para ello hacemos la llamada de la funcion EliminarVersion
# Posteriormente clonamos el repositorio del microservicio con la funcion ClonRepo
# Por ultimo instalamos requirements haciendo uso de la funcion InstallReq

def MicroservicioClean():
    # Eliminamos la carpeta almacenada y hacemos una clonacion del
    # repositorio
    EliminarVersion()
    ClonRepo()
    ## Instalamos requirements.txt
    InstallReq()

# Funcion para iniciar el microservicio
def LanzarApp():
    run('cd ./iv1819proyecto/src/ && sudo gunicorn proyecto-dep-app:__hug_wsgi__ -b 0.0.0.0:80')

# Funcion para parar el microservicio
def StopApp():
    run('sudo pkill -f gunicorn')
