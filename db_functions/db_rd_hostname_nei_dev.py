import psycopg2

def db_rd_host():
    ip_host = []
    host_name = []
    domain_name = []

    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT ip_addr, hostname, domain_name  from devices")
    rows = cur.fetchall()

    for row in rows:
        ip_host.append(row[0])
        host_name.append(row[1])
        domain_name.append(row[2])
    con.close()

    return ip_host, host_name, domain_name

def db_rd_nei():
    ip_nei = []
    interface = []
    hostname = []

    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT ip_addr, interface, ne_hostname  from neighbor_dev")
    rows = cur.fetchall()

    for row in rows:
        ip_nei.append(row[0])
        interface.append(row[1])
        hostname.append(row[2])
    con.close()

    return ip_nei, interface, hostname