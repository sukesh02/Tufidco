from flask import Flask,render_template,url_for,request
from flask_mysqldb import MySQL
import mysql.connector
from flask_sqlalchemy import SQLAlchemy

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

@app.route("/schemes")
def schemes():
    global data
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
    
    return render_template("schemes.html", data=data)

@app.route('/boardofdirectors')
def bod():
    return render_template('boardofdirectors.html')

@app.route('/fund')
def fund():
    return render_template("fund.html")

@app.route("/sch")
def sch():
     return render_template("sch.html")

@app.route("/about")
def welcome():
	return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)