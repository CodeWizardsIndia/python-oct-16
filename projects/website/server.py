import flask as f
app= f.Flask(__name__)

@app.route("/")
def home():
	return f.render_template("my_page.htm")

app.run(host="0.0.0.0",port=80)
