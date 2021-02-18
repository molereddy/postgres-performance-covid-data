import psycopg2
conn, cur = None

try:
    conn=exec.connect()
    cur=conn.cursor() 
    cur.execute('DROP TABLE IF EXISTS covid CASCADE')
except Exception as err:
    print("ERROR %%%%%%%%%%%%%%%% \n", err)




conn.commit()
conn.close()