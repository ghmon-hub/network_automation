import subprocess
import ipaddress
import json
import concurrent.futures
import time
from datetime import datetime , timedelta
import difflib

int_y = "y"
network_list = ['10.0.0.0/8', '172.16.0.0/16', '192.168.0.0/16']

#active_hosts = {"active_ip_addrs": []}
#inactive_hosts = {"inactive_ip_addrs": []}
active_ip = []
inactive_ip = []
start_time = datetime.now()

for network in network_list:
    network = ipaddress.ip_network(network)
    hosts = network.hosts()

    def ping_f(ip_addr):
        try:
            subprocess.check_output(["ping", "-c", "1", ip_addr])
            active_ip.append(ip_addr)
        except:
            inactive_ip.append(ip_addr)


    executor = concurrent.futures.ThreadPoolExecutor(254)
    ping_hosts = [executor.submit(ping_f, str(ip)) for ip in hosts]

end_time = datetime.now()

d_1 = datetime.now().date()
d_2 = datetime.now().date() - timedelta(1)

f_1 = open(str(d_1)+'_active_ip.txt', "w")
for ip in active_ip:
    f_1.write(ip+"\n")
f_1.close()

with open(str(d_1)+'_active_ip.txt', "r") as f1:
    c_1 = f1.readlines()
with open(str(d_2)+'_active_ip.txt', "r") as f2:
    c_2 = f2.readlines()
for ip in c_2:
    if ip not in c_1:
        ip = ip[:-1]
        print(ip, " is New")
f1.close()
f2.close()

#json_active_hosts = json.dumps(active_hosts, indent=1)
#json_inactive_hosts = json.dumps(inactive_hosts, indent=1)
#print(active_ip, inactive_ip)
print(" Start  Time: ", start_time, "\n", "Finish Time: ", end_time)
