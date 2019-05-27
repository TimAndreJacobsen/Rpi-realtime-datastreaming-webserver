# This file handles recording and and logging of humidity and temperature.
# Records from DHT_22 sensor and logs into SQLite3 database

import sqlite3
import time
import gevent
import Adafruit_DHT
import mailer

# Setup and config
ALERT_INTERVAL = 3600   # time between alert mails | 3600 = 1hour

def log_values(sensor_id, temperature, humidity):
    connection = sqlite3.connect('/var/www/sensor_app/sensor_app.db')
    cursor = connection.cursor()
    cursor.execute("""INSERT INTO temperatures values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id, temperature))
    cursor.execute("""INSERT INTO humidities values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id, humidity))
    connection.commit()
    connection.close()

def send_alert(temp, hum):
    try:
        if (last_time_called + 1200) < time.time():
            mailer.send(temp, hum, last_time_called)
            last_time_called = time.time()
    except UnboundLocalError:
        last_time_called = time.time()
        mailer.send(temp, hum, last_time_called)

HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
if HUMIDITY is not None and TEMPERATURE is not None:
    if not HUMIDITY > 100 and not TEMPERATURE > 100:
        if not HUMIDITY < 0 and not TEMPERATURE < 0:
            log_values("ceiling", TEMPERATURE, HUMIDITY)
            if TEMPERATURE > 27 or TEMPERATURE < 10:
                send_alert(TEMPERATURE, HUMIDITY)
else:
    while HUMIDITY is None:
        HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
        gevent.sleep(5)
    log_values("ceiling", TEMPERATURE, HUMIDITY)
    # set up error reporting
