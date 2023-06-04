import subprocess
import threading
import time
import datetime

active_ip = []
threads = []


def a_ip(ip):
    result = subprocess.Popen(["ping", "-c", "1", "-n",    ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE).wait()
    if result == 0:
        active_ip.append(ip)


def m_th_ip(ip_addr):
    for ip in ip_addr:
        th = threading.Thread(target=a_ip, args=(ip,))  # args is a tuple with a single element
        th.start()
        threads.append(th)

    for th in threads:
        th.join()

    return active_ip
