from flask import Flask,render_template,url_for
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

host = os.getenv('host')
user = os.getenv('user')
password= os.getenv('password')
db = os.getenv('db')
database1=os.getenv('database1')
database2=os.getenv('database2')
database3=os.getenv('database3')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/about")
def welcome():
	return render_template("about.html")

@app.route('/contact')
def contact():
     return render_template('contact.html')




@app.route('/funds')
def fund():
    return render_template("funds.html")

@app.route("/schemes")
def sch():
    conn = mysql.connector.connect(
    host=host,
    db=db,
    user=user,
    password="tejaswini@3012" )

    # cursor = conn.cursor()
    # query="SELECT * FROM fund_data"
    # cursor.execute(query)

    
    # cursor = conn.cursor()
    # query="SELECT * FROM swap"
    # cursor.execute(query)
    

    swap_data=cursor.fetchall()
    conn.close()

    global smart_data
    conn = mysql.connector.connect(
    host="localhost",
    database="funds",
    user="root",
    password="tejaswini@3012" )

    # swap_data=cursor.fetchall()
    # conn.close()

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
    
    return render_template("sch.html",data2=smart_data,data3=uids_data)



if __name__ == "__main__":
    app.run(debug=True)