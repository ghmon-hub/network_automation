import psycopg2

def show_loc():
    locations = str()
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    #print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT location from locations")
    rows = cur.fetchall()
    for row in rows:
        #locations = locations+"\n"+str(row)
        row = str(row)
        row = str(row.replace("'", ""))
        row = str(row.replace(",", ""))
        row = str(row.replace("(", ""))
        row = str(row.replace(")", ""))
        locations = locations+"\n"+row
    return locations

def import_locations(new,id):
    locts = set()
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    # print("Database opened successfully")
    cur = con.cursor()
    cur.execute("SELECT location from locations")
    rows = cur.fetchall()
    for row in rows:
            locts.add(row[0])
    if new in locts:
        return ("The name is Exist")
    else:
        cur.execute("INSERT INTO locations (location, id) VALUES (%s, %s)", (str(new), str(id)))
        con.commit()
        con.close()

def edit_locations(old, new, id):
    con = psycopg2.connect(database="ai", user="ai", password="ai123", host="127.0.0.1", port="5432")
    # print("Database opened successfully")
    cur = con.cursor()
    cur.execute("UPDATE locations set location=%s, id=%s where location=%s", (str(new), str(id), str(old)))
    con.commit()
    con.close()
