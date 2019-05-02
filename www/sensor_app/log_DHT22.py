# This file handles recording and and logging of humidity and temperature.
# Records from DHT_22 sensor and logs into SQLite3 database

import sqlite3
import sys
import Adafruit_DHT

def log_values(sensor_id, temperature, humidity):
    connection = sqlite3.connect('/var/www/sensor_app/sensor_app.db')
    cursor = connection.cursor()

