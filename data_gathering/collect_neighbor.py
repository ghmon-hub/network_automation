import netmiko
import time
import datetime
from ciscoconfparse import CiscoConfParse
import ipaddress
import re
from colorama import init
from colorama import Fore
import sys
import threading
from www.codes.my_projects.db_functions.db_in_backup import db_backup_nei
from www.codes.my_projects.db_functions.db_in_neighbor import db_nei_device
from www.codes.my_projects.db_functions.db_int_device_rd import db_rd_int_device

threads = []
name_fg_nei = []
name_cs_nei = []
name_ju_nei = []

def ssh_nei(ip, username, password, brand, os_version):
    if brand == 'Cisco':
        devices = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': username,
            'password': password,
            'port': 22,
                    }
        try:
            ssh_b = netmiko.ConnectHandler(**devices)
            ssh_b.find_prompt()
            # ssh_t.establish_connection()
        except netmiko.ssh_exception.NetMikoTimeoutException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        except netmiko.ssh_exception.NetMikoAuthenticationException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        else:
            # connection was established successfully
            # print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            cmd_list = [
                "config terminal",
                "lldp run",
                "end",
            ]
            output_1 = ssh_b.send_config_set(cmd_list)
            return output_1, ssh_b.disconnect()


    if brand == 'Juniper':
        devices = {
            'device_type': 'juniper',
            'host': ip,
            'username': username,
            'password': password,
            'port': 22,
        }
        try:
            ssh_b = netmiko.ConnectHandler(**devices)
            # ssh_t.establish_connection()
        except netmiko.ssh_exception.NetMikoTimeoutException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        except netmiko.ssh_exception.NetMikoAuthenticationException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        else:

            # connection was established successfully
            # print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            cmd_list = [
                "cli",
                "confiure",
                "set protocol lldp",
                "set interface all",
                "commmit",
                "end"
            ]
            output_1 = ssh_b.send_command(cmd_list)
            return output_1, ssh_b.disconnect()

    if brand == 'Fortinet':
        devices = {
            'device_type': 'fortinet',
            'host': ip,
            'username': username,
            'password': password,
            'port': 22,
        }
        try:
            ssh_b = netmiko.ConnectHandler(**devices)
            # ssh_t.establish_connection()
        except netmiko.ssh_exception.NetMikoTimeoutException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        except netmiko.ssh_exception.NetMikoAuthenticationException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        else:

            # connection was established successfully
            # print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            cmd_list = [
                "config system global",
                "set lldp-trans enable",
                "end",
            ]
            #output_1 = ssh_b.send_config_set(cmd_list)
            #ssh_b.send_config_set(cmd_list)
            #ssh_b.disconnect()
            #output_2 = ()
            #cmd_list_in = []
            for inter_l in db_rd_int_device(ip):
                #print(inter_l, ip)
                cmd_list.append("config system interface")
                cmd_list.append("edit " + inter_l)
                cmd_list.append("set device-identification enable")
                cmd_list.append("set lldp-transmission enable")
                cmd_list.append("end")
            #output_2 = ssh_b.send_config_set(cmd_list_in)
            ssh_b.send_config_set(cmd_list)
            ssh_b.disconnect()
            #return output_1, output_2 , ssh_b.disconnect()


def nei_file(ip, username, password, brand, os_version):
    if brand == 'Cisco':
        devices = {
            'device_type': 'cisco_ios',
            'host': ip,
            'username': username,
            'password': password,
            'port': 22,
                    }
        try:
            ssh_b = netmiko.ConnectHandler(**devices)
            ssh_b.find_prompt()
            # ssh_t.establish_connection()
        except netmiko.ssh_exception.NetMikoTimeoutException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        except netmiko.ssh_exception.NetMikoAuthenticationException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        else:
            # connection was established successfully
            # print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            output_1 = ssh_b.send_command("show lldp neighbor")
            time_act = str(datetime.datetime.now()).replace(" ", "_")
            time_act = time_act[:-7]
            db_backup_nei(ip, time_act, output_1, brand)
            name_f = "nei_"+brand+"_"+ip+"_"+time_act+".txt"
            name_cs_nei.append(name_f)
            return output_1, ssh_b.disconnect()


    if brand == 'Juniper':
        devices = {
            'device_type': 'juniper',
            'host': ip,
            'username': username,
            'password': password,
            'port': 22,
        }
        try:
            ssh_b = netmiko.ConnectHandler(**devices)
            # ssh_t.establish_connection()
        except netmiko.ssh_exception.NetMikoTimeoutException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        except netmiko.ssh_exception.NetMikoAuthenticationException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        else:

            # connection was established successfully
            # print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            cmd_list = [
                "cli",
                "show lldp neighbor",
            ]
            output_1 = ssh_b.send_config_set(cmd_list)
            time_act = str(datetime.datetime.now()).replace(" ", "_")
            time_act = time_act[:-7]
            db_backup_nei(ip, time_act, output_1, brand)
            name_f = "nei_"+brand+"_"+ip+"_"+time_act+".txt"
            name_ju_nei.append(name_f)
            return output_1, ssh_b.disconnect()

    if brand == 'Fortinet':
        devices = {
            'device_type': 'fortinet',
            'host': ip,
            'username': username,
            'password': password,
            'port': 22,
        }
        try:
            ssh_b = netmiko.ConnectHandler(**devices)
            # ssh_t.establish_connection()
        except netmiko.ssh_exception.NetMikoTimeoutException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        except netmiko.ssh_exception.NetMikoAuthenticationException:
            # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            time.sleep(1)
        else:

            # connection was established successfully
            # print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
            output_1 = ssh_b.send_command("diagnose user device list")
            time_act = str(datetime.datetime.now()).replace(" ", "_")
            time_act = time_act[:-7]
            db_backup_nei(ip, time_act, output_1, brand)
            name_f = "nei_"+brand+"_"+ip+"_"+time_act+".txt"
            name_fg_nei.append(name_f)
            return output_1, ssh_b.disconnect()

def col_nei(n_cs_nei, n_ju_nei, n_fg_nei):
    path = "/var/www/codes/my_projects/backup/bk/"
    for file in n_fg_nei:
        ip_i = file.replace("nei_Fortinet_", "")
        ip_i = ip_i[:-24]
        with open(path+file, "r") as f:
            all_file = f.readlines()
            all_1 = str(all_file).split("vd")
        for i in all_1:
            if 'lldp' in i:
                nei_host = 'none'
                l_port = 'none'
                i = i.split(",")
                for j in i:
                    if 'host' in j:
                        j = j.rstrip()
                        j = j.lstrip()
                        j = j.split(" ")
                        index_1 = j.index('host')
                        nei_host = j[index_1 + 1].replace("'", "")
                    if 'port' in j:
                        j = j.rstrip()
                        j = j.lstrip()
                        j = j.split(" ")
                        for i in j:
                            if 'port' in i:
                                l_port = i
                db_nei_device(ip_i, l_port, nei_host)

    for file in n_cs_nei:
        lst_j = []
        index_f = int()
        num_n = int()
        ip_i = file.replace("nei_Cisco_", "")
        ip_i = ip_i[:-24]
        with open(path+file, "r") as f:
            all_file = f.readlines()
        for i in all_file:
            if 'Device ID' in i:
                index_f = all_file.index(i)
            if 'Total entries displayed: ' in i:
                num_n = i.replace("Total entries displayed: ", "")
            for j in range(int(index_f) + 1, int(index_f) + int(num_n) + 1):
                lst_j = (all_file[j]).split(" ")
                while ("" in lst_j):
                    lst_j.remove("")
                db_nei_device(ip_i, lst_j[1],lst_j[0])

    for file in n_ju_nei:
        index_f = int()
        list_n = []
        ip_i = file.replace("nei_Juniper_", "")
        ip_i = ip_i[:-24]
        with open(path+file, "r") as f:
            all_file = f.readlines()
            # all_1 = str(all_file).split("\n")
            len_f = len(all_file)
        for i in all_file:
            if 'Local Interface' in i:
                index_f = all_file.index(i)
        for j in range(index_f + 1, len_f):
            list_n = all_file[j].split(" ")
            while ("" in list_n):
                list_n.remove("")
            while ('-' in list_n):
                list_n.remove('-')
            db_nei_device(ip_i, list_n[0], list_n[3])

def m_th_ssh_nei(active_ip, usr, passwd, brands, os_version):

    loop_1 = len(active_ip)
    for i in range(0, loop_1):
        th = threading.Thread(target=ssh_nei, args=(active_ip[i], usr[i], passwd[i], brands[i], os_version[i]))  # args is a tuple with a single element
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
    #time.sleep(10)

def m_th_nei_file(active_ip, usr, passwd, brands, os_version):
    loop_1 = len(active_ip)
    for i in range(0, loop_1):
        th = threading.Thread(target=nei_file, args=(active_ip[i], usr[i], passwd[i], brands[i], os_version[i]))  # args is a tuple with a single element
        th.start()
        threads.append(th)
    for th in threads:
        th.join()
    # time.sleep(10)
    return name_fg_nei, name_cs_nei, name_ju_nei
