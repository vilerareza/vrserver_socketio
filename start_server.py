import socketio
import eventlet

sio = socketio.Server()
app = socketio.WSGIApp(sio)

frames = {}

class ConnectionNameSpace(socketio.Namespace):

    def __init__(self, namespace=None):
        super().__init__(namespace)
        print (self.namespace)

    def on_connect(self, sid, environ):
        print('connected')
        print (self.namespace)

    def on_disconnect(self, sid):
        pass

    def on_frame(self, sid, data):
        print ('frame')
        #self.emit('my_response', data)

device1 = ConnectionNameSpace('/device1')
device2 = ConnectionNameSpace('/device2')
sio.register_namespace(device1)
sio.register_namespace(device2)

eventlet.wsgi.server(eventlet.listen(('', 8000)), app)