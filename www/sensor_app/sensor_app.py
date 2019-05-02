from flask import Flask, request, render_template
import sys
import Adafruit_DHT
import sqlite3
import time
import datetime

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

@app.route("/status", methods=['GET'])
def status():
    from_datetime = request.args.get('from',time.strftime("%Y-%m-%d %H:%M"))
    to_datetime = request.args.get('to', time.strftime("%Y-%m-%d %H:%M"))

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