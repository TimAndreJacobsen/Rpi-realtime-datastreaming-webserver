from flask import Flask, request, render_template
import sys
import Adafruit_DHT

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return render_template("index.html", message="hello world, flask with render here!")

@app.route("/data")
def show_data():
    humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
    if humidity is not None and temp is not None:
        return render_template("room_data.html", temp=temp, humidity=humidity)
    else:
        return render_template("sensor_error.html", msg="temp/humid is None")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)