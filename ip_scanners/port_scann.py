import sys
import os
import socket
import threading
import easysnmp
from easysnmp import Session
from www.codes.my_projects.db_functions.db_in_devices import db_upd_in
from www.codes.my_projects.check_devices_type.check_brands import ch_br


threads = []
open_snmp_dir = '/var/www/codes/my_projects/ip_scanners/snmp/'
open_ssh_file = open('/var/www/codes/my_projects/ip_scanners/open_ssh_file.txt', 'w')


def p_scan(ip, community_a):
    # Print a nice banner with information on which host we are about to scan
    #print("-" * 60)
    #print("Please wait, scanning remote host", ip)
    #print("-" * 60, "\n")
    db_el = []
    db_el.insert(1, ip)
    db_el.insert(5, community_a)

    try:

        for port in (22, 161):
            if port == 22:

                sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result_tcp = sock_tcp.connect_ex((ip, port))

                if result_tcp == 0:
                    #print("Port {}: 	 Open".format(port), "\n")
                    #open_ssh_file.write("-" * 60)
                    #open_ssh_file = open('/root/codes/my-projects/ip_scanners/open_ssh_file.txt', '+w')
                    #open_ssh_file.write(str(ip) + "\t" + str(port) + "\n")
                    db_el.insert(2,port)
                    #open_ssh_file.close()
                    #open_ssh_file.write("-" * 60)
                    sock_tcp.close()
                else:
                    db_el.insert(2, '')

            elif port == 161:
                # ip = input('\nEnter the device IP address: ')
                oid_1 = 'iso.3.6.1.2.1.1.1.0'

                # Opening the SNMPv3 session to the device
                # session = Session(hostname = ip, version = 3, security_level = "auth_with_privacy", security_username = "mihai", auth_protocol = "SHA", auth_password = "shapass1234", privacy_protocol = "AES", privacy_password = "aespass1234")
                session = Session(hostname=ip, community=community_a, version=2)
                oid_out_1 = session.get(oid_1)
                result_1 = oid_out_1.value

                if oid_out_1:
                    #print("Port {}: 	 Open".format(port), "\n")
                    db_el.insert(3, port)
                    #file_name_1 = ip + ".txt"
                    #file_name_2 = os.path.join(open_snmp_dir, file_name_1)
                    #open_snmp_file = open(file_name_2, 'w')

                    #open_snmp_file.write("-" * 60)
                    oid_walk = session.bulkwalk()
                    data_snmp = []
                    for item in oid_walk:
                        data_snmp.append('{oid}.{oid_index} {snmp_type} = {value}'.format(oid=item.oid, oid_index=item.oid_index, snmp_type=item.snmp_type, value=item.value))
                    ch_br(ip, data_snmp)
                    #open_snmp_file.write(ip + "\t" + community_a + "\t" + str(result_1) + "\n")
                    #for item in oid_walk:
                        #open_snmp_file.write('{oid}.{oid_index} {snmp_type} = {value}'.format(oid=item.oid, oid_index=item.oid_index, snmp_type=item.snmp_type, value=item.value)+"\n")
                    #open_snmp_file.write("-" * 60)

    # except KeyboardInterrupt:
    #    print("TCP : You pressed Ctrl+C")
    #    sys.exit()

    # except socket.gaierror:
    #    print('TCP : Hostname could not be resolved. Exiting')
    #    sys.exit()

    except socket.error:
        #print("TCP : Couldn't connect to server", "\n")
        db_el.insert(2, '')
        #sys.exit()

    except SystemError:
        #print("Port {}: 	 Close".format('SNMP'), "\n")
        db_el.insert(3, '')
        #sys.exit()

    except easysnmp.exceptions.EasySNMPUnknownObjectIDError:
        #print("oid is wrong", "\n")
        db_el.insert(3, '')
        #sys.exit()

    except easysnmp.exceptions.EasySNMPTimeoutError:
        #print(ip, "Port {}: 	 Close".format('SNMP'), "\n")
        db_el.insert(3, '')
        #sys.exit()

    db_upd_in(db_el[0], db_el[2], db_el[3], db_el[1])


def m_th_port(ip_addr, community_a):
    for ip in ip_addr:
        th = threading.Thread(target=p_scan, args=(ip, community_a))  # args is a tuple with a single element
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    open_ssh_file.close()