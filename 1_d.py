import psycopg2,config
import time
from csv import reader
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect(database=config.name, user=config.user,
                            password=config.pswd, host=config.host, port=config.port)

cur = conn.cursor()

def exec_update(conn, sql):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(sql)


def wrap(lst): return ["'"+ele+"'" for ele in lst]


def update_sql(row):
    return f"""
            INSERT INTO covid
            VALUES ({', '.join(wrap(row))});
            """

exec_update(sql="DELETE from COVID;", conn=conn)

for i in range(1, 6):
    with open(f"data{i}.csv", 'r') as f:
        start = time.time()
        index = 0
        for row in reader(f):
            index += 1
            if index == 1:
                continue
            exec_update(sql=update_sql(row), conn=conn)
        print(time.time()-start)
        exec_update(sql="DELETE from COVID;", conn=conn)

conn.commit()
cur.close()
