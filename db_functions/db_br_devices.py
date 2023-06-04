import psycopg2

def db_upd_in(ip, data_version, brd):
    ip_list = set()
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    #print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT ip_addr from devices")
    rows = cur.fetchall()
    for row in rows:
        ip_list.add(row[0])
    if ip in ip_list:
        cur.execute("UPDATE devices set brand=%s, os_version=%s where ip_addr=%s", (str(brd), str(data_version), str(ip)))
        con.commit()
        con.close()
    else:
        cur.execute("INSERT INTO devices (ip_addr, brand, os_version) VALUES (%s, %s, %s)", (str(ip), str(brd), str(data_version)))
        con.commit()
        con.close()