import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from boolean import *
from player import *
from blackjack import *
import random
from tkinter import messagebox as mb



class new_game_parametrs:
    
    def __init__(self, master):
        
        
        self.slave = Toplevel(master)
        self.slave.title('Выберите параметры игры')
        self.slave.geometry('220x120+150+50')

        global Name, NumDeck
        Name=tk.StringVar()
        NumDeck=tk.IntVar()
        Name.set("Al") ###################
        NumDeck.set(2)

        self.lbl_name=Label(self.slave,text="Введите имя")
        self.ent_name=Entry(self.slave, textvariable=Name)
        self.lbl_numdeck=Label(self.slave, text="Введите кол-во колод")
        self.ent_numdeck=Entry(self.slave, textvariable=NumDeck)
        self.btn_begin=Button(self.slave, text="Начать", command=self.slave.destroy)
        self.lbl_name.pack()
        self.ent_name.pack()
        self.lbl_numdeck.pack()
        self.ent_numdeck.pack()
        self.btn_begin.pack()
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()
        self.begin_new_game()
                     
    def begin_new_game(self):
        if Name.get()!='' and NumDeck.get()!=0:
            name=Name.get()
            numdeck=NumDeck.get()
            return name, numdeck
        else:
            return("",0)
    
            
            
            

##    def return_numdeck(self):
##        numdeck=self.numdeck
##        return numdeck
##    def return_name(self):
##        name=self.name
##        return name
      

##      main_menu = Menu()
##      main_menu.add_command(label="Новая игра", command=self.game_table)
##      main_menu.add_command(label="Новая игра")#, command=)
##      main_menu.add_command(label="Выход",command=self.master.destroy)
##      self.frame_croupier=Frame(self.master, relief=SOLID)
##      self.frame_desk=Frame(self.master, relief=SOLID)
##      self.frame_player=Frame(self.master, relief=SOLID)


##      self.master.config(menu=main_menu)
##      self.master.protocol('WM_DELETE_WINDOW',self.exitMethod)
      
      
#      self.master.mainloop()
