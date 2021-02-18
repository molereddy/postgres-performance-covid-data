import psycopg2,config

import time
from csv import reader
from psycopg2.extras import RealDictCursor


def wrap(lst): return ["'"+ele+"'" for ele in lst]


def update_sql(row):
    return f"""
            INSERT INTO covid
            VALUES ({', '.join(wrap(row))});
            """


for i in range(6, 11):
    with open(f"data{i}.csv", 'r') as f:
        start = time.time()
        index = 0
        for row in reader(f):
            index += 1
            if index == 1:
                continue
            conn = psycopg2.connect(database=config.name, user=config.user,
                            password=config.pswd, host=config.host, port=config.port)

            cur = conn.cursor()
            cur.execute(update_sql(row))
            cur.close()
        print(time.time()-start)
