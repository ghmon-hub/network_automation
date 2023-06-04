#Generate IP address

import ipaddress

ip_addr = []

def ip_adr(ip_a_1, subnet_a_1):
    if int(subnet_a_1) in range(1, 33):
        ip_b_1 = ip_a_1 + '/' + subnet_a_1
    else:
        subnet_a_1 = '32'
        ip_b_1 = ip_a_1 + '/' + '32'
    ip_a_2 = ipaddress.IPv4Network(ip_b_1)

    if int(subnet_a_1) == 32 or int(subnet_a_1) == 31 or int(subnet_a_1) == 0:
        for ip in ip_a_2:
            ip_addr.append(str(ip))
    else:
        for ip in ip_a_2:
            ip_addr.append(str(ip))
        ip_addr.pop(0)
        ip_addr.pop(-1)

    return ip_addr
