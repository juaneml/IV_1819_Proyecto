# Despliegue desde 0, azure

- Para llevar a cabo el despliegue tenemos que hacer la instalación de herramientas tales como,
[Vagrant](https://www.vagrantup.com/),[ansible](https://www.ansible.com/),[fabric](https://get.fabric.io/)

##Azure
- Antes de comenzar a usar azure y poder desplegar nuestro servicio necesitamos:
Instalar azure [cli](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli?view=azure-cli-latest)
que nos va a permitir conectarnos a nuestra suscripción de azure y crear nuestra máquina virtual.

Una vez instalada la herramienta Vagrant y la herramienta que nos proporciona azure, procedemos con los siguientes pasos:

### Paso 1

~~~
az login
~~~
Con el siguiente comando iniciamos sesión en nuestra suscripción de azure, se nos abrirá una
ventana en el navegador e iniciamos sesión.

### Paso 2

~~~
az ad sp create-for-rbac
~~~

- Para crear una aplicación de Azure Active Directory con acceso a Azure Resource Manager para la suscripción actual de Azure

### Paso 3
~~~
az account list --query "[?isDefault].id" -o tsv
~~~
para obtener tu ID de suscripción de Azure.

### Paso 4
~~~
az ad sp create-for-rbac
~~~
debe ser similar a la siguiente:

~~~
{
  "appId": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
  "displayName": "some-display-name",
  "name": "http://azure-cli-2017-04-03-15-30-52",
  "password": "XXXXXXXXXXXXXXXXXXXX",
  "tenant": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
}
~~~

Los valores tenant, appIdy se passwordasignan a los valores de configuración azure.tenant_id, azure.client_idy azure.client_secreten su archivo o variables de entorno Vagrant.


## Creación del Vagrantfile

Para la creación del Vagranfile es necesario hacer las exportaciones de las variables de azure que necesita vagrant:

AZURE_SUBSCRIPTION_ID = Resultado Paso 3
AZURE_CLIENT_ID = Paso 4 campo appId
AZURE_TENANT_ID = Paso 4 campo tenant
AZURE_CLIENT_SECRET = Paso 4 campo password

Abrimos terminal y exportamos las variables:

~~~
export AZURE_SUBSCRIPTION_ID="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
export AZURE_CLIENT_ID="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
export AZURE_TENANT_ID="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
export AZURE_CLIENT_SECRET="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
~~~

Una vez exportadas las variables procedemos a la creación del Vagrantfile.

## Comentamos que hemos hecho
~~~
vagrant box add cloud_azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
~~~

- Con el siguiente comando le estamos diciendo a vagrant que cree un box llamado cloud_azure indicándole el destino donde está y el proveedor azure.


- Mi Vagrantfile quedaría como sigue:
~~~

Vagrant.configure('2') do |config|
  config.vm.box = "cloud_azure"

  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.provider :azure do |azure, override|

    # each of the below values will default to use the env vars named as below if not specified explicitly
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    azure.vm_name = 'iv1819noticias'
    azure.vm_size = 'Standard_DS2_v2'
    azure.location = 'westeurope'
    azure.tcp_endpoints = 80


  end

  # Configuración  para provisionar con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provision/playbook.yml"
  end

end

~~~

- Con el archivo [Vagranfile](https://github.com/juaneml/IV_1819_Proyecto/blob/master/Vagrantfile), indicamos que tengamos conexión a nuestra máquina virtual mediante ssh por la configuración
~~~
  config.ssh.private_key_path = '~/.ssh/id_rsa'
~~~
y el puerto 80
~~~
azure.tcp_endpoints = 80
~~~

- El nombre de nuestra máquina virtual es iv1819noticias
- Con un tamaño Standard_DS2_v2 "que nos proporciona Uso equilibrado de la CPU en proporción de memoria. Ideal para desarrollo y pruebas, bases de datos pequeñas o medianas, y servidores web de tráfico bajo o medio". [consultado](https://docs.microsoft.com/es-es/azure/virtual-machines/windows/sizes)

~~~
azure.location = 'westeurope'
~~~
- Le indicamos dónde queremos alojar nuestra máquina.

- Por último le decimos que vamos a provisionar con ansible con :
~~~
config.vm.provision "ansible" do |ansible|
  ansible.playbook = "provision/playbook.yml"
end
~~~

- También necesitamos instalar el plugin de azure para vagrant con el comando:
~~~
vagrant plugin instalar vagrant-azure
~~~

- Y por último para levantar nuestra máquina hacemos uso del comando:
~~~
vagrant up --provider = azure
~~~

- En la siguiente captura podemos ver el resultado:
![vagrant_up](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/images/vagrant_up.png)

Enlaces consultados:
- [tutorial](https://github.com/Azure/vagrant-azure/blob/v2.0/README.md)
- [Configuración Vagrantfile-1](https://github.com/Azure/vagrant-azure/blob/v2.0/README.md)
- [Configuración Vagrantfile-2](https://azure.microsoft.com/es-es/resources/videos/azure-virtual-machine-creation-and-set-up-using-vagrant-with-corey-fowler/)

- [az Comandos](https://docs.microsoft.com/en-us/cli/azure/ad/app?view=azure-cli-latest)

- [Lista plugin Vagrant](https://github.com/hashicorp/vagrant/wiki/Available-Vagrant-Plugins)
- [Configuración vagrant con ansible](https://www.vagrantup.com/docs/provisioning/ansible.html)


### Para conectarnos mediante ssh a nuestras máquinas

- Conectar

~~~
 vagrant ssh
~~~

### Para parar nuestra máquina virtual ejecutamos el comando:
- Apagar

~~~
 vagrant halt
~~~


#Ansible

- Para aportar el provisionamiento a la máquina virtual hago uso de ansible.

Ansible lo que nos permite una vez creada la máquina provisionar de utilidades que necesita nuestra máquina, de forma que automaticemos el aprovisionamiento, tales como instalaciones de paquetes como pip3,git, la clonación de nuestro repositorio y la instalación de los requirements necesarios definidos en nuestro repositorio y que nuestra máquina necesita para desplegarse y lanzar nuestro microservicio.

- El archivo necesario tiene extensión .yml tiene el nombre de [playbook.yml](https://github.com/juaneml/IV_1819_Proyecto/blob/master/provision/playbook.yml)

Mi playbook.yml tiene el siguiente contenido:

~~~
---
- hosts: all
  become: yes
  tasks:


    # Instalacion de git
    - name: Instala git
      apt: pkg=git state=present


    # Clonamos Repositorio
    - name: Clonar nuestro repositorio en github
      git:
        repo: https://github.com/juaneml/IV_1819_Proyecto.git
        dest: iv1819proyecto/


    # Instalación de  Python 3

    # Repositorios necesarios para python3
    - name: repositorios necesario deadsnakes PPA python3
      apt_repository: repo=ppa:deadsnakes/ppa state=present

    #Actualzamos repositorio
    - name: update repositorio
      command: sudo apt-get update

    #Instalamos python3
    - name: Instalación python3
      apt: pkg=python3.6 state=present


  # Instalamos pip3

    - name: Instalación pip3
      apt: pkg=python3-pip state=latest

  # Instalamos Requirements necesarios para nuestro microservicio

    - name: Install requirements.txt
      command: pip3 install -r ./iv1819proyecto/requirements.txt

~~~

- Si queremos volver a provisionar una vez creada nuestra máquina, podemos hacerlo mediante al comando:
~~~
vagrant provision
~~~



Enlaces consultados:
- [Documentación](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/ansible-install-configure?toc=%2Fen-us%2Fazure%2Fansible%2Ftoc.json&bc=%2Fen-us%2Fazure%2Fbread%2Ftoc.json#file-credentials)

- Como uso python3 instalo como dice la [documentación](https://docs.python-guide.org/starting/install3/linux/)
- Para añadir el repositorio consulto[1](https://docs.python-guide.org/starting/install3/linux/) y consulto[2](https://blog.jetbrains.com/pycharm/2017/12/developing-in-a-vm-with-vagrant-and-ansible/)

#Fabric

Para el despliegue y ejecución de la aplicación, hago uso de Fabric.

Mi fabfile tiene el siguiente contenido:
~~~
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
    # Clonamos nuestro repositorio de github
    ClonRepo()
    ## Instalamos requirements.txt
    InstallReq()

def MicroservicioClean():
    # Eliminamos la carpeta almacenada y hacemos un clonación del
    # repositorio
    EliminarVersion()
    ClonRepo()

def LanzarApp():
    run('cd ./iv1819proyecto/src/ && sudo gunicorn proyecto-dep-app:__hug_wsgi__ -b 0.0.0.0:80')

def StopApp():
    run('sudo pkill -f gunicorn')
~~~

- El método StatusDns comprueba nuestra url con el uso de curl.
- El método GuardaVersionAnterior, guarda la versión anterior.
- El método EliminarVersionAnterior, elimina la versión anterior creada.
- El método EliminarVersion, elimina la carpeta almacenada.
- El método InstallReq, instala los requirements.
- El método ClonRepo, clona nuestro repositorio.
- El método MicroservicioSecure, guarda la versión anterior, clona nuestro repositorio e instala los requirements.
- El método MicroservicioClean, elimina la carpeta almacenada.
- El método LanzarApp, iniciamos la aplicación.
- El método StopApp, detenemos la aplicación.



# Resultados

[DNSstatus](https://github.com/juaneml/IV_1819_Proyecto/blob/master/doc/images/dns_status_ok.png)
