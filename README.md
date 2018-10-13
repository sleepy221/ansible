# Cisco IOS Configuration Builder
This project will create templates for Cisco IOS devices

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites
1. Install Ansible via appropriate method:
https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

- ```sudo apt-get update```
- ```sudo apt-get install software-properties-common```
- ```sudo apt-add-repository --yes --update ppa:ansible/ansible```
- ```sudo apt-get install ansible```

2. Install PIP and PIP modules below:
- ```sudo apt-get install python-pip```
- ```pip install ipaddr```
- ```pip install ipaddress```
- ```pip install jinja2```
- ```pip install PyYAML```

## Step 1: Clone repo to local machine and copy files to appropriate directory
1. ```git clone https://github.com/castironclay/ansible.git```
2. ```cd ansible```
3. ```mkdir /etc/ansible/playbooks && mkdir /etc/ansible/roles```
4. ```cp -r roles/* /etc/ansible/roles && cp -r playbooks/* /etc/ansible/playbooks```

## Step 2: Run test build
1. ```ansible-playbook /etc/ansible/playbooks/eve-devices.yml```
- Files will be placed in /tmp/eve/

## Step 3: Modify files to meet your needs
This repo currently is being tested by build a config for a router and a config for a switch. You can modify the vars and template files to meet your needs
1. Router files
- ```/etc/ansible/roles/eve-router/templates```
- ```/etc/ansible/roles/eve-router/vars```
2. Switch files
- ```/etc/ansible/roles/eve-switch/templates```
- ```/etc/ansible/roles/eve-switch/vars```

## Versioning

I use [SemVer](http://semver.org/) for versioning

## All Built With

* [PyCharm Professional](https://www.jetbrains.com/pycharm/) - IDE Used
* [Ansible](https://www.ansible.com/) - Automation Framework
* [EVE](http://www.eve-ng.net/) - Network Lab
* [PIP](https://pypi.org/project/pip/) - Python PIP v18.1

## Authors

- Clay Coppage
