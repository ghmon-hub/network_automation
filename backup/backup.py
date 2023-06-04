import netmiko
import time
import datetime
#from colorama import init
#from colorama import Fore
#import sys
import threading

from www.codes.my_projects.db_functions.db_in_backup import db_backup_in
from www.codes.my_projects.db_functions.db_in_backup import db_backup_rt
from www.codes.my_projects.db_functions.db_in_hostname import db_host_in
from www.codes.my_projects.db_functions.db_in_backup import db_backup_vrf
from www.codes.my_projects.data_gathering.collect_route import vrf_vdom_list
from www.codes.my_projects.connection_module.ssh_m import ssh_m_show

threads = []
forti_list = set()
forti_r_list = set()
csc_list = set()
csc_r_list = set()
juni_list = set()
juni_r_list = set()
csc_v_list = set()
output_csc_rt = str()

def ssh_back(ip, username, password, brand, os_version, domain_name):
    if brand == 'Cisco':
        d_type = 'cisco_ios'
        cmd_1 = 'show runn'
        cmd_2 = 'show running | in hostname'
        cmd_3 = 'show ip vrf'
        output_1 = ssh_m_show(ip, username, password, d_type, cmd_1)
        output_2 = ssh_m_show(ip, username, password, d_type, cmd_2)
        output_3 = ssh_m_show(ip, username, password, d_type, cmd_3)
        host_dev = output_2.replace('hostname ', "")
        time_act = str(datetime.datetime.now()).replace(" ", "_")
        time_act = time_act[:-7]
        db_backup_in(ip, time_act, output_1, brand)
        db_host_in(ip, host_dev, domain_name)
        db_backup_vrf(ip, time_act, output_3, brand)
        name_v = 'vrf_' + brand + "_" + ip + "_" + time_act + ".txt"
        name_f = brand+"_"+ip+"_"+time_act+".txt"
        csc_list.add(name_f)
        csc_v_list.add(name_v)

    if brand == 'Juniper':
        d_type = 'juniper'
        cmd_1 = 'show configuration'
        cmd_2 = 'show route'
        cmd_3 = 'show configuration | grep host-name'
        output_1 = ssh_m_show(ip, username, password, d_type, cmd_1)
        output_2 = ssh_m_show(ip, username, password, d_type, cmd_2)
        output_3 = ssh_m_show(ip, username, password, d_type, cmd_3)
        host_dev = output_3.split("\n")
        if len(host_dev) <= 1:
            host_dev_1 = ""
        else:
            host_dev_1 = host_dev[1].replace("hostname", "")
            host_dev_1 = host_dev_1.replace(":", "")
            host_dev_1 = host_dev_1.replace(" ", "")
        host_dev_1 = host_dev[1].replace('host-name', "")
        host_dev_1 = host_dev_1.replace(";", "")
        host_dev_1 = host_dev_1.replace(" ", "")
        time_act = str(datetime.datetime.now()).replace(" ", "_")
        time_act = time_act[:-7]
        db_backup_in(ip, time_act, output_1, brand)
        db_host_in(ip, host_dev_1, domain_name)
        db_backup_rt(ip, time_act, output_2, brand)
        name_r = 'rt_' + brand + "_" + ip + "_" + time_act + ".txt"
        name_f = brand + "_" + ip + "_" + time_act + ".txt"
        juni_list.add(name_f)
        juni_r_list.add(name_r)

    if brand == 'Fortinet':
        d_type = 'fortinet'
        cmd_1 = 'show full-configuration'
        cmd_2 = 'get router info routing-table all'
        cmd_3 = 'get system global | grep hostname'
        output_1 = ssh_m_show(ip, username, password, d_type, cmd_1)
        output_2 = ssh_m_show(ip, username, password, d_type, cmd_2)
        output_3 = ssh_m_show(ip, username, password, d_type, cmd_3)
        host_dev = output_3.split("\n")
        if len(host_dev) <= 1:
            host_dev_1 = ""
        else:
            host_dev_1 = host_dev[1].replace("hostname", "")
            host_dev_1 = host_dev_1.replace(":", "")
            host_dev_1 = host_dev_1.replace(" ", "")
        time_act = str(datetime.datetime.now()).replace(" ", "_")
        time_act = time_act[:-7]
        db_backup_in(ip, time_act, output_1, brand)
        db_host_in(ip, host_dev_1, domain_name)
        db_backup_rt(ip, time_act, output_2, brand)
        name_r = 'rt_' + brand + "_" + ip + "_" + time_act + ".txt"
        name_f = brand + "_" + ip + "_" + time_act + ".txt"
        forti_list.add(name_f)
        forti_r_list.add(name_r)

def csc_rt_bk (ip, username, password, brand, os_version, vrf_list):
    if brand == 'Cisco':
        d_type = 'cisco_ios'
        cmd_1 = 'show ip route'
        output_1 = "routing"+"\n"+ssh_m_show(ip, username, password, d_type, cmd_1)
        for vrf_l in vrf_list:
            if ip in vrf_l:
                vrf_name = vrf_vdom_list(vrf_l)
                if not vrf_name:
                    #print(vrf_name, "Nothing here", vrf_l)
                    break
                else:
                    for vrf in vrf_name:
                        #print(vrf_name, ip)
                        cmd_2 = 'show ip route vrf '+vrf
                        outputs = ssh_m_show(ip, username, password, d_type, cmd_2)
                        output_1 = output_1+"\n"+"routing"+"\n"+outputs
        time_act = str(datetime.datetime.now()).replace(" ", "_")
        time_act = time_act[:-7]
        name_r = 'rt_' + brand + "_" + ip + "_" + time_act + ".txt"
        csc_r_list.add(name_r)
        db_backup_rt(ip, time_act, output_1, brand)


def m_th_ssh_b(active_ip, usr, passwd, brands, os_version, domain_name):

    loop_b = len(active_ip)
    for i in range(0, loop_b):
        th = threading.Thread(target=ssh_back, args=(active_ip[i], usr[i], passwd[i], brands[i], os_version[i], domain_name))  # args is a tuple with a single element
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
    #time.sleep(10)
    return csc_list, forti_list, juni_list, forti_r_list, juni_r_list, csc_v_list


def m_th_ssh_a(active_ip, usr, passwd, brands, os_version, csc_vrf_list):

    loop_a = len(active_ip)
    for i in range(0, loop_a):
        th = threading.Thread(target=csc_rt_bk, args=(active_ip[i], usr[i], passwd[i], brands[i], os_version[i], csc_vrf_list))  # args is a tuple with a single element
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
    #time.sleep(10)
    return csc_r_list