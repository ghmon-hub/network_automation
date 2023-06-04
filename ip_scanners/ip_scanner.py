
from www.codes.my_projects.db_functions.db_read_devices import db_rd_devices
import sys
sys.path.append("/var/www/")
from www.codes.my_projects.ip_scanners.ip_range import ip_adr
from www.codes.my_projects.ip_scanners.ip_reach import m_th_ip
from www.codes.my_projects.ip_scanners.port_scann import m_th_port
from www.codes.my_projects.ip_scanners.ssh_test import m_th_ssh_test
import socket
import time


def scanners_a(ip_a_1, subnet_a_1, community_a):
    #ip_a_1 = input('Please Enter a range or of IP management Network : ')
    ip_a_1 = socket.gethostbyname(ip_a_1)
    #subnet_a_1 = input('Please Enter The Subnet mask(default is 32) : ') or "32"
    #community_a = input('Please Enter The community string for SNMP : ') or "public"
    community_a = str(community_a)

    try:
        ip_list = (ip_adr(ip_a_1, subnet_a_1))
    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    try:
        ip_active = m_th_ip(ip_list)
    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    try:
        port_open = m_th_port(ip_active, community_a)
        time.sleep(10)
    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

    try:
        m_th_ssh_test(db_rd_devices()[0], db_rd_devices()[1])
    except KeyboardInterrupt:
        print("\n\n* Program aborted by user. Exiting...\n")
        sys.exit()

