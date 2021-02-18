import psycopg2
import config
conn = config.connect()
cur = conn.cursor()

try:
    cur.execute("""DROP TABLE IF EXISTS covid CASCADE""")
    cur.execute("""CREATE TABLE covid
                    (
                    cdc_report_dt  char(128),
                    pos_spec_dt  char(128),
                    onset_dt  char(128),
                    current_status  char(128),
                    sex  char(128),
                    age_group  char(128),
                    Race_and_ethnicity  char(128),
                    hosp_yn  char(128),
                    icu_yn  char(128),
                    death_yn  char(128),
                    medcond_yn   char(128)
                    );"""
                )

except Exception as err:
    print("ERROR while creation %%%%%%%%%%%%%%%% \n", err)


conn.commit()
conn.close()

# lab4db=# \COPY covid FROM '/host/Desktop/CS-387/180050059-180050074-a4/postgres-performance-covid-data/data1.csv' DELIMITER ',' CSV HEADER;
# COPY 99999
# Time: 14706.240 ms (00:14.706)

# lab4db=# \COPY covid FROM '/host/Desktop/CS-387/180050059-180050074-a4/postgres-performance-covid-data/data2.csv' DELIMITER ',' CSV HEADER;
# COPY 199999
# Time: 36239.200 ms (00:36.239)

# lab4db=# \COPY covid FROM '/host/Desktop/CS-387/180050059-180050074-a4/postgres-performance-covid-data/data3.csv' DELIMITER ',' CSV HEADER;
# COPY 299999
# Time: 120634.530 ms (02:00.635)

# lab4db=# \COPY covid FROM '/host/Desktop/CS-387/180050059-180050074-a4/postgres-performance-covid-data/data4.csv' DELIMITER ',' CSV HEADER;
# COPY 399999
# Time: 176377.818 ms (02:56.378)

