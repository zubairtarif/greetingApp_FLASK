from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "abc"

@app.route("/hello")
def index():
	flash("What's your name????????")
	return render_template("index.html") #because we saved an index file udner templates folder, flask will be able to find it

@app.route("/greet", methods=["POST", "GET"])
def greetingforyou():
	flash("Hi " + str(request.form['name_input']) + ", great to see you!")
	return render_template("index.html")
