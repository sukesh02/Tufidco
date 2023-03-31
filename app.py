from flask import Flask,render_template,url_for
import mysql.connector
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/schemesfunds")
def sch():
    global sch_data
    conn = mysql.connector.connect(
    host="localhost",
    database="funds",
    user="root",
    password="tejaswini@3012" )

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
    password="tejaswini@3012" )
    
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
    password="tejaswini@3012" )

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
    password="tejaswini@3012" )

    cursor = conn.cursor()
    query="SELECT * FROM uids"
    cursor.execute(query)

    uids_data=cursor.fetchall()
    conn.close()
    
    return render_template("sch.html", data=sch_data,data1=swap_data,data2=smart_data,data3=uids_data)
@app.route("/fund")
def fund():
     return render_template("fund.html")

@app.route("/about")
def welcome():
	return render_template("about.html")

@app.route("/schemes")
def schemes():
    return render_template("schemes.html")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)