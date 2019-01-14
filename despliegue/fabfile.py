from fabric.api import *

#Muestra el estado del DNS de nuestra app, si
def StatusDns():
    run('curl http://iv1819noticias.westeurope.cloudapp.azure.com/status')

def GuardaVersionAnterior():
    run('cp -r ./iv1819proyecto oldiv1819proyecto')

def EliminarVersionAnterior():
    run('rm -rf ./oldiv1819proyecto')

def EliminarVersion():
    run('rm -rf ./1819proyecto')
    
def InstallReq():
    run('pip3 install -r ./iv1819proyecto/requirements.txt')

def ClonRepo():
    run('git clone https://github.com/juaneml/IV_1819_Proyecto.git iv1819proyecto/')

def MicroservicioSecure():
    ## Se guarda la version anterior
    GuardaVersionAnterior()
    # Clonamos nuestro respotorio de github
    ClonRepo()
    ## Instalamos requirements.txt
    InstallReq()

def MicroservicioClean():
    # Eliminamos la carpeta almacenada y hacemos un clonacion del
    # repositorio
    EliminarVersionAnterior()
    ClonRepo()

def LanzarApp():
    run('cd ./iv1819proyecto/src/ && sudo gunicorn proyecto-dep-app:__hug_wsgi__ -b 0.0.0.0:80')

def StopApp():
    run('sudo pkill -f gunicorn')
