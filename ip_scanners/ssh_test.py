import netmiko
import time
from colorama import init
from colorama import Fore
import sys
import threading
from www.codes.my_projects.db_functions.db_in_credentials import db_upd_in
from www.codes.my_projects.connection_module.ssh_m import ssh_m_test


threads = []

usr = ['admin', 'root']
pas = ['CiscoCisco', 'cisco']

user_pass_ssh_file = open('/var/www/codes/my_projects/ip_scanners/user-pass.txt', '+w')

# Clear the screen
#subprocess.call('clear', shell=True)
# Ask for input
#remoteServer = input("Enter a remote host to scan: ")

# initialize colorama
init()
GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET
BLUE = Fore.BLUE


def ssh_test(ip, username, password, brand):
    # initialize SSH client
    if brand == 'Cisco':
        d_type = 'cisco_ios'
        output_test = ssh_m_test(ip, username, password, d_type)
        if not output_test:
            #print(output_test)
            pass
        else:
            db_upd_in(output_test[0], output_test[1],output_test[2])


    if brand == 'Fortinet':
        d_type = 'fortinet'
        output_test = ssh_m_test(ip, username, password, d_type)
        if not output_test:
            #print(output_test)
            pass
        else:
            db_upd_in(output_test[0], output_test[1], output_test[2])


    if brand == 'Juniper':
        d_type = 'juniper'
        output_test = ssh_m_test(ip, username, password, d_type)
        if not output_test:
            #print(output_test)
            pass
        else:
            db_upd_in(output_test[0], output_test[1], output_test[2])


    if brand == 'linux' or '':
        d_type = 'juniper'
        output_test = ssh_m_test(ip, username, password, d_type)
        if not output_test:
            #print(output_test)
            pass
        else:
            db_upd_in(output_test[0], output_test[1], output_test[2])


def m_th_ssh_test(active_ip, brands):
    len_ip = len(active_ip)
    len_br = len(brands)
    for username in usr:
        for password in pas:
            for num_r in range (0, len_ip):
                ip = active_ip[num_r]
                brand = brands[num_r]
                th = threading.Thread(target=ssh_test,args=(ip, username, password, brand))  # args is a tuple with a single element
                th.start()
                threads.append(th)
            for th in threads:
                th.join()
            time.sleep(10)