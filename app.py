from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sukesh:sukesh@2002@localhost/mydatabase'

@app.route("/sch")
def sch():
     return render_template("sch.html")

@app.route("/fund")
def fund():
     return render_template("fund.html")

@app.route("/about")
def welcome():
	return render_template("about.html")

@app.route("/<name>")
def schemes(name):
    return render_template("schemes.html", name=name)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)