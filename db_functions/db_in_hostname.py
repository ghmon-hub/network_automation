import psycopg2

def db_host_in(ip, hostname, domain_name):
    ip_list = set()
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    #print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT ip_addr from devices")
    rows = cur.fetchall()
    for row in rows:
        ip_list.add(row[0])
    if ip in ip_list:
        cur.execute("UPDATE devices set hostname=%s, domain_name=%s where ip_addr=%s", (str(hostname), (str(domain_name)), str(ip)))
        con.commit()
        con.close()
    else:
        cur.execute("INSERT INTO devices (ip_addr, hostname, domain_name) VALUES (%s, %s, %s)", (str(ip), str(hostname), str(domain_name)))
        con.commit()
        con.close()

