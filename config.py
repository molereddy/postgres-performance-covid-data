import psycopg2
from psycopg2.extras import RealDictCursor

# database name, username, password, host, port number in order
# update values if necessary
name = "lab4db"
user = "postgres"
pswd = "ubuntu123"
host = "127.0.0.1"
port = "5432"
"""to access results by column as a dictionary use:
from psycopg2.extras import RealDictCursor
then in connect use last argument as psycopg2.connect(..cursor_factory=RealDictCursor)
then you can access as cur.fetchall()[row_num][col_name]"""

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


