import socket
import threading
from datetime import datetime

class Server:
    def __init__(self):
            self.ip = '127.0.0.1'
            while True:
                try:
                    self.port = 1234

                    self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.s.bind((self.ip, self.port))

                    break
                except:
                    print("Couldn't bind to that port")

            self.connections = []
            self.accept_connections()

    def accept_connections(self):
        self.s.listen(100)

        print('Running on IP: '+self.ip)
        print('Running on port: '+str(self.port))
        
        while True:
            c, addr = self.s.accept()
            self.connections.append(c)
            threading.Thread(target=self.handle_client,args=(c,addr,)).start()
        
    def broadcast(self, sock, data):
        for client in self.connections:
            if client != self.s and client != sock:
                try:
                    client.send(data)
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print(f'Data sent succesfully at time:{current_time} | FROM USER:{client}')
                except:
                    pass

    def handle_client(self,c,addr):
        while True:
            try:
                data = c.recv(1024)
                self.broadcast(c, data)
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                print(f'Data sent succesfully at time:{current_time} FOR ALL USERS')
            
            except socket.error:
                c.close()

server = Server()
