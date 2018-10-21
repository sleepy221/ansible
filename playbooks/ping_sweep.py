import socket
import ipaddress
import os
import time

# Create inventory file
f= open("live_hosts.txt","w+")

# Configure inventory file
f.write("[all:vars]\n""device_type=cisco:ios\n""ansible_network_os = ios\n""ansible_connection = network_cli\n""[hosts]\n")

# Get network from user
scan = input("Specify network to scan including CIDR notation: ")
start = time.time()
# Specify range

network = ipaddress.ip_network(scan)

# Check for live hosts with port 22 open and write to inventory file
for i in network.hosts():
	i = str(i)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# Set timeout 3/10th of a second. Should have no problem detecting devices on LAN
	sock.settimeout(0.030)
	result = sock.connect_ex((i,22))
	if result == 0:
		f.write(i + "\n")
		print(i)

# Close file
f.close()

# Run ansible playbook targetting newly created file
os.system("ansible-playbook -i live_hosts.txt /etc/ansible/playbooks/3_gather_live_facts.yml --ask-vault-pass")

end = time.time()
print(end -start, "seconds")
