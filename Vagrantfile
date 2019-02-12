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
    azure.tcp_endpoints = "80"
    azure.resource_group_name = 'iv1819noticias'
    azure.vm_image_urn = 'canonical:ubuntuserver:16.04.0-LTS:latest'

    # Evitar que busque actualizaciones
    config.vm.box_check_update = false

    # dns_name
    azure.dns_name = 'iv1819noticias'


  end

  # Configuración  para provisionar con ansible
  config.vm.provision "ansible" do |ansible|
    ansible.compatibility_mode = "2.0"
    ansible.version = "2.7.5"
    ansible.playbook = "provision/playbook.yml"

  end

end
