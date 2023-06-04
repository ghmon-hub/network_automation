import psycopg2

def db_rd_devices():
    active_ip = []
    brand_list = []
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT ip_addr, ssh_port, brand from devices")
    rows = cur.fetchall()

    for row in rows:
        if row[1] == '22':
            active_ip.append(row[0])
            brand_list.append(row[2])
        else:
            continue

    con.close()
    return active_ip, brand_list

def db_rd_devices_qt():
    active_ip = []
    brand_list = []
    os_version = []
    host_name = []
    domain_nme = []
    user_name = []
    password = []
    dev_type = []
    dev_loc = []
    dev_role = []

    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT ip_addr, brand, os_version, hostname, domain_name, usr, passwd, dev_type, dev_loc, dev_role from devices")
    rows = cur.fetchall()

    for row in rows:
        active_ip.append(row[0])
        brand_list.append(row[1])
        os_version.append(row[2])
        host_name.append(row[3])
        domain_nme.append(row[4])
        user_name.append(row[5])
        password.append(row[6])
        dev_type.append(row[7])
        dev_loc.append(row[8])
        dev_role.append(row[9])

    con.close()
    return active_ip, brand_list, os_version, host_name, domain_nme, user_name, password, dev_type, dev_loc, dev_role
