from time import sleep
from client import sioProcess

speed=200
isTracking = 1

while True:
    isTracking = 1
    sioProcess(isTracking, speed)
    sleep(5)
    isTracking = 0
    sioProcess(isTracking, speed)
    sleep(5)