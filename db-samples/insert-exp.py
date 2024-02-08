import psycopg2

conn = psycopg2.connect(database="SAN_DB", user = "postgres", password = "pass1234", host = "127.0.0.1", port = "5432")
print('Opened database successfully')

cur = conn.cursor()

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'San', 32, 'Blore', 20000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Dan', 25, 'Hyd', 15000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Sam', 23, 'Chennai', 20000.00 )");

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Pune', 65000.00 )");

conn.commit()
print('Records created successfully')
conn.close()