import psycopg2


con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
cur = con.cursor()
cur.execute("SELECT  ip_addr, net_m, net_br, ip_a, inter, spd, p_srv, p_acl, ip_sec, src_ad, dst_ad, dup_mo  from interface_dev")
rows = cur.fetchall()
con.close()
for row in rows:
    print(row[0]+"\n", row[1]+"\n", row[2]+"\n", row[3]+"\n", row[4]+"\n", row[5]+"\n", row[6]+"\n", row[7]+"\n", row[8]+"\n", row[9]+"\n", row[10]+"\n", row[11]+"\n")
