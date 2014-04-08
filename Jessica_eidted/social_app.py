#This is just a test. No serious business
from flask import Flask, render_template,request

import sqlite3

app = Flask(__name__)
@app.route("/")
def info():
	return render_template("form_social.html")

#define a handlers
@app.route("/dev", methods = ["POST"])
def index():
	CONN = sqlite3.connect("social.db")
	DB = CONN.cursor()

	# WIll work if "GET" is included as part of methods
	# user_id = request.args.get("user_id")
	# password = request.args.get("password")

	user_id = request.form["user_id"]
	password = request.form["password"]
	
	#query= """Select fname, Class FROM users WHERE ID = ? AND pass = ?"""
	query = """SELECT fname, l_name FROM users WHERE user_id = ? AND password = ?"""
	DB.execute(query,(user_id,password))
	result=DB.fetchone()

	print result

	fname = result[0]
	lname = result[1]

	query= """Select topic, body FROM posts WHERE user_id = ?"""
	DB.execute(query,(user_id))
	result=DB.fetchall()
	
	# topic = result[0]
	# body = result[1]

	return render_template("user.html",fname=fname,lname=lname,posts=result)

	
#run app
if __name__=="__main__":
	app.run(debug=True)


