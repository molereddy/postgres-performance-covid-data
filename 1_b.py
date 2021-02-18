import glob
from csv import reader
"""to access results by column as a dictionary use:
from psycopg2.extras import RealDictCursor
then in connect use last argument as psycopg2.connect(..cursor_factory=RealDictCursor)
then you can access as cur.fetchall()[row_num][col_name]"""

import psycopg2
from psycopg2.extras import RealDictCursor



def connect():
    """ returns connection to database """
    # TODO: use variables from config file as connection params
    conn = psycopg2.connect(database=name, user=user,
                            password=pswd, host=host, port=port)
    return conn

def exec_query(conn, sql):
    """ Executes sql query and returns header and rows """
    # TODO: create cursor, get header from cursor.description, and execute query to fetch rows.
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(sql)
        return ([desc[0] for desc in cursor.description], cursor.fetchall())

def exec_update(conn, sql):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(sql)


def wrap(lst): return ["'"+ele+"'" for ele in lst]

csv_names = [f"./data{i+6}.csv" for i in range(5)]
sql_names = [f"./insert/data{i+6}.sql" for i in range(5)]

for i in range(5):
    index = 0
    csv_open = open(csv_names[i], "r")
    sql_open = open(sql_names[i], "w+")
    for row in reader(csv_open):
        index += 1
        if index == 1:
            continue
        sql_open.write("insert into covid values ("+', '.join(wrap(row))+");\n")
    sql_open.close()
    csv_open.close()
