from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sukesh:sukesh@2002@localhost/mydatabase'


@app.route("/<name>")
def fund(name):
     return render_template("fund.html", name=name)
@app.route("/<name>")
def welcome(name):
	return render_template("about.html", name=name)

@app.route("/<name>")
def schemes(name):
    return render_template("schemes.html", name=name)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)