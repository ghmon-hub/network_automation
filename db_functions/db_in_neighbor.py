import psycopg2

def db_nei_device(l_ip, l_port, nei_host):
    ip_list = []
    inter_list = []
    nei_list = []
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    cur = con.cursor()
    cur.execute("SELECT ip_addr, interface, ne_hostname from neighbor_dev")
    rows = cur.fetchall()
    for row in rows:
        ip_list.append(row[0])
        inter_list.append(row[1])
        nei_list.append(row[2])

    if l_ip in ip_list:
        i_index = ip_list.index(l_ip)
        if l_port == inter_list[i_index]:
            if nei_host == nei_list[i_index]:
                pass
            else:
                con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
                cur = con.cursor()
                cur.execute("INSERT INTO neighbor_dev (ip_addr, interface, ne_hostname) VALUES (%s, %s, %s)",(str(l_ip), str(l_port), str(nei_host)))
                con.commit()
                con.close()
        else:
            con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
            cur = con.cursor()
            cur.execute("INSERT INTO neighbor_dev (ip_addr, interface, ne_hostname) VALUES (%s, %s, %s)",(str(l_ip), str(l_port), str(nei_host)))
            con.commit()
            con.close()
    else:
        con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
        cur = con.cursor()
        cur.execute("INSERT INTO neighbor_dev (ip_addr, interface, ne_hostname) VALUES (%s, %s, %s)",(str(l_ip), str(l_port), str(nei_host)))
        con.commit()
        con.close()
