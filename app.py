#importing neccessary libraries
from tkinter import *
import random as r
from pygame import  mixer
import pygame
from tkinter import filedialog
from lyrics_extractor import *
from tkinter import messagebox

#search engine id
# 5c14f8c1291b897b1
#api id 
# AIzaSyDo_8GZVuy35Si0pZySV3QZjQfIbT_wsHQ

#creating a class
class musixplayer():
    #initializing 
    mixer.init()
    pygame.init()

    def __init__(self,window):
        #variable for scale
        v1 = DoubleVar()
        window.title("musix player")
        window.geometry('500x350')
        window.resizable(0,0)
        #buttons
        Play = Button(window,text='►',width=10,bg='red',font=('Times'),command=self.play_method).pack(side="top")
        Pause = Button(window,text='║║',width=10,bg='blue',font=('Times'),command=self.pause_method).pack(padx=2,pady=8)
        unPause = Button(window,text='unpause',width=10,bg='green',font=('Times'),command=self.unpause_method).pack(padx=2,pady=9)
        Open = Button(window,text='open',width=10,bg='yellow',font=('Times'),command=self.open).pack(padx=2,pady=10)
        Lyrics = Button(window,text='lyrics',width=10,bg='orange',font=('Times'),command=self.get_lyrics).pack(padx=2,pady=11)
        #scale
        vol = Scale(root,variable=v1,from_=10,to=1,orient=VERTICAL,command=self.voladj).pack(anchor="nw")
    #methods for buttons
    def play_method(self):
        try:
            mixer.music.play()
        except Exception as e:
            messagebox.showerror("error",e)

    def pause_method(self):
        mixer.music.pause()
    
    def unpause_method(self):
        mixer.music.unpause()
    
    def open(self):
        open = filedialog.askopenfile()
        mixer.music.load(open)
    
    def get_lyrics(self):
        pass
    
    def voladj(self,val):
        mixer.music.set_volume((float(val))/10)

if __name__ == "__main__":
    root = Tk()
    app = musixplayer(root)
    root.mainloop()
