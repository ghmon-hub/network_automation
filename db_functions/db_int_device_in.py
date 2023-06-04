import psycopg2

def db_ne_l3_in(ip, net_m, net_br, ip_ad, inter, spd, p_srv, p_acl, ip_sec, src_ad, dst_ad, dup_mo):

    ip_list = set()
    inter_list = []
    #print(ip, net_m, net_br, ip_ad, inter, spd, p_srv, p_acl, ip_sec, src_ad, dst_ad, dup_mo)
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    #print("Database opened successfully")
    cur = con.cursor()
    cur.execute("INSERT INTO interface_dev (ip_addr, net_m, net_br, ip_a, inter, spd, p_srv, p_acl, ip_sec, src_ad, dst_ad, dup_mo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" ,(str(ip), str(net_m), str(net_br), str(ip_ad), str(inter), str(spd), str(p_srv), str(p_acl), str(ip_sec), str(src_ad), str(dst_ad), str(dup_mo)))
    con.commit()
    con.close()
