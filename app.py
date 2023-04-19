from flask import Flask,render_template,url_for
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
load_dotenv()
host = os.getenv('host')
database = os.getenv('database')
user = os.getenv('user')
password= os.getenv('password')


app = Flask(__name__)

# app.config['MYSQL_HOST'] = 'localhost'
# #MySQL username
# app.config['MYSQL_USER'] = 'root'
# #MySQL password here in my case password is null so i left empty
# app.config['MYSQL_PASSWORD'] = 'Sukesh@2002'
# #Database name In my case database name is projectreporting
# app.config['MYSQL_DB'] = 'schemes'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
     return render_template('contact.html')
     
# @app.route("/schemes")
# def schemes():
#     # global schemes_data
#     conn = mysql.connector.connect(
#     host= host,
#     database= database,
#     user= user,
#     password= password)

#     cursor = conn.cursor()
#     query="SELECT * FROM schemes_data"
#     cursor.execute(query)

#     schemes_data=cursor.fetchall()
#     conn.close()
    
#     return render_template("schemes.html", data=schemes_data)

@app.route('/boardofdirectors')
def bod():
    # global bod_data
    conn = mysql.connector.connect(
    host= host,
    database= database,
    user= user,
    password= password )

    cursor = conn.cursor()
    query="SELECT * FROM bod_data"
    cursor.execute(query)

    bod_data=cursor.fetchall()
    conn.close()
    return render_template('boardofdirectors.html', data=bod_data)

@app.route('/funds')
def fund():
    return render_template("funds.html")

@app.route("/tnuidrf")
def sch():
    global sch_data
    conn = mysql.connector.connect(
    host="localhost",
    database="funds",
    user="root",
    password="Swetha#2002" )

    cursor = conn.cursor()
    query="SELECT * FROM fund_data"
    cursor.execute(query)

    sch_data=cursor.fetchall()
    conn.close()

    global swap_data
    conn = mysql.connector.connect(
    host="localhost",
    database="funds",
    user="root",
    password="Swetha#2002" )
    
    cursor = conn.cursor()
    query="SELECT * FROM swap"
    cursor.execute(query)
    
    swap_data=cursor.fetchall()
    conn.close()

    global smart_data
    conn = mysql.connector.connect(
    host="localhost",
    database="funds",
    user="root",
    password="Swetha#2002" )

    cursor = conn.cursor()
    query="SELECT * FROM smartcity"
    
    cursor.execute(query)

    smart_data=cursor.fetchall()
    conn.close()

    global uids_data
    conn = mysql.connector.connect(
    host="localhost",
    database="funds",
    user="root",
    password="Swetha#2002" )

    cursor = conn.cursor()
    query="SELECT * FROM uids"
    cursor.execute(query)

    uids_data=cursor.fetchall()
    conn.close()
    
    return render_template("sch.html", data=sch_data,data1=swap_data,data2=smart_data,data3=uids_data)

@app.route("/about")
def welcome():
	return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)