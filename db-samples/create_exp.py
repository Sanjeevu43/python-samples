# This example is demonstrated with PostreSQL (PostreSQL is opensource database)

import psycopg2
from gretel_trainer.relational import Connector

conn = psycopg2.connect(database="SAN_DB", user = "postgres", password = "pass1234", host = "127.0.0.1", port = "5432")
print('Opened database successfully')

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')

print("Table created successfully")

conn.commit()
conn.close()