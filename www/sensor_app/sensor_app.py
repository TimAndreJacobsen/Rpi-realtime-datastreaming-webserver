from flask import Flask, request, render_template
import sys
import Adafruit_DHT
import sqlite3

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
    return status()

@app.route("/data")
def show_data():
    humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
    if humidity is not None and temp is not None:
        return render_template("room_data.html", temp=temp, humidity=humidity)
    else:
        return render_template("sensor_error.html", msg="temp/humid is None")

@app.route("/status")
def status():
    connection = sqlite3.connect('/var/www/sensor_app/sensor_app.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM temperatures')
    temp_rows = cursor.fetchall()
    cursor.execute('SELECT * FROM humidities')
    humi_rows = cursor.fetchall()

    connection.close()
    return render_template("room_status.html", temp=temp_rows, hum=humi_rows)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)