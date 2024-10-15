import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter.scrolledtext import ScrolledText



class rules:
    
    def __init__(self, master):
        
        
        self.slave = Toplevel(master)
        self.slave.title('Правила игры')
        self.slave.geometry('400x300+150+150')
        self.rules_text=ScrolledText(self.slave,wrap='word', height=100)
        self.rules()

       
                     
    def rules(self):
        with open("rules",'r') as file:
         rules=file.read()
        
         self.rules_text.insert('1.0', rules)
         self.rules_text.pack(side=TOP,fill=BOTH)
        
        
            
            
            

