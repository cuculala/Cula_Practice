#This is just a test. No serious business
from flask import Flask, render_template,request

import sqlite3

app = Flask(__name__)
@app.route("/")
def info():
	return render_template("formsocial.html")

#define a handlers
@app.route("/dev")
def index():
	CONN = sqlite3.connect("social.db")
	DB = CONN.cursor()
	id = request.args.get("user_id")
	pass = request.args.get("password")
	
	#query= """Select fname, Class FROM users WHERE ID = ? AND pass = ?"""
	DB.execute("SELECT fname, lname FROM users WHERE ID = ? AND password = ?",id,pass)
	result=DB.fetchone()

	fname = result[0]
	lname = result[1]

	query= """Select topic,body Class FROM posts WHERE ID = ?"""
	DB.execute(query,(id))
	result=DB.fetchone()
	
	topic = result[0]
	body = result[1]

	return render_template("user.html",fname=fname,lname=lname,topic=topic,body=body)

	
#run app
if __name__=="__main__":
	app.run(debug=True)


