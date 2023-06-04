import psycopg2

def db_rd_int_device(ip):
    interface_list = set()
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT inter, ip_addr FROM interface_dev ORDER BY ip_addr")
    rows = cur.fetchall()
    for row in rows:
        if row[1] == ip:
            interface_list.add(row[0].replace(" ", ""))
    con.close()
    return interface_list

