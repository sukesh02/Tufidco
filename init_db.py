import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="schemes",
    user="root",
    password="Sukesh@2002" )

cursor = conn.cursor()
query="SELECT * FROM schemes_data"
cursor.execute(query)

data=cursor.fetchall()
conn.close()

for row in data:
    print(row)