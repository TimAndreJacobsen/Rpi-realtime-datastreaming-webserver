import pigpio
from time import sleep
from pigpio_DHT22 import DHT22

# this connects to the pigpio daemon which must be started first
pi = pigpio.pi()

s = DHT22.sensor(pi, 4)

def poll():
    s.trigger()
    sleep(.05) # Necessary on faster Raspberry Pi's
    print('Humidity:' + '{:3.0f}'.format(s.humidity() / 1.) + '%')
    print('Temperature:' + '{:3.0f}'.format(s.temperature() / 1.) + 'c')

while True:
    poll()
    sleep(3)
    
s.cancel()
pi.stop()