import pigpio
import csv
import datetime
from time import sleep
import DHT22

# this connects to the pigpio daemon - needs to be started in CLI first with "sudo pigpiod"
pi = pigpio.pi()

s = DHT22.sensor(pi, 4) # initialize sensor on the pi, gpio#4
time = datetime.datetime.now() # shortening this call

def poll():
    s.trigger()
    sleep(.05) # sleep in seconds - needed to allow registering of data to complete before reading
    write(s.humidity(), s.temperature())

def write(humidity, temperature):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    writer.writerow([now, str(humidity), int(temperature)])

with open('log.csv', 'a') as file:
    writer = csv.writer(file, lineterminator='\n')
    poll()

# cleaning up
s.cancel()
pi.stop()