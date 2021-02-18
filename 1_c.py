import psycopg2,config
import time
conn = psycopg2.connect(database=config.name, user=config.user,
                            password=config.pswd, host=config.host, port=config.port)

cur = conn.cursor()

copy_sql = """
           COPY covid FROM stdin DELIMITER ',' CSV HEADER;
           """

for i in range(1, 6):
    with open(f"data{i}.csv", 'r') as f:
        start = time.time()
        cur.copy_expert(sql=copy_sql, file=f)
        print(time.time()-start)

conn.commit()
cur.close()
