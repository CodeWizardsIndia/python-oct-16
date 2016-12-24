import flask as f
app = f.Flask(__name__)



@app.route("/")
def home ():
	#return "hello world"
	return f.render_template("my_page.html")

@app.route("/dhruv")
def dhruv():
	return "My Name is Dhruv"

app.run(host = "0.0.0.0", port = 80, debug=True)
