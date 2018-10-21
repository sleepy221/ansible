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

2. Install PIP below:
- ```sudo apt-get install python-pip```

3. Install Python3 (Required if you want to use script for gathering facts)

## Step 1: Clone repo to local machine and copy files to appropriate directory, install pip requirements
1. `git clone https://github.com/castironclay/ansible.git`
2. `cd ansible`
4. `pip install -r requirements.txt`

## Step 2: Run test build

1. from the location of the playbook, run `ansible-playbook playbooks/eve-devices.yml`
- Files will be placed in /tmp/eve/

## Step 3: Modify files to meet your needs
This repo currently is being tested by build a config for a router and a config for a switch. You can modify the vars and template files to meet your needs
1. Router files
- `roles/eve-router/templates`
- `roles/eve-router/vars`
2. Switch files
- `roles/eve-switch/templates`
- `roles/eve-switch/vars`

## Configure vault file with your credentials
If you are using username and password for authentication you'll want to configure an ansible vault file. Listed below are some example steps to do that. 
1. Create file: cred.yml
2. Put 2 YAML variables in file and save
* username: *username*
* password: *password*
3. Encrypt file with ansible vault
`ansible encrypt cred.yml`
4. Specify password
* `[user@server-01 ansible]# ansible-vault encrypt test.yml`
* `New Vault password:`
5. Your file is now AES256 encrypted and can be used within an Ansible playbook. Below is an example of it being used within a gather facts file.
```
---
- name: Gather Facts
  gather_facts: True
  hosts: eve_devices
  vars_files:
    - creds.yml **#full path required if outside current directory**
  
  tasks:
  - name: Configure Provider **#Task to build provider within playbook to be called later**
    set_fact:
      provider:
        username: "{{ username }}"
        password: "{{ password }}"
        host: "{{ inventory_hostname }}"

  - name: Backup Config
    ios_config:
      provider: "{{ provider }}" **#Use your credentials to complete task**
      backup: yes
```
6. To run a playbook containing a vault file remember to include `--ask-vault-pass` at the end of the command to be prompted for your password.
- `ansible-playbook myplaybook.yml --ask-vault-pass`

## Scan new IP range and gather facts
- `playbooks/ping_sweep.py`
I made a python scipt using sockets to scan for devices with port 22 active. This can be ran to scan a new range of IPs. After executing the scipt you'll be prompted to enter your network with CIDR notation.
- `[user@server-01 ansible]# python36 playbooks/ping_sweep.py`
- `Specify network to scan including CIDR notation: 1.2.3.4/24`
After entering your network hosts being found will be printed and you'll be followed by a prompt to enter your vault password


## Versioning

I use [SemVer](http://semver.org/) for versioning

## All Built With

* [PyCharm Professional](https://www.jetbrains.com/pycharm/) - IDE Used
* [Ansible](https://www.ansible.com/) - Automation Framework
* [EVE](http://www.eve-ng.net/) - Network Lab
* [PIP](https://pypi.org/project/pip/) - Python PIP v18.1

## Authors

- Clay C
- Tony P
