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

@app.route("/current")
def show_realtime_status():
    humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
    if humidity is not None and temp is not None:
        return render_template("room_data.html", temp=temp, humidity=humidity)
    else:
        return render_template("sensor_error.html", msg="temp/humid is None")

@app.route("/status", methods=['GET'])
def status():
    from_datetime, to_datetime = get_args()
    temperatures, humidities, temp_hum = get_records(from_datetime, to_datetime)
    return render_template("room_status.html", temp=temperatures, hum=humidities, both=temp_hum, temp_items=len(temperatures), hum_items=len(humidities), both_items=len(temp_hum))

def get_records(from_datetime, to_datetime):
    conn, curs = db_connect()
    curs.execute('SELECT * FROM temperatures WHERE rDatetime BETWEEN ? AND ?', (from_datetime, to_datetime))
    temp_rows = curs.fetchall()
    curs.execute('SELECT * FROM humidities WHERE rDatetime BETWEEN ? AND ?', (from_datetime, to_datetime))
    humi_rows = curs.fetchall()
    curs.execute('SELECT temperatures.rDatetime, temperatures.temp, humidities.humidity FROM temperatures WHERE rDatetime BETWEEN ? AND ? JOIN humidities ON temperatures.rDatetime = humidities.rDatetime', (from_datetime, to_datetime))
    both_rows = curs.fetchall()

    db_disconnect(conn)
    return temp_rows, humi_rows, both_rows

def get_args():
    # get args from url
    start_datetime_obj = request.args.get('from', time.strftime("%Y-%m-%d 00:00"))
    end_datetime_obj = request.args.get('to', time.strftime("%Y-%m-%d %H:%M"))
    radio_hours_form = request.args.get('range_h')

    start_datetime, end_datetime = validate_datetime_interval(start_datetime_obj, end_datetime_obj)

    range_hours_int = "nan"
    try:
        range_hours_int = int(radio_hours_form)
    except:
        print("range_hours_form not a number")
    if isinstance(range_hours_int, int):
        time_now, time_to = datetime.datetime.now(), datetime.datetime.now()
        time_from = time_now - datetime.timedelta(hours=range_hours_int)
        start_datetime = time_from.strftime("%Y-%m-%d %H:%M")
        end_datetime = time_to.strftime("%Y-%m-%d %H:%M")

    return start_datetime, end_datetime

    
def validate_datetime_interval(from_datetime, to_datetime):
    if not validate_datetime(from_datetime):
        from_datetime = time.strftime("%Y-%m-%d 00:00")
    if not validate_datetime(to_datetime):
        to_datetime = time.strftime("%Y-%m-%d %H:%M")
    return from_datetime, to_datetime

def validate_datetime(datetime_obj):
    try:
        datetime.datetime.strptime(datetime_obj, "%Y-%m-%d %H:%M")
        return True
    except ValueError:
        return False

def db_connect():
    connection = sqlite3.connect('/var/www/sensor_app/sensor_app.db')
    cursor = connection.cursor()
    return connection, cursor

def db_disconnect(conn):
    conn.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)