import datetime
from ciscoconfparse import CiscoConfParse
import ipaddress
import re
from colorama import init
from colorama import Fore
import sys
import threading


def vrf_vdom_list(csc_vrf_list):
    path = "/var/www/codes/my_projects/backup/bk/"
    ip_i = csc_vrf_list.replace("vrf_Cisco_", "")
    ip_i = ip_i[:-24]
    with open(path + csc_vrf_list, "r") as f_1:
        file_1 = f_1.read()
        file_1 = file_1.split("\n")
        vrf_name_list = []
        file_f = list(filter(None, file_1))
        if not file_f:
            vrf_name_list = []
        else:
            file_f.pop(0)
            for i in file_f:
                vrf_n = i.lstrip()
                vrf_n = vrf_n.split(" ")
                vrf_name_list.append(vrf_n[0])
    return vrf_name_list


def route_find(cs_rt_list, forti_rt_list, juni_rt_list):
    path = "/var/www/codes/my_projects/backup/bk/"
    for f_c in cs_rt_list:
        ip_i = f_c.replace("rt_Cisco_", "")
        ip_i = ip_i[:-24]
        with open(path + f_c, "r") as f_1:
            f_1 = f_1.read()
            f_1 = f_1.split('routing')
            for el in f_1:
                el = el.split("\n")
                vrf_name = el[0]
                el = el[1:10]
                pass
                #print(el, vrf_name)

    for f_f in forti_rt_list:
        ip_i = f_f.replace("rt_Fortinet_", "")
        ip_i = ip_i[:-24]
        with open(path + f_f, "r") as f_1:
            f_1 = f_1.read()
            f_1 = f_1.split('Routing table for VRF=')
            for el in f_1:
                pass
                #print('ok')

    for f_j in juni_rt_list:
        ip_i = f_j.replace("rt_Juniper_", "")
        ip_i = ip_i[:-24]
        with open(path + f_j, "r") as f_1:
            f_1 = f_1.readlines()
            pass
            #print(f_1, ip_i)