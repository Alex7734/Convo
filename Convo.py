import socket
import threading
import pyaudio
import tkinter as tk

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            self.target_ip = '172.104.157.235'
            self.target_port = 6969
            self.s.connect((self.target_ip, self.target_port))
        except:
            pass

        chunk_size = 1024 
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 20000

        self.p = pyaudio.PyAudio()
        self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size)
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)

    def receive_server_data(self):
        while not isClosed:
            if not isDeafen:
                try:
                    data = self.s.recv(1024)
                    self.playing_stream.write(data)
                except:
                    pass


    def send_data_to_server(self):
        while not isClosed:
            if not isDeafen:
                if not isMute:
                    try:
                        data = self.recording_stream.read(1024)
                        self.s.sendall(data)
                    except:
                        pass

client = Client()
isMute = False
isDeafen = False

def connect():
    receive_thread = threading.Thread(target=client.receive_server_data).start()
    sending_thread = threading.Thread(target=client.send_data_to_server).start()

def goMute():
    global isMute
    if isMute == False:
        isMute = True
    else:
        isMute = False

def goDeafen():
    global isDeafen
    if isDeafen == False:
        isDeafen = True
    else:
        isDeafen = False

def quit():
    root.destroy()
    isClosed = True


root = tk.Tk()
root.geometry("240x80")
root.title("Convo")
root.resizable(False, False)
frame = tk.Frame(root)
frame.pack()

join = tk.Button(frame, text="Join", fg="blue", command=connect)
join.grid(row=1, column=1, padx=5, pady=5)

button = tk.Button(frame, text="Quit", fg="red", command=quit)
button.grid(row=2, column=1, padx=5, pady=5)

mute = tk.Button(frame, text="Mute", fg="grey", command=goMute)
mute.grid(row=1, column=2, padx=5, pady=5)

deafen = tk.Button(frame, text="Deafen", fg="grey", command=goDeafen)
deafen.grid(row=2, column=2, padx=5, pady=5)

isClosed = False
root.mainloop()
isClosed = True


