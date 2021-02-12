import psycopg2
import config
from psycopg2.extras import RealDictCursor
"""to access results by column as a dictionary use:
from psycopg2.extras import RealDictCursor
then in connect use last argument as psycopg2.connect(..cursor_factory=RealDictCursor)
then you can access as cur.fetchall()[row_num][col_name]"""

def connect():
    """ returns connection to database """
    # TODO: use variables from config file as connection params
    conn = psycopg2.connect(database=config.name, user=config.user,
                            password=config.pswd, host=config.host, port=config.port)
    return conn


def exec_query(conn, sql):
    """ Executes sql query and returns header and rows """
    # TODO: create cursor, get header from cursor.description, and execute query to fetch rows.
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(sql)
        conn.commit()
        return ([desc[0] for desc in cursor.description], cursor.fetchall())

def exec_update(conn, sql):
    with conn.cursor(cursor_factory=RealDictCursor) as cursor:
        cursor.execute(sql)
        conn.commit()


if __name__ == "__main__":
    from sys import argv
    import config

    query = argv[1]
    try:
        conn = connect()
        (header, rows) = exec_query(conn, query)
        print(",".join([str(i) for i in header]))
        for r in rows:
            print(",".join([str(i) for i in r]))
        conn.close()
    except Exception as err:
        print("ERROR %%%%%%%%%%%%%%%% \n", err)
