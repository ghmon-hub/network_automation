import datetime
from ciscoconfparse import CiscoConfParse
import ipaddress
import re
from colorama import init
from colorama import Fore
import sys
import threading
from www.codes.my_projects.db_functions.db_int_device_in import db_ne_l3_in

threads = []


def inter_find(csc_list, forti_list, juni_list):
    path = "/var/www/codes/my_projects/backup/bk/"
    for file in csc_list:
        int_i = 'none'
        ip_a = 'none'
        ip_m = 'none'
        ip_br = 'none'
        dup_a = 'none'
        sp_a = 'none'
        p_srv = 'none'
        p_acl = 'none'
        ip_sec = 'none'
        src_a = 'none'
        dst_a = 'none'
        ip_i = file.replace("Cisco_", "")
        ip_i = ip_i[:-24]
        con_par = CiscoConfParse(path+file)
        int_cmds = con_par.find_objects(r"^interface ")
        for obj in int_cmds:
            out_1 = str({obj.text: [child.text.strip() for child in obj.children]})
            out_1 = out_1.replace(":", ",")
            out_1 = out_1.replace("[", "")
            out_1 = out_1.replace("]", "")
            out_1 = out_1.replace("{", "")
            out_1 = out_1.replace("}", "")
            out_1 = out_1.split(",")
            for i in out_1:
                if 'interface' in i:
                    int_i = i.replace('interface', '')
                    int_i = int_i.replace("'", "")
                if 'FastEthernet' in i:
                    sp_a = '100M'
                elif 'Gig' in i:
                    sp_a = '1G'
                if 'tunnel protection ipsec profile' in i:
                    i.replace("tunnel protection ipsec profile", "")
                    ip_sec = i
                if 'tunnel source' in i:
                    i = i.replace("tunnel source ", "")
                    src_a = i
                if 'tunnel destination' in i:
                    i = i.replace("tunnel destination ", "")
                    dst_a = i
                if 'no ip address' in i:
                    ip_a = 'none'
                elif 'ip address' in i:
                    ip_a = i.replace("ip address", "")
                    ip_a = ip_a.replace("'", "")
                    ip_a = ip_a.lstrip()
                    if '/' in ip_a:
                        ip_id = ip_a.split("/")
                    else:
                        ip_id = ip_a.split(" ")
                    # ip_1 = IPNetwork(ip_id[0], ip_id[1])
                    IP = ip_id[0]
                    MASK = ip_id[1]
                    if IP == '0.0.0.0':
                        ip_a = 'none'
                        ip_m = 'none'
                        ip_br = 'none'
                    else:
                        host = ipaddress.IPv4Address(IP)
                        net = ipaddress.IPv4Network(IP + '/' + MASK, False)
                        ip_a = ip_id[0]
                        ip_m = ipaddress.IPv4Address(int(host) & int(net.netmask))
                        ip_br = net.broadcast_address
                elif 'ip unnumbred' in i:
                    ip_a = i.replace("ip address", "")
                if 'duplex' in i:
                    dup_a = i.replace("duplex ", "")
                else:
                    continue
                if 'service-policy' in i:
                    i.replace("service-policy", "")
                    p_srv = i
                else:
                    continue
                if 'ip access-group' in i:
                    i.replace("ip access-group", "")
                    p_acl = i
                else:
                    continue
            db_ne_l3_in(ip_i, ip_m, ip_br, ip_a, int_i, sp_a, p_srv, p_acl, ip_sec, src_a, dst_a, dup_a)

    for file in forti_list:
        index_n = []
        int_i = 'none'
        ip_a = 'none'
        ip_m = 'none'
        ip_br = 'none'
        dup_a = 'none'
        sp_a = 'none'
        p_srv = 'none'
        p_acl = 'none'
        ip_sec = 'none'
        src_a = 'none'
        dst_a = 'none'
        ip_i = file.replace("Fortinet_", "")
        ip_i = ip_i[:-24]
        con_par = CiscoConfParse(path + file)
        int_cmds = con_par.find_all_children(r"^config system interface")
        index_1 = len(int_cmds)
        for obj in int_cmds:
            if 'edit' in obj:
                index_n.append(int_cmds.index(obj))
        index_n.append(index_1)
        for num_1 in range (0, len(index_n) - 1):
            for num_2 in range (index_n[num_1], index_n[num_1+1]):
                content_1 = (int_cmds[num_2])
                if 'set ip ' in content_1:
                    ip_a = content_1.replace("set ip ", "")
                    #ip_a = ip_a.replace("'", "")
                    ip_a = ip_a.lstrip()
                    ip_id = re.split('\s', ip_a)
                    # ip_1 = IPNetwork(ip_id[0], ip_id[1])
                    IP = ip_id[0]
                    MASK = ip_id[1]
                    if IP == '0.0.0.0':
                        ip_a = 'none'
                        ip_m = 'none'
                        ip_br = 'none'
                    else:
                        host = ipaddress.IPv4Address(IP)
                        net = ipaddress.IPv4Network(IP + '/' + MASK, False)
                        ip_a = ip_id[0]
                        ip_m = ipaddress.IPv4Address(int(host) & int(net.netmask))
                        ip_br = net.broadcast_address
                if 'set speed ' in content_1:
                    sp_a = content_1.replace("set speed ", "")
                if 'edit ' in content_1:
                    int_i = content_1.replace('edit ', "")
                    int_i = int_i.replace('"', "")
            db_ne_l3_in(ip_i, ip_m, ip_br, ip_a, int_i, sp_a, p_srv, p_acl, ip_sec, src_a, dst_a, dup_a)

    for file in juni_list:
        ip_a = 'none'
        ip_m = 'none'
        ip_br = 'none'
        dup_a = 'none'
        sp_a = 'none'
        p_srv = 'none'
        p_acl = 'none'
        ip_sec = 'none'
        src_a = 'none'
        dst_a = 'none'
        ip_i = file.replace("Juniper_", "")
        ip_i = ip_i[:-24]
        con_par = CiscoConfParse(path + file)
        int_cmds = con_par.find_all_children(r"^interface")
        len_int = len(int_cmds)
        int_i = int_cmds[1].replace("{", '')
        for obj in int_cmds:
            obj_1 = str(obj)
            obj_2 = obj_1.replace("{", "")
            obj_3 = obj_2.replace("}", "")
            obj_4 = obj_3.replace(";", "")
            obj_5 = obj_4.replace(" ", "")
            obj_6 = obj_5.replace("unit", "")
            if 'address' in obj_6:
                ip_a = obj_6.replace("address", "")
                ip_id = re.split("/", ip_a)
                IP = ip_id[0]
                MASK = ip_id[1]
                if IP == '0.0.0.0':
                    ip_a = 'none'
                    ip_m = 'none'
                    ip_br = 'none'
                else:
                    host = ipaddress.IPv4Address(IP)
                    net = ipaddress.IPv4Network(IP + '/' + MASK, False)
                    ip_a = ip_id[0]
                    ip_m = ipaddress.IPv4Address(int(host) & int(net.netmask))
                    ip_br = net.broadcast_address
        db_ne_l3_in(ip_i, ip_m, ip_br, ip_a, int_i, sp_a, p_srv, p_acl, ip_sec, src_a, dst_a, dup_a)