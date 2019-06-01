# Realtime datastreaming with a raspberrypi
Raspberry Pi server collecting data from a [DHT22 sensor](https://learn.adafruit.com/dht/overview)(humidity and temperature) and streaming video. Can handle up to 100 normal connections, but due to hardware limitations can only handle 5 simultaneous streams at 1080p 24fps. Stream quality can be dropped to increase viewer count. To prevent blocking the server implements coroutines using [Gevent](http://www.gevent.org/).

## Tech stack
- Python 3.7
- Flask
- uWSGI
- NGINX
- SQLite3

## Functionality
- streaming live video feed
- streaming live sensor readings
- plotting historic temperature & humidity

## API's
- Google Charts

## Hardware
- Raspberry Pi 3b +
- DHT22 AM2302 Sensor
- Raspberry Pi Camera Module v2
