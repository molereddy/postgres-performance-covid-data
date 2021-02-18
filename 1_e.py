import psycopg2
import 1_b
import time
from csv import reader


def update_sql(row):
    return f"""
            INSERT INTO covid
            VALUES ({', '.join(1_b.wrap(row))});
            """"


for i in range(6, 11):
    with open(f"data{i}.csv", 'r') as f:
        start = time.time()
        index = 0
        for row in reader(f):
            index += 1
            if index == 1:
                continue
            conn = 1_b.connect()
            cur = conn.cursor()
            1_b.exec_update(sql=update_sql(row), conn=conn)
            conn.commit()
            cur.close()
        print(time.time()-start)
