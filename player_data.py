import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from boolean import *

from models import Player

class player_data:
    
    def __init__(self, master):
        
        
        self.slave = Toplevel(master)
        self.slave.title('Выберите игрока')
        self.slave.geometry('320x120+150+50')

        global Name
        Name=tk.StringVar()     
        Name.set("Alex") 
       
        self.lbl_name = Label(self.slave,text="Введите имя")
        self.ent_name = Entry(self.slave, textvariable=Name)
        self.btn_begin = Button(self.slave, text="Начать", command=self.slave.destroy)
        # self.lbl_name_new = Label(self.slave, text="Новый игрок")
        # self.ent_name_new = Entry(self.slave, textvariable=Name)
        #
        # self.btn_begin_new = Button(self.slave, text="Зарегистрироваться", command=self.slave.destroy)
        self.lbl_name.pack()
        self.ent_name.pack()
        self.btn_begin.pack()
        # self.lbl_name_new.pack()
        # self.ent_name_new.pack()
        # self.btn_begin_new.pack()
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()
        self.new_player_name()
                     
    def new_player_name(self):
        name=Name.get()
        if Player.find_by_name(name):
            return name
        else:
            Player.add(name)
            return name
            
            
            

