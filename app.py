#This is just a test. No serious business
from flask import Flask, render_template,request

import sqlite3

app = Flask(__name__)
@app.route("/")
def info():
	return render_template("home.html")

#define a handlers
@app.route("/dev")
def index():
	CONN = sqlite3.connect("test.db")
	DB = CONN.cursor()
	id = request.args.get("id")
	
	query = """Select FullName, Class FROM Regstd_Player WHERE ID = ?"""
	DB.execute(query,(id,))
	result=DB.fetchone()

	Name = result[0]
	Class = result[1]

	return render_template("Registered_Player.html",Name = Name, Class = Class)

	
#run app
if __name__=="__main__":
	app.run(debug=True)


