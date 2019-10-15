# Name: Kevin Chen
# Net ID: kc3585

from flask import Flask, render_template, request
import pymysql.cursors

app = Flask(__name__)

connection = pymysql.connect(
				host='cs1122.c1icwtbkfcxn.us-east-1.rds.amazonaws.com',
				user='kc3585',
				password='kc3585',
				db='kc3585'
			)

@app.route("/")
def home():
	try:
		with connection.cursor() as cursor:
			# write the SQL query that gets all items in the todos table
			sql = "SELECT item FROM todos"
			cursor.execute(sql)
			result = cursor.fetchall()
			todos = [r[0] for r in result]
	except:
		return render_template("index.html", success=False)
	return render_template("index.html", todos=todos)

@app.route("/add", methods=['POST'])
def add():
	item = request.form.get('todo')
	try:
		with connection.cursor() as cursor:
			# write the SQL query that inserts an item into the todos table
			sql = "INSERT INTO todos(item) VALUES (%s)"
			cursor.execute(sql, (item))
		connection.commit()
	except:
		return '0'
	return '1'

@app.route("/delete", methods=['POST'])
def delete():
	target = request.form.get('target')
	try:
		with connection.cursor() as cursor:
			# write the SQL query that deletes the item matching the value of target from the todos table
			sql = "DELETE FROM todos WHERE item = %s"
			cursor.execute(sql, (target))
		connection.commit()
	except:
		return '0'
	return '1'

app.run(port=8000, debug=True)
