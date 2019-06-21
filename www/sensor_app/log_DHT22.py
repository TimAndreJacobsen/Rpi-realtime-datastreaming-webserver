# This file handles recording and and logging of humidity and temperature.
# Records from DHT_22 sensor and logs into SQLite3 database

import sqlite3
import time
import gevent
import Adafruit_DHT
import mailer
import config


def log_values(sensor_id, temperature, humidity):
    connection = sqlite3.connect('/var/www/sensor_app/sensor_app.db')
    cursor = connection.cursor()
    cursor.execute(
        """INSERT INTO temperatures values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id, temperature))
    cursor.execute(
        """INSERT INTO humidities values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""", (sensor_id, humidity))
    connection.commit()
    connection.close()


def send_alert(temp, hum):
    gevent.sleep(1)
    if (config.CNF['last_time_called'] + 1200) < time.time():
        mailer.send(temp, hum, config.CNF['last_time_called'])
        print(config.CNF['last_time_called'])
        config.set_time()
        print(config.CNF['last_time_called'])
    gevent.sleep(1)


HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
if HUMIDITY is not None and TEMPERATURE is not None:
    if not HUMIDITY > 100 and not TEMPERATURE > 100:
        if not HUMIDITY < 0 and not TEMPERATURE < 0:
            log_values("ceiling", TEMPERATURE, HUMIDITY)
            if TEMPERATURE > 30 or TEMPERATURE < 5:
                send_alert(TEMPERATURE, HUMIDITY)
else:
    while HUMIDITY is None:
        HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
        gevent.sleep(5)
    log_values("ceiling", TEMPERATURE, HUMIDITY)
    # set up error reporting
