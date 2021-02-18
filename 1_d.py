import psycopg2
import 1_b
import time
from csv import reader
conn = 1_b.connect()
cur = conn.cursor()


def update_sql(row):
    return f"""
            INSERT INTO covid
            VALUES ({', '.join(1_b.wrap(row))});
            """"


for i in range(1, 6):
    with open(f"data{i}.csv", 'r') as f:
        start = time.time()
        index = 0
        for row in reader(f):
            index += 1
            if index == 1:
                continue
            1_b.exec_update(sql=update_sql(row), conn=conn)
        print(time.time()-start)

conn.commit()
cur.close()
