from time import sleep
from client3 import sioProcess

speed=200
isTracking = 1

while True:
    isTracking = 1
    sioProcess(isTracking)
    sleep(20)
    isTracking = 0
    sioProcess(isTracking)
    sleep(20)
    isTracking = -1
    sioProcess(isTracking)
    sleep(20)