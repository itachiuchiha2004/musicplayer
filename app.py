#importing neccessary libraries
from ctypes import memmove
from email.mime import image
from logging import exception
from msilib.schema import Binary, Directory
from platform import platform
from timeit import repeat
from tkinter import *
import random as r
from turtle import bgcolor, width, window_height
from unittest.mock import seal
from numpy import binary_repr
from pygame import  mixer
import pygame
from tkinter import filedialog
import os
import tkinter.ttk as ttk
#from lyrics_extractor import *
import os
from PIL import Image
#from tkinter.ttk import 
import tkinter.messagebox as mb

#init
mixer.init()    
#state var
repeat_state = False
play_state = False
shuffle_state = False
con_style = 'rep_one'
default_music_folder = [r'music\Copines.mp3',r'music\Run Free (feat._IVIE).mp3',r'music\Silhouette.mp3',r'music\Zenzenzense.mp3',r'music\インフェルノ（Inferno）.mp3',r'music\Ik Vaari Aa.mp3',r'music\Kasoor.mp3',r'music\Lonely.mp3',r'music\Mai Ni Meriye.mp3',r'music\Main Tera Boyfriend.mp3',r'music\Noor.mp3',r'music\Photo.mp3']
default_music_folder =  sorted(default_music_folder)


class musixplayer:    
    #methods
    def repeat_method(self):
        global repeat_state
        if repeat_state == False:
            Repeat_btn['image']=Repeat_img2
            repeat_state = True
        else:
            Repeat_btn['image']=Repeat_img1
            repeat_state = False
    
    def play_method(self):
        global play_state
        if play_state == False:
            Play_btn['image']=Pause_img
            play_state = True
        elif play_state == True:
            Play_btn['image']=Play_img
            play_state = False

    #about
    def about(self):
        mb.showinfo('About','This is an exclusive distribution of Musix Player.\n Creator of this apllication is Ganesh Pawar.\nThis was completed on 23/6/2019.\n Thanks For Using The Application.')
    
    def playSongInitial(self, *args):
        self.stop()
        self.play_music()


    def open_file(self):
        dir_ = filedialog.askopenfilename(initialdir='D:/',title='Select File')
        cng_dir = dir_.split('/')[0:-1]
        cng_dir = ''.join(cng_dir)
        os.chdir(cng_dir)
        self.songs.append(dir_)
        filename = os.path.basename(dir_)
        play_list.insert(END,filename)
        global playing
        playing = False


    def set_playlist(self):
        music_ex = ['mp3','wav','mpeg','m4a','wma','ogg']
        dir_ =  filedialog.askdirectory(initialdir='D:\\',title='Select Directory')
        os.chdir(dir_)
        dir_files = os.listdir(dir_)
        self.songs = []
        for file in dir_files:
            exten = file.split('.')[-1]
            for ex in music_ex:
                if exten == ex:
                    play_list.insert(END,file)
                    self.songs.append(file)

    def __init__(self):
        window = Tk()
        window.title("musix player")
        #window.resizable(0,0)
        window.config(bg='gray85')
        window.geometry('1150x650')
        #Labels
        side_bar = Label(window,text='', bg='light grey',height=33,width=10,relief_='ridge')
        side_bar.place(x=0,y=0)
        music_info_bar = Label(window,text='', bg='gray69',height=11,width=164,relief_='ridge')
        music_info_bar.place(x=0,y=501)

        
        #images
        global Search_img
        Search_img = PhotoImage(file=r'C:\Users\User\Desktop\music prject\Resources\search.png')
        Search_img = Search_img.subsample(12)
        global Play_img
        Play_img = PhotoImage(file=r'C:\Users\User\Desktop\music prject\Resources\375.png')
        Play_img = Play_img.subsample(6)
        global Pause_img
        Pause_img = PhotoImage(file=r'C:\Users\User\Desktop\music prject\Resources\pause.png')
        Pause_img = Pause_img.subsample(6)
        global Next_img
        Next_img = PhotoImage(file=r'C:\Users\User\Desktop\music prject\Resources\next1.png')
        Next_img = Next_img.subsample(6)
        global Prev_img
        Prev_img = PhotoImage(file=r'C:\Users\User\Desktop\music prject\Resources\prev.png')
        Prev_img = Prev_img.subsample(6)
        global Shuffle_img
        Shuffle_img = PhotoImage(file=r'C:\Users\User\Desktop\music prject\Resources\shuffe.png')
        Shuffle_img = Shuffle_img.subsample(6)
        global Repeat_img2
        Repeat_img2 = PhotoImage(file=r'C:\Users\User\Desktop\music prject\Resources\repeat1.png')
        Repeat_img2 = Repeat_img2.subsample(6)
        global Repeat_img1
        Repeat_img = PhotoImage(file=r'C:\Users\User\Desktop\music prject\Resources\repeat.png')
        Repeat_img1 = Repeat_img.subsample(6)

        #progress bar
        prog_bar = ttk.Progressbar(window, orient = HORIZONTAL,length = 1100)
        prog_bar.place(x=10,y=510)
        prog_bar['value'] = 20


        ## Volume Scale - adjust volume
        global scale
        scale = ttk.Scale(window, from_=0, to=100, orient=HORIZONTAL)
        scale.set(70)  # implement the default value of scale when music player starts
        mixer.music.set_volume(0.7)
        scale.place(x=915,y=550)

        #btn
        global Search_btn
        Search_btn = Button(side_bar,borderwidth=0,text='btn',width=45,image=Search_img,bd=0,bg='light grey')
        Search_btn.image = Search_img
        Search_btn.place(x=12,y=15)
        global Play_btn
        Play_btn = Button(window,borderwidth=0,text='btn',width=90,image=Play_img,command=self.play_method,bd=0,bg='gray69')
        Play_btn.image = Play_img
        Play_btn.place(x=200,y=550)
        global Next_btn
        Next_btn = Button(window,borderwidth=0,text='btn',image=Next_img,width=90,bg='gray69')
        Next_btn.image = Next_img
        Next_btn.place(x=290,y=550)
        global Prev_btn
        Prev_btn = Button(window,borderwidth=0,text='btn',image=Prev_img,width=90,bg='gray69')
        Prev_btn.image = Prev_img
        Prev_btn.place(x=110,y=550)
        global Repeat_btn
        Repeat_btn = Button(window,borderwidth=0,text='btn',image=Repeat_img1,command=self.repeat_method,width=90,bg='gray69')
        Repeat_btn.image = Repeat_img1
        Repeat_btn.place(x=390,y=550)
        global Shuffle_btn
        Shuffle_btn = Button(window,borderwidth=0,text='btn',image=Shuffle_img,width=90,bg='gray69')
        Shuffle_btn.image = Shuffle_img
        Shuffle_btn.place(x=10,y=550)

        
        ## Time Durations
        global dur_start, dur_end
        dur_start = Label(window, text='--:--',font=('Calibri',10,'bold'),bg='gray69')
        dur_start.place(x=7,y=510)
        dur_end = Label(window, text='--:--',font=('Calibri',10,'bold'),bg='gray69')
        dur_end.place(x=1103,y=510)

        global play_list
        play_list = Listbox(window,height=31,width=69,bg='gray69')
        play_list.place(x=749,y=2)
        play_list.bind("<Double-1>",self.play_method())
        for names in default_music_folder:
            i = 1
            play_list.insert(i,names[6:][:-4])
            i += 1  
        


        #window.protocol("WM_DELETE_WINDOW", .exit)
        window.mainloop()
        

if __name__ == '__main__':
    app = musixplayer()
