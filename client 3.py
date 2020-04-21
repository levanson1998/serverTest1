import socketio
from time import sleep
import datetime
import base64

isTracking=0
timerLost=2.0

sio = socketio.Client()

@sio.on('connect')
def on_connect():
	print("I'm connected!\n")
	sio.emit('car-on',True)		

@sio.on('car-send-speed-ok')
def on_message(data):
	print('Server has received your speed\n')
	sioIsConnected=True

@sio.on('car-send-img-ok')
def on_message(data):
	print('Server has received your image\n')

@sio.on('disconnect')
def on_disconnect():
	try:
		sio.connect("http://localhost:8888/")
	except:
		print("I'm disconnected !")

sio.connect("http://localhost:8888/")
print('my sid is: ', sio.sid)

# goi hinh anh va datetime tu raspi
def sioSendPicTime():
	pic = capturePic()
	capturedTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	mydict_img = {"Image": "data:image/jpg;base64," + pic.decode("utf-8"), "CapTime":capturedTime}
	sio.emit('car-send-img', mydict_img)

# chup hinh anh tu camera
def capturePic():
	with open("./image.jpg","rb") as file:
		jpg_as_text = base64.b64encode(file.read())
	return jpg_as_text

# goi toc do
def sioSendSp(speed):
	mydict = {"Speed":speed}
	sio.emit("car-speed", mydict)

# main of client.py
def sioProcess(isTracking, speed):
	if (isTracking==1):
		sioSendSp(speed)
	elif (isTracking==0):
		sioSendPicTime()

# sleep(10)

# mydict = {"isTracking": isTracking, "lostTime": timerLost}
# sio.emit('car-isTracking', mydict)
# sleep(10)

# with open("./image.jpg","rb") as file:
# 	jpg_as_text = base64.b64encode(file.read())
# capturedTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# mydict_img = {"Image": "data:image/jpg;base64," + jpg_as_text.decode("utf-8"), "CapTime":capturedTime}
# sio.emit('car-send-img', mydict_img)

