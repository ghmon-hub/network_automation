import os
import sys
from www.codes.my_projects.db_functions.db_br_devices import db_upd_in

brand_names = ['Cisco', 'Fortinet', 'juniper', 'arista', 'paloalto', 'f5']
cisco = set()
fortinet = set()
juniper = set()
paloalto = set()
f5 = set()
arista = set()

#iso.3.6.1.2.1.47.1.2.1.1.2.1. OCTETSTR = ' fortinet
#'iso.3.6.1.2.1.1.1.0. OCTETSTR = ' cisco
#iso.1.3.6.1.2.1.25.6.3.1.2 OCTETSTR = ' Juniper

def ch_br(ip,snmp_data):
    for d in snmp_data:
        if ('iso.3.6.1.2.1.1.1.0. OCTETSTR =' in d) and ('Cisco' in d):
            d = d.split("= ")
            db_upd_in(ip, d[1], 'Cisco')

        if ('iso.3.6.1.2.1.47.1.2.1.1.2.1' in d) and ('Fortinet' in d):
            d = d.split("= ")
            db_upd_in(ip, d[1], 'Fortinet')

        if ('iso.1.3.6.1.2.1.25.6.3.1.2' in d) and ('JUNOS' in d) or ('iso.3.6.1.2.1.54.1.1.1.1.4.2' in d) and ('JUNOS' in d):
            d = d.split("= ")
            db_upd_in(ip, d[1], 'Juniper')

