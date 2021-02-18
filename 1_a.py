import psycopg2
import 1_b

conn = 1_b.connect()
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

