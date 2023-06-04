import netmiko
import time
import datetime

def ssh_m_show(ip, username, password, d_type, cmd):
    output = str()
    devices = {
            'device_type': d_type,
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
    except netmiko.ssh_exception.SSHException:
        # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        time.sleep(1)
    else:
        # connection was established successfully
        # print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
        # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
        output = ssh_b.send_command(cmd)
    return output

def ssh_m_test(ip, username, password, d_type):
    output = str()
    devices = {
            'device_type': d_type,
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
    except netmiko.ssh_exception.SSHException:
        # print(f"{RED}[+] Wrong credential:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        time.sleep(1)
    else:
        # connection was established successfully
        # print(f"{GREEN}[+] Found combo:\n\tHOSTNAME: {ip}\n\tUSERNAME: {username}\n\tPASSWORD: {password}{RESET}")
        # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
        # user_pass_ssh_file.write(ip + "\t" + username + "\t" + password + "\n")
        ssh_b.disconnect()
        return ip, username, password
