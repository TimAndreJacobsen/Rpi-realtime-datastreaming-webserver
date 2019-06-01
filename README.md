# Realtime datastreaming with a raspberrypi
Raspberry Pi server collecting data from a [DHT22 sensor](https://learn.adafruit.com/dht/overview)(humidity and temperature) and streaming video. Can handle up to 100 connections, but due to hardware limitations can only handle 5 simultaneous streams at 1080p 24fps. Stream quality can be dropped to increase viewer count. To prevent blocking the server implements coroutines using [Gevent](http://www.gevent.org/) instead of a multithreading solution.

### How it works
The raspberry pi runs a python script regularly polling the sensor for information. This information is inserted into a SQLite database. When a connection is established the Flask server sends a query to the database. If no specific time period is requested, Flask will use a predetermined default. This is sent through a query string in the URL. There are also a number of interface options for quickly selecting a time period.
click [here](https://github.com/TimAndreJacobsen/Rpi-streaming-webserver#demo-of-functionality) for a demo.

The server also has a camera attached and upon receiving a request, it will start up the camera and create a video feed using motion-jpeg. This raised issues of blocking. After trying both multithreading and coroutines I landed on using coroutines for it's superior performance. The Gevent event loop solved the blocking issues and allowed to have up to 5 viewers at the same time without any slowdown. click [here](https://github.com/TimAndreJacobsen/Rpi-streaming-webserver/blob/master/assets/concurrency.gif) for a demo of concurrency.

## Tech stack
- Python 3.7
- Flask
- uWSGI
- NGINX
- SQLite3
- Skeleton (CSS Boostrap)

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

## Demo of functionality
![](https://github.com/TimAndreJacobsen/Rpi-streaming-webserver/blob/master/assets/demo.gif)
