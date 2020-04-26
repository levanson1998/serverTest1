import socketio
from time import sleep
import datetime
import base64

isTracking=0
timerLost=2.0
url_heroku = "https://supercuteboy.herokuapp.com/"
status = "Run"
speed = 1.0

sio = socketio.Client()

@sio.on('connect')
def on_connect():
	print("I'm connected!\n")
	sio.emit('car-on',True)		

@sio.on('car-send-stt-ok')
def on_message(data):
	print('Server has received your status\n')

@sio.on('car-send-img-ok')
def on_message1(data):
	print('Server has received your image\n')

@sio.on('request_img')
def sioSendPicTime():
	pic = capturePic()
	capturedTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
	mydict_img = {"Image": "data:image/jpg;base64," + pic.decode("utf-8"), "CapTime":capturedTime}
	sio.emit('car-send-img', mydict_img)

@sio.on('requestStatus')
def sioSendStt():
	global status, speed
	mydict = {"status":status,"speed":speed}
	sio.emit("car-send-stt", mydict)

@sio.on('disconnect')
def on_disconnect():
	try:
		sio.connect(url_heroku)
	except:
		print("I'm disconnected !")

sio.connect(url_heroku)
print('my sid is: ', sio.sid)

# # goi hinh anh va datetime tu raspi
# def sioSendPicTime():
# 	pic = capturePic()
# 	capturedTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# 	mydict_img = {"Image": "data:image/jpg;base64," + pic.decode("utf-8"), "CapTime":capturedTime}
# 	sio.emit('car-send-img', mydict_img)

# chup hinh anh tu camera
def capturePic():
	with open("./image.jpg","rb") as file:
		jpg_as_text = base64.b64encode(file.read())
	return jpg_as_text

# goi toc do


# main of client.py
def sioProcess(isTracking):
	global status, speed
	if (isTracking==1):
		speed = 3.5
		status = "Run"
	elif (isTracking==0):
		speed = 0.0
		status = "Stop"
	elif (isTracking==-1):
		speed = 0.0
		status = "Lost"

# sleep(10)

# mydict = {"isTracking": isTracking, "lostTime": timerLost}
# sio.emit('car-isTracking', mydict)
# sleep(10)

# with open("./image.jpg","rb") as file:
# 	jpg_as_text = base64.b64encode(file.read())
# capturedTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# mydict_img = {"Image": "data:image/jpg;base64," + jpg_as_text.decode("utf-8"), "CapTime":capturedTime}
# sio.emit('car-send-img', mydict_img)

