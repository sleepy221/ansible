# Cisco IOS Configuration Builder
This project will create templates for Cisco IOS devices

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites
Install Ansible via appropriate method:
- https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

Install any missing pip modules listed below:
- ipaddr
- ipaddress
- jinja2
- PyYAML

## Step 1: Clone repo to local folder no int ```/etc/ansible```
```git clone https://github.com/castironclay/ansible.git```

## Step 2: Modify hosts file to match local IPs
Current hosts file
```
[eve_devices]
10.0.0.46
10.0.0.45

[eve_switch]
10.0.0.45

[eve_router]
10.0.0.46

[all:vars]
device_type=cisco_ios
ansible_connection = network_cli
ansible_user = root
ansible_network_os = ios                    
```
### Note: 
If you will not be pushing the configurations out to any devices you will not need to modify the default Ansible hosts file

## Step 3: 

## Built With
* [PyCharm Professional](https://www.jetbrains.com/pycharm/) - IDE Used
* [Ansible](https://www.ansible.com/) - Automation Framework
* [EVE](http://www.eve-ng.net/) - Network Lab

## Authors
- Clay Coppage
