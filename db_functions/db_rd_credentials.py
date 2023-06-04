import psycopg2

def db_rd_cr():

    active_ip = []
    usr = []
    passwd = []
    brands = []
    br_ip = []
    br_id = []

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
    cur.execute("SELECT ip_addr, brand  from devices")
    rows_1 = cur.fetchall()
    for row in rows_1:
        br_ip.append(row[0])
        br_id.append(row[1])
    con_1.close()

    for ip in active_ip:
        if ip in br_ip:
            index_1 = active_ip.index(ip)
            index_2 = br_ip.index(ip)
            brands.insert(index_1, br_id[index_2])
        else:
            index_1 = active_ip.index(ip)
            brands.insert(index_1, '')

    return active_ip, usr, passwd, brands

