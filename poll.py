import pigpio
import csv
import datetime
from time import sleep
from pigpio_DHT22 import DHT22

# this connects to the pigpio daemon which must be started first
pi = pigpio.pi()

s = DHT22.sensor(pi, 4)
time = datetime.datetime.now()



def poll():
    s.trigger()
    sleep(.05) # Necessary on faster Raspberry Pi's
    write(s.humidity(), s.temperature())
    print('Humidity:' + '{:3.0f}'.format(s.humidity() / 1.) + '%')
    print('Temperature:' + '{:3.0f}'.format(s.temperature() / 1.) + 'c')

def write(humidity, temperature):
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    writer.writerow([now, str(humidity), int(temperature)])

with open('log.csv', 'w') as file:
    writer = csv.writer(file, lineterminator='\n')
    writer.writerow(['time', 'humidity', 'temperature'])
    poll()
    sleep(5)
    poll()
    
s.cancel()
pi.stop()