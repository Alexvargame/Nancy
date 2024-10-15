import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from boolean import *
from player import *
from blackjack import *
import random
from tkinter import messagebox as mb



class game_data:
    
    def __init__(self, master):
        
        
        self.slave = Toplevel(master)
        self.slave.title('Выберите параметры игры')
        self.slave.geometry('220x120+150+50')

        global  NumDeck, Bet
        NumDeck=tk.IntVar()
        Bet=tk.IntVar()
        Bet.set(10) 
        NumDeck.set(2)

        self.lbl_numdeck=Label(self.slave,text="Введите кол-во колод")
        self.ent_numdeck=Entry(self.slave, textvariable=NumDeck)
        self.lbl_bet=Label(self.slave, text="Введите размер ставки")
        self.ent_bet=Entry(self.slave, textvariable=Bet)
        self.btn_begin=Button(self.slave, text="Начать", command=self.slave.destroy)
        self.lbl_numdeck.pack()
        self.ent_numdeck.pack()
        self.lbl_bet.pack()
        self.ent_bet.pack()
        self.btn_begin.pack()
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()
        self.new_game_param()
                     
    def new_game_param(self):
        numdeck=NumDeck.get()
        bet=Bet.get()
        
        return numdeck, bet
            
            
            

