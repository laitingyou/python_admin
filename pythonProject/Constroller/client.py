import socket;
websocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
class yousocket:
    def __init__(self,host,port):
        self.host=host
        self.port=port
        self.con()
    def con (self):
        try:
            websocket.connect((self.host, self.port))
            self.recv()
            self.close()
        except BaseException:
            print ('connect error')
    def recv(self):
        print(websocket.recv(1024) )
    def close (self):
        websocket.close()