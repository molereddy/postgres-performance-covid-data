import glob, config, os, shutil
from csv import reader
from pathlib import Path
dirpath=Path('insert')
if dirpath.exists() and dirpath.is_dir():
    shutil.rmtree(dirpath)
dirpath.mkdir()
"""to access results by column as a dictionary use:
from psycopg2.extras import RealDictCursor
then in connect use last argument as psycopg2.connect(..cursor_factory=RealDictCursor)
then you can access as cur.fetchall()[row_num][col_name]"""

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
