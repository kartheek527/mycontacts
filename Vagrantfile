# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty32"

   # mapping guest port 8000 to host port 8080
  config.vm.network "forwarded_port", guest: 8000, host: 8080

  # contacts-app from local to vagrant box
  config.vm.synced_folder "mycontacts", "/home/vagrant/mycontacts"


  # provisioning using shell script
  config.vm.provision "shell", path: "./startup.sh"
end
