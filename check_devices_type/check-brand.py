import os
import sys
import glob


ssh_file = open('/root/codes/my_projects/ip_scanners/open_ssh_file.txt', 'r')

brand_file = '/root/codes/my_projects/ip_scanners/brands/*.txt'
files_brand = glob.glob(brand_file)

path_snmp = '/root/codes/my_projects/ip_scanners/snmp/*.txt'
files_snmp = glob.glob(path_snmp)

lines = ssh_file.readlines()


name_list_1 = []
name_list_2 = set()
num_len = ''
brand_names = ['Cisco', 'Fortinet', 'juniper', 'arista', 'paloalto', 'f5']

cisco = set()
fortinet = set()
juniper = set()
paloalto = set()
f5 = set()
arista = set()

#for ln in lines:
#    line = ln.split("\t")
#    name_list_1.append(line[0])

#num_len = len(name_list_1)

#for i in name_list_1:
#    n_f = i+".txt"
#    if n_f in snmp_file:
#        name_list_2.add(n_f)

#print(name_list_1, "\n", name_list_2)

for file in files_snmp:
    with open(file, "r") as f:
        lines = f.read()
        #print(lines)
        for br_nm in brand_names:
            if br_nm == 'cisco' or br_nm == 'Cisco' and br_nm in lines:
                outpt = open('/root/codes/my_projects/ip_scanners/brands/cisco/ip.txt', 'r+')
                output = outpt.read()
                file = file.split("/")
                name_out = file[-1][:-4]
                if name_out in output:
                    continue
                else:
                    outpt.write(name_out + "\n")
                    outpt.close()
            if br_nm == 'fortinet' or br_nm == 'Fortinet' and br_nm in lines:
                outpt = open('/root/codes/my_projects/ip_scanners/brands/fortinet/ip.txt', 'r+')
                output = outpt.read()
                file = file.split("/")
                name_out = file[-1][:-4]
                if name_out in output:
                    continue
                else:
                    outpt.write(name_out + "\n")
                    outpt.close()
            if br_nm == 'juniper' and br_nm in lines:
                outpt = open('/root/codes/my_projects/ip_scanners/brands/juniper/ip.txt', 'r+')
                output = outpt.read()
                file = file.split("/")
                name_out = file[-1][:-4]
                if name_out in output:
                    continue
                else:
                    outpt.write(name_out + "\n")
                    outpt.close()
            if br_nm == 'paloalto' and br_nm in lines:
                outpt = open('/root/codes/my_projects/ip_scanners/brands/paloalto/ip.txt', 'r+')
                output = outpt.read()
                file = file.split("/")
                name_out = file[-1][:-4]
                if name_out in output:
                    continue
                else:
                    outpt.write(name_out + "\n")
                    outpt.close()
            if br_nm == 'arista' and br_nm in lines:
                outpt = open('/root/codes/my_projects/ip_scanners/brands/arista/ip.txt', 'r+')
                output = outpt.read()
                file = file.split("/")
                name_out = file[-1]
                if name_out in output:
                    continue
                else:
                    outpt.write(name_out + "\n")
                    outpt.close()
            if br_nm == 'f5' and br_nm in lines:
                outpt = open('/root/codes/my_projects/ip_scanners/brands/f5/ip.txt', 'r+')
                output = outpt.read()
                file = file.split("/")
                name_out = file[-1][:-4]
                if name_out in output:
                    continue
                else:
                    outpt.write(name_out + "\n")
                    outpt.close()
            else:
                continue


#iso.3.6.1.2.1.47.1.2.1.1.2.1 fortinet
#iso.3.6.1.2.1.1.1.0 cisco

#Find version of devices
with open('/root/codes/my_projects/ip_scanners/brands/cisco/ip.txt', "r") as f:
    all_data = f.readlines()
    for line in all_data:
        line = line[:-1]
        with open('/root/codes/my_projects/ip_scanners/snmp/'+line+'.txt', 'r') as l_1:
            l_1 = l_1.readlines()
            for snmp_l in l_1:
                if 'iso.3.6.1.2.1.1.1.0. OCTETSTR =' in snmp_l:
                    with open('/root/codes/my_projects/ip_scanners/brands/cisco/version.txt', "a") as v:
                        v.write(line + "\t" + (snmp_l.split('= '))[1])
                else:
                    continue

with open('/root/codes/my_projects/ip_scanners/brands/fortinet/ip.txt', "r") as f:
    all_data = f.readlines()
    for line in all_data:
        line = line[:-1]
        with open('/root/codes/my_projects/ip_scanners/snmp/' + line + '.txt', 'r') as l_1:
            l_1 = l_1.readlines()
            for snmp_l in l_1:
                if 'iso.3.6.1.2.1.47.1.2.1.1.2.1. OCTETSTR =' in snmp_l:
                    with open('/root/codes/my_projects/ip_scanners/brands/fortinet/version.txt', "a") as v:
                        v.write(line+ "\t" +(snmp_l.split('= '))[1])
                else:
                    continue
