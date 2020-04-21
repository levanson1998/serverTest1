import socketio


sio = socketio.Client()

@sio.on('connect')
def on_connect():
	print("I'm connected!")
	sio.emit('user2-on',True)		

@sio.on('suitcase-send-status-ok')
def on_message(data):
	print('Server has received your data')
	sioIsConnected=True

@sio.on('suitcase-send-img-ok')
def on_message(data):
	print('Server has received your image')

@sio.on('disconnect')
def on_disconnect():
	try:
		sio.connect("http://localhost:8888/")
	except:
		print("I'm disconnected")

sio.connect("http://localhost:8888/")
print('my sid is', sio.sid)