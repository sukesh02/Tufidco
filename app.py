from flask import Flask,render_template,url_for,request
import psycopg2
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/schemes")
def schemes():
    return render_template("schemes.html")

@app.route('/bod')
def bod():
    return render_template('bod.html')

@app.route('/fund')
def fund():
    return render_template("fund.html")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

conn = psycopg2.connect(database="schemes", 
                        user="sukku",
                        password="schemes", 
                        host="localhost", port="5432")

cur = conn.cursor()

cur.execute('''SELECT * FROM schemes_data''')

data = cur.fetchall()

conn.commit()

cur.close()
conn.close()