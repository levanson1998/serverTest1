import socketio
from time import sleep
import datetime
import base64

isTracking=0
timerLost=2.0

sio = socketio.Client()

@sio.on('connect')
def on_connect():
	print("I'm connected!")
	sio.emit('car-on',True)		

@sio.on('car-send-status-ok')
def on_message(data):
	print('Server has received your data')
	sioIsConnected=True

@sio.on('car-send-img-ok')
def on_message(data):
	print('Server has received your image')

@sio.on('disconnect')
def on_disconnect():
	try:
		sio.connect("https://supercuteboy.herokuapp.com/")
	except:
		print("I'm disconnected")

sio.connect("https://supercuteboy.herokuapp.com/")
print('my sid is', sio.sid)
sleep(5)

mydict = {"isTracking": isTracking, "lostTime": timerLost}
sio.emit('car-send-status', mydict)
sleep(5)

with open("./image.jpg","rb") as file:
    jpg_as_text = base64.b64encode(file.read())
capturedTime = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
mydict_img = {"Image": "data:image/jpg;base64," + jpg_as_text.decode("utf-8"), "CapTime":capturedTime}
sio.emit('car-send-img', mydict_img)
