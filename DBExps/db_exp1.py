import psycopg2
from gretel_trainer.relational import Connector

conn = psycopg2.connect(database="SAN_DB", user = "postgres", password = "Unisys123", host = "127.0.0.1", port = "5432")
print('Opened database successfully')

cur = conn.cursor()
# cur.execute('''CREATE TABLE COMPANY
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50),
#       SALARY         REAL);''')

# Customer Data
# country table
# cur.execute('''CREATE TABLE COUNTRY (COUNTRY_ID INT PRIMARY KEY NOT NULL,
#                                      COUNTRY_NAME TEXT NOT NULL)''')

# cur.execute('''CREATE TABLE CITY (CITY_ID INT PRIMARY KEY NOT NULL,
#                                      CITY_NAME TEXT NOT NULL,
#                                      COUNTRY_ID INT,
#                                      CONSTRAINT FK_city_country FOREIGN KEY(COUNTRY_ID)
#                                      REFERENCES COUNTRY(COUNTRY_ID) )''')

# cur.execute('''CREATE TABLE ADDRESS (ADDRESS_ID INT PRIMARY KEY NOT NULL,
#                                      ADDRESS TEXT NOT NULL,
#                                      POSTAL_CODE VARCHAR(20),
#                                      PHONE_NO VARCHAR(10),
#                                      CITY_ID INT,
#                                      CONSTRAINT FK_address_city FOREIGN KEY(CITY_ID)
#                                      REFERENCES CITY(CITY_ID) )''')

# cur.execute('''CREATE TABLE CUSTOMER (CUSTOMER_ID INT PRIMARY KEY NOT NULL,
#                                      FIRSTNAME TEXT NOT NULL,
#                                      LASTNAME TEXT NOT NULL,
#                                      EMAIL VARCHAR(50),
#                                      ADDRESS_ID INT,
#                                      CONSTRAINT FK_custoner_address FOREIGN KEY(ADDRESS_ID)
#                                      REFERENCES ADDRESS(ADDRESS_ID) )''')

print("Table created successfully")

conn.commit()
conn.close()