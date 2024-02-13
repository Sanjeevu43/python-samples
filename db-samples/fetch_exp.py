import psycopg2

conn = psycopg2.connect(database="SAN_DB", user = "postgres", password = "pass1234", host = "127.0.0.1", port = "5432")
print('Opened database successfully')

cur = conn.cursor()

cur.execute("SELECT * from COMPANY")
rows = cur.fetchall()
for row in rows:
   print(row)

print("Operation done successfully")
conn.close()