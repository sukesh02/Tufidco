import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    database="funds",
    user="root",
    password="tejaswini@3012" )

cursor = conn.cursor()
query="SELECT * FROM uids"
cursor.execute(query)

sch_data=cursor.fetchall()
conn.close()

for row in sch_data:
    print(row)