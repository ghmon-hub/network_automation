import psycopg2

def db_upd_in(ip, ssh, snmp, snmp_community):
    ip_list = set()
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    #print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT ip_addr from devices")
    rows = cur.fetchall()
    for row in rows:
        ip_list.add(row[0])
    if ip in ip_list:
        cur.execute("UPDATE devices set ssh_port=%s, snmp_port=%s, snmp_community=%s where ip_addr=%s", (str(ssh), str(snmp), str(snmp_community), str(ip)))
        con.commit()
        con.close()
    else:
        cur.execute("INSERT INTO devices (ip_addr, ssh_port, snmp_port, snmp_community) VALUES (%s, %s, %s, %s)" ,(str(ip), str(ssh), str(snmp), str(snmp_community)))
        con.commit()
        con.close()

def edit_locations(ip, item_e, new_e):
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    cur = con.cursor()
    if item_e == 'IP Address':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set ip_addr=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()
    if item_e == 'Brand':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set brand=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()
    if item_e == 'OS Version':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set os_version=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()
    if item_e == 'Host Name':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set hostname=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()
    if item_e == 'Domain':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set domain_name=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()
    if item_e == 'User Name':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set usr=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()
    if item_e == 'Password':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set passwd=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()
    if item_e == 'Location':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set dev_loc=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()
    if item_e == 'Device Role':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set dev_role=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()
    if item_e == 'Device Type':
        # print("Database opened successfully")
        cur.execute("UPDATE devices set dev_type=%s where ip_addr=%s", (str(new_e), str(ip)))
        con.commit()
        con.close()