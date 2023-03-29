import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    database="boardofdirectors",
    user="root",
    password="Sukesh@2002" )

cursor = conn.cursor()
query="SELECT * FROM bod_data"
# query="SELECT COALESCE(), '')"
cursor.execute(query)

data=cursor.fetchall()
conn.close()

for row in data:
    print(row)