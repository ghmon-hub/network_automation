import psycopg2

def db_upd_in(ip, brd, os_v):
    ip_list = set()
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    #print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT ip_addr from brands")
    rows = cur.fetchall()
    for row in rows:
        ip_list.add(row[0])
    if ip in ip_list:
        cur.execute("UPDATE devices set brand=%s, os_version=%s, where ip_addr=%s", (str(brd), str(os_v), str(ip)))
        #cursor.execute("UPDATE table_name SET field1=%s, ..., field10=%s WHERE id=%s", (var1, ... var10, id))
        con.commit()
        con.close()
    else:
        cur.execute("INSERT INTO brands (ip_addr, brand, os_version) VALUES (%s, %s, %s)" ,(str(ip), str(brd), str(os_v)))
        con.commit()
        con.close()

