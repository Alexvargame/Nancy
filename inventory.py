import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from boolean import *

import random
from tkinter import messagebox as mb



class Inventory:
    
    def __init__(self, master, player):
        
        self.player = player
        print('INVENT', self.player)
        self.slave = Toplevel(master)
        self.slave.title(f'Инвентарь {self.player.name}')
        self.slave.geometry('320x220+300+50')

        self.inventory_frame = tk.Frame(self.slave)
        self.inventory_frame.pack(padx=10, pady=10, fill=BOTH)
        print('PLAy_INV', self.player, self.player.pl_items)
        print(len(self.player.pl_items))
        width = 4
        height = len(self.player.pl_items)//width+1
        # print(len(self.player.items), height )
        for i in range(width): self.inventory_frame.columnconfigure(index=i, weight=1)
        for j in range(height): self.inventory_frame.rowconfigure(index=j, weight=1)
        count = 0
        for i in range(width):
            for j in range(height):
                if count >= len(self.player.pl_items):
                    break
                print('ITEM', self.player.pl_items[count], self.player.pl_items[count].__class__.__name__)
                print(self.player.pl_items[count], self.player.pl_items[count].count)
                #if self.player.pl_items[count].count > 0:
                btn = tk.Button(self.inventory_frame, text=f'{self.player.pl_items[count]}:{self.player.pl_items[count].count}', cursor="arrow", borderwidth=1,
                                        width=4, height=2)
                btn.bind('<Button-1>', lambda e, itm=self.player.pl_items[count]:  self.print_item(e, itm))
                btn.bind('<Button-3>', lambda e, itm=self.player.pl_items[count]: self.get_description(e, itm))
                btn.grid(column=i, row=j)
                count += 1
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()
    #     self.new_game_param()
    #
    # def new_game_param(self):
    #     numdeck=NumDeck.get()
    #     bet=Bet.get()
    #
    #     return numdeck, bet
    def print_item(self,e,itm):
        print(e.widget.grid_info)
        print('DESC',itm.description)
            
    def get_description(self,e,itm):
        Description(self.slave,itm)

class Description:
    def __init__(self, slave, itm):
        self.itm = itm
        #print('INVENT', self.player)
        self.slave = Toplevel(slave)
        self.slave.title(f'Описание {self.itm.description}')
        self.slave.geometry('320x220+300+50')

        self.description_lbl = tk.Label(self.slave, text=self.itm.description)
        self.description_lbl.pack()
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()
