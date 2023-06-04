import psycopg2

def db_rd_cr_br():

    active_ip = []
    usr = []
    passwd = []
    br_ip = []
    br_id = []
    br_os = []
    last_ip = []
    last_br = []
    last_os = []
    last_usr = []
    last_passwd = []

    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT ip_addr, usr, passwd  from devices")
    rows = cur.fetchall()

    for row in rows:
        active_ip.append(row[0])
        usr.append(row[1])
        passwd.append(row[2])
    con.close()

    con_1 = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    cur = con_1.cursor()
    cur.execute("SELECT ip_addr, brand, os_version  from devices")
    rows_1 = cur.fetchall()
    for row in rows_1:
        br_ip.append(row[0])
        br_id.append(row[1])
        br_os.append(row[2])
    con_1.close()

    for ip in active_ip:
        if ip in br_ip:
            index_1 = active_ip.index(ip)
            index_2 = br_ip.index(ip)
            last_br.insert(index_1, br_id[index_2])
            last_os.insert(index_1, br_os[index_2])
            last_ip.insert(index_1, active_ip[index_1])
            last_usr.insert(index_1, usr[index_1])
            last_passwd.insert(index_1, passwd[index_1])
        else:
            index_1 = active_ip.index(ip)
            last_br.insert(index_1, '')
            last_os.insert(index_1, '')
            last_ip.insert(index_1, active_ip[index_1])
            last_usr.insert(index_1, usr[index_1])
            last_passwd.insert(index_1, passwd[index_1])

    return last_ip, last_usr, last_passwd, last_br, last_os

