from flask import Flask,render_template
import json

#create an instance of Flask
app = Flask(__name__)

@app.route("/displayMap")
def render_map():
	return render_template("index.html")

@app.route('/updateMap', methods= ["POST"])
def addMarker():
	lat = 51.484321
	lng = -3.1717929

	return json.dumps({'latitude': lat, 'longitude':lng})

@app.route("/")
def hello():
	return 'Hello World'

if __name__ =='__main__':
		app.run(debug=True)

