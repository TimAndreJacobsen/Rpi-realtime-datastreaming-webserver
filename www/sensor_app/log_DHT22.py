# This file handles recording and and logging of humidity and temperature.
# Records from DHT_22 sensor and logs into SQLite3 database

import sqlite3
import sys
import Adafruit_DHT

def log_values(sensor_id, temperature, humidity):
    connection = sqlite3.connect('/var/www/sensor_app/sensor_app.db')
    cursor = connection.cursor()

    cursor.execute("""INSERT INTO temperatures values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""")
    cursor.execute("""INSERT INTO humidities values(datetime(CURRENT_TIMESTAMP, 'localtime'), (?), (?))""")
    
    connection.commit()
    connection.close()

humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
if humidity is not None and temperature is not None:
    log_values("ceiling", temperature, humidity)
    # set up out of optimal range notification
else:
    log_values("ceiling", -998, -998)
    # set up error reporting