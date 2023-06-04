import psycopg2

def db_ne_dev_clean():
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    #print("Database opened successfully")
    cur = con.cursor()
    cur.execute("DELETE FROM neighbor_dev;")
    con.commit()
    con.close()
