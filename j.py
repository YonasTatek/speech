import tkinter as tk
import threading
import pyaudio
import wave
import time
import subprocess
from keyword_spotting_service import Keyword_Spotting_Service
class App():
    chunk = 1024 
    sample_format = pyaudio.paInt16 
    channels = 2
    fs = 44100  
    
    frames = []  
    def __init__(self, master):
        self.isrecording = False
        self.button1 = tk.Button(main, text='ጀምር',command=self.startrecording)
        self.button2 = tk.Button(main, text='ተው',command=self.stoprecording)
       

        self.button1.pack()
        self.button2.pack()

    def startrecording(self):
        self.p = pyaudio.PyAudio()  
        self.stream = self.p.open(format=self.sample_format,channels=self.channels,rate=self.fs,frames_per_buffer=self.chunk,input=True)
        self.isrecording = True
        
        print('Recording')
        t = threading.Thread(target=self.record)
        t.start()
    def s(self):
        kss = Keyword_Spotting_Service()
        keyword = kss.predict("h.wav")
        if keyword=="3":
            subprocess.run(["thunar", "/home"])
        elif keyword=="5":
            subprocess.run(["xfce4-taskmanager"])
        elif keyword=="8":
            subprocess.run(["xfce4-power-manager-settings"])
        elif keyword=="10":
            subprocess.run(["xfce4-keyboard-settings"])
        elif keyword=="13":
            subprocess.run(["xfce4-session-logout"])
      



            


          

    def stoprecording(self):
        self.isrecording = False
        print('recording complete')
       # self.filename=input('the filename?')
        # self.filename = self.filename+".wav"
        wf = wave.open("h.wav", 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(self.frames))
        wf.close()
        self.s()
       
    def record(self):
       
        while self.isrecording:
            data = self.stream.read(self.chunk)
            self.frames.append(data)
	

main = tk.Tk()
main.title('ካሶፒያ ኤአይ')
main.geometry("500x200")

app = App(main)
main.mainloop()

