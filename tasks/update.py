import time
import threading
import ftplib
import ftputil
import fnmatch
from www.codes.my_projects.connection_module.ssh_m import ssh_m_show

def up_os(brand, addr_dev, dev_type, addr_l, path_f, server_addr, username, passwd):
    adr_ok = []
    adr_not = []
    if brand == 'Cisco':
        host = ftputil.FTPHost(server_addr, username, passwd)
        fu_pa = host.path.join(path_f)
        size = host.path.getsize(fu_pa)
        cmd = 'show version | in IOS'
        a_d = ssh_m_show(addr_l, 'admin', 'CiscoCisco', 'cisco_ios', cmd)
        print(a_d)
        d_o = a_d.split(" ")
        if str(size) < str(d_o[0]):
            a_s = addr_l+","+d_o[0]
            adr_ok.append(a_s)
        else:
            a_s = addr_l+","+d_o[0]
            adr_not.append(a_s)
    return adr_ok, adr_not


print(up_os('Cisco', '192.168.0.8', 'router', '192.168.0.80', '/home/gh/Pictures/easysnmp-0.2.5.tar.gz', '192.168.0.8', 'gh', '12345678'))
