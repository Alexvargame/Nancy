import tkinter as tk
import tkinter.ttk as ttk
import os
import random
import importlib
from time import sleep
from tkinter import messagebox as mb

import PIL.Image
import PIL.ImageTk

from boolean import *
from player_data import *

from inventory import *
from rules import *
from models import Type_Item, Item, Player

class Main:
   def __init__(self, master):
      self.master = master
      self.master.title('Nancy')
      self.master.geometry('1000x620+300+50')
      self.player = Player.find_by_name("Alex")

      self.DIALOG_PLAYER_STATUS = 0
      self.DIALOG_BOT_STATUS = 0
      self.DIALOG_SAFE_STATUS = 1
      self.ACTION_STATUS = {}
      self.DIALOG_STATUS_DICT ={}

      self.frame_dialog_window=Frame(self.master, relief=SOLID, borderwidth=1)
      self.frame_tools_window=Frame(self.master, relief=SOLID, borderwidth=1)

      self.frame_main_game_window = Frame(self.frame_dialog_window, relief=SOLID, borderwidth=1)

      
      #self.frame_menu=Frame(self.master, relief=SOLID)
      self.frame_dialog_window.pack(pady=3, side='top', padx=10, fill=BOTH,expand=1)
      self.frame_tools_window.pack(pady=3, side='bottom', padx=10, fill=BOTH,expand=0)
      for c in range(5): self.frame_tools_window.columnconfigure(index=c, weight=1)
      #self.frame_tools_window.columnconfigure(0, pad=3)
      self.frame_main_game_window.pack(fill=BOTH,expand=1)
      print(self.frame_main_game_window['background'])

      self.master.protocol('WM_DELETE_WINDOW', self.exitMethod)
      self.menu_panel()
      #print(self.player.save_location)
      self.game_window()#self.player.save_location)
      self.master.mainloop()

   def menu_panel(self):#, player):
      main_menu = Menu()
      main_menu.add_command(label="Новая игра", command=self.get_player)
      #if player.name!='Alex':
      # for widget in self.frame_dialog_window.winfo_children():
      #    widget.destroy()
      # for widget in self.frame_tools_window.winfo_children():
      #    widget.destroy()
         # for widget in self.frame_menu.winfo_children():
         #    widget.destroy()
         #
         # self.begin_btn=ttk.Button(self.frame_menu, width=15, text="Начать раздачу", command=self.clean_table)
         # self.begin_btn.pack(side=LEFT, ipady=10, padx=20, pady=20)
         # self.choice_btn_2=ttk.Button(self.frame_menu, text='Стоп', command=self.no_card)
         # self.choice_btn_2.pack()
      main_menu.add_command(label="Параметры игры")#,command=self.new_param)
      main_menu.add_command(label="Правила игры")#,command=self.rules)
      main_menu.add_command(label="Выход", command=self.master.destroy)
      self.master.config(menu=main_menu)
      
   def get_player(self):

      player_data(self.master)
      #self.player.name=player_data.new_player_name(self)
      #self.player = Player.find_by_name(player_data.new_player_name(self))
      self.player = Player.find_by_name(player_data.new_player_name(self))
      print('SPL', self.player, self.player.save_location)
      self.game_window(self.player.save_location)
      return self.player
   #
   # def new_param(self):
   #
   #    game_data(self.master)
   #    self.n, self.bet=game_data.new_game_param(self)
   #    if all(game_data.new_game_param(self)):
   #       self.card_deck, self.card_deck_dict=get_deck(self.n)
   #       self.clean_table()
   #    else:
   #       game_data(self.master)
   #
   #
   def clean_table(self):
      for widget in self.frame_tools_window.winfo_children():
            widget.destroy()
      for widget in self.frame_dialog_window.winfo_children():
            widget.destroy()
      # for widget in self.frame_player.winfo_children():
      #       widget.destroy()
      # self.choice_btn_2=ttk.Button(self.frame_menu, text='Стоп',width=15, command=self.no_card)
      # self.choice_btn_2.pack(side=RIGHT, ipady=10, padx=20, pady=20)
      #self.game_window()#'locations.location_2')
  
##
   def game_window(self, loc='locations.location_0'):

      loc = loc.strip('\r''\n')
      imp_mod = importlib.import_module(loc)#'locations.location_2')
      if imp_mod.THE_BACKGROUND:
         img = PIL.Image.open(imp_mod.THE_BACKGROUND)
         img = img.resize((980, 600), PIL.Image.Resampling.LANCZOS)
         self.frame_main_game_window.image = PIL.ImageTk.PhotoImage(img)  # file = 'images/1588.png')
         self.im_logo = Label(self.frame_main_game_window, text='dsgfwg', image=self.frame_main_game_window.image)
         self.im_logo.place(relx=0, rely=0)

      objects = imp_mod.THE_OBJECTS
      dialogs = imp_mod.THE_DIALOGS
      next_loc = imp_mod.THE_NEXT_LOCATION
      print('dial_obj', dialogs, objects)
      self.DIALOG_STATUS_DICT = dict.fromkeys(dialogs['PLAYER_DIALOG'].keys(), {'player': None, 'bot': None})
      self.ACTION_STATUS = dict.fromkeys([d for d in dialogs.keys() if d != 'PLAYER_DIALOG' and 'BOT' not in d], None)
      for i in range(30): self.frame_main_game_window.columnconfigure(index=i, weight=1)
      for j in range(20): self.frame_main_game_window.rowconfigure(index=j,weight=1)

      for b in objects['THE_BOT'].keys():
         btn = tk.Button(self.frame_main_game_window, text=objects['THE_BOT'][b]['name'], cursor="circle",
                         borderwidth=0, state=objects['THE_BOT'][b]['state']) # , width=2,height=1)
         # btn=ttk.Button(self.frame_main_game_window, text=f'{i}:{j}',cursor= "circle")
         btn.bind('<Button-1>', lambda e, bot=b, dialogs= dialogs: self.bot_dialog(e, bot, dialogs))
         #btn.bind('<Button-1>', self.bot_dialog)
         btn.grid(column=objects['THE_BOT'][b]['location'][0], row=objects['THE_BOT'][b]['location'][1],
                  columnspan=objects['THE_BOT'][b]['width'], rowspan=objects['THE_BOT'][b]['height'], sticky='nsew')
         #btn.place(relx=objects['THE_BOT'][b]['location'][0], rely=objects['THE_BOT'][b]['location'][1])
      for b in objects['THE_FURNITURE'].keys():
         btn = tk.Button(self.frame_main_game_window, text=objects['THE_FURNITURE'][b]['name'], cursor="circle",
                         borderwidth=1, state=objects['THE_FURNITURE'][b]['state'])
         btn.bind('<Button-1>', lambda e, bot=b, next_loc=next_loc, dialogs = dialogs: self.furniture_dialog(e, bot, dialogs, next_loc))
         btn.grid(column=objects['THE_FURNITURE'][b]['location'][0], row=objects['THE_FURNITURE'][b]['location'][1],
                  columnspan=objects['THE_FURNITURE'][b]['width'], rowspan=objects['THE_FURNITURE'][b]['height'], sticky='nsew')

      self.frame_tools_window_segment_1 = Frame(self.frame_tools_window, borderwidth=1)
      for c in range(3): self.frame_tools_window_segment_1.columnconfigure(index=c, weight=1)
      self.frame_tools_window_segment_2 = Frame(self.frame_tools_window, relief=SOLID,borderwidth=1)
      for c in range(1): self.frame_tools_window_segment_2.columnconfigure(index=c, weight=1)
      self.frame_tools_window_segment_3 = Frame(self.frame_tools_window, relief=SOLID,borderwidth=1)
      for c in range(3): self.frame_tools_window_segment_3.columnconfigure(index=c, weight=1)
      self.frame_tools_window_segment_1.grid(row=0, column=0, sticky='ew')
      self.frame_tools_window_segment_2.grid(column=1, row=0, sticky='ew',columnspan=3)
      self.frame_tools_window_segment_3.grid(column=4, row=0, sticky='ew')

      #self.main_game_window_lbl = ttk.Label(self.frame_main_game_window, text='DIALOG',background="lightgreen", anchor='center')

      self.tool_segment_1_btn_1 = ttk.Button(self.frame_tools_window_segment_1, text='Инвентарь', command=self.get_player_invetory)
      self.tool_segment_1_btn_2 = ttk.Button(self.frame_tools_window_segment_1, text='2')
      self.tool_segment_1_btn_3 = ttk.Button(self.frame_tools_window_segment_1, text='3')

      self.tool_segment_2_lbl = ttk.Label(self.frame_tools_window_segment_2, text='Ответы', anchor='center', background="lightblue",)

      self.tool_segment_3_btn_1 = ttk.Button(self.frame_tools_window_segment_3, text='1')
      self.tool_segment_3_btn_2 = ttk.Button(self.frame_tools_window_segment_3, text='2')
      self.tool_segment_3_btn_3 = ttk.Button(self.frame_tools_window_segment_3, text='3')

      #self.main_game_window_lbl.pack(fill=BOTH,expand=1)

      self.tool_segment_1_btn_1.grid(column=0, row=0, sticky='ew')
      self.tool_segment_1_btn_2.grid(column=1, row=0, sticky='ew')
      self.tool_segment_1_btn_3.grid(column=2, row=0, sticky='ew')

      self.tool_segment_2_lbl.grid(sticky='ew')

      self.tool_segment_3_btn_1.grid(column=0, row=0, sticky='ew')
      self.tool_segment_3_btn_2.grid(column=1, row=0, sticky='ew')
      self.tool_segment_3_btn_3.grid(column=2, row=0, sticky='ew')


   def print_coord(self, event):
      grid_info=event.widget.grid_info()
      self.tool_segment_2_lbl.config(text=f'{grid_info["column"]}:{grid_info["row"]}')


   def bot_dialog(self, event, bot, dialogs):
      if event.widget.configure('state')[-1] == 'disabled':
         self.tool_segment_2_lbl.config(text='Ищите дальше')
         self.tool_segment_2_lbl.update()
         print('Ищите дальше')
      elif self.DIALOG_STATUS_DICT[bot]['player'] and len(dialogs['PLAYER_DIALOG'][bot]['state'])<=self.DIALOG_STATUS_DICT[bot]['player']:
         self.tool_segment_2_lbl.config(text='Ничего интересного больше нет!')
         print('Ничего интересного больше нет!')
         self.tool_segment_2_lbl.update()
      else:
         dialog_key = bot.upper()+'_DIALOG'
         print('KEY', dialogs[dialog_key])
         print('PLAY', dialogs['PLAYER_DIALOG'][bot])
         if not self.DIALOG_STATUS_DICT[bot]['player'] or not self.DIALOG_STATUS_DICT[bot]['bot']:
            self.DIALOG_STATUS_DICT[bot] = {'player': 0, 'bot': 0}
         self.DIALOG_STATUS_DICT[bot]['player'] += 1

         if dialogs['PLAYER_DIALOG'][bot]['state'].get(self.DIALOG_STATUS_DICT[bot]['player']):
            print(dialogs['PLAYER_DIALOG'][bot]['state'][self.DIALOG_STATUS_DICT[bot]['player']]['text'])
            self.tool_segment_2_lbl.config(text=dialogs['PLAYER_DIALOG'][bot]['state'][self.DIALOG_STATUS_DICT[bot]['player']]['text'])
            self.tool_segment_2_lbl.update()
         sleep(1)
         if self.DIALOG_STATUS_DICT[bot]['player']-self.DIALOG_STATUS_DICT[bot]['bot'] == 1:
            self.DIALOG_STATUS_DICT[bot]['bot'] += 1
            if dialogs[dialog_key]['state'].get(self.DIALOG_STATUS_DICT[bot]['bot']):
               print('D@@@',dialogs[dialog_key]['state'][self.DIALOG_STATUS_DICT[bot]['bot']]['text'][0])
               self.tool_segment_2_lbl.config(text=dialogs[dialog_key]['state'][self.DIALOG_STATUS_DICT[bot]['bot']]['text'][0])
               if len(dialogs[dialog_key]['state'][self.DIALOG_STATUS_DICT[bot]['bot']]['text']) > 1:
                  furni_name = dialogs[dialog_key]['state'][self.DIALOG_STATUS_DICT[bot]['bot']]['text'][1]
                  er = [w for w in self.frame_main_game_window.winfo_children() if w.configure('text')[-1]=='_'.join(furni_name.split('_')[:-1])][0]
                  #print('2131',er.configure('state'))
                  self.ACTION_STATUS[furni_name] = dialogs[dialog_key]['state'][self.DIALOG_STATUS_DICT[bot]['bot']]['act']
                  print(self.ACTION_STATUS[furni_name])
                  event.widget.configure(state=['disabled'])
                  print('223', event.widget.configure('state'))
                  event.widget.update()

   def furniture_dialog(self,event, bot, dialogs, next_loc):
      print('SBD', bot, dialogs)
      dialog_key = bot.upper() + '_DIALOG'
      print(dialog_key)
      if not self.ACTION_STATUS[dialog_key]:
         self.ACTION_STATUS[dialog_key] = 0
         self.tool_segment_2_lbl.config(text=dialogs[dialog_key]['state'][self.ACTION_STATUS[dialog_key]]['text'])
      elif self.ACTION_STATUS[dialog_key] == 1:
         door = [w for w in self.frame_main_game_window.winfo_children() if w.configure('text')[-1] == 'DOOR'][0]
         if dialog_key == 'DOOR_DIALOG' and door.configure('state')[-1] == 'normal':
            print('text', dialogs[dialog_key]['state'][self.ACTION_STATUS[dialog_key]]['text'])
            Item.change_count(Item.find_by_player(self.player, Type_Item.find_by_name(dialogs[dialog_key].get('de_action')).id).id, -1)
            self.tool_segment_2_lbl.config(text=dialogs[dialog_key]['state'][self.ACTION_STATUS[dialog_key]]['text'])
            self.game_window(next_loc)
            Player.change_location(self.player.name, next_loc)
         self.tool_segment_2_lbl.config(text=dialogs[dialog_key]['state'][self.ACTION_STATUS[dialog_key]]['text'])
         ev_widg = [w for w in self.frame_main_game_window.winfo_children() if w.configure('text')[-1] == 'MAIN_BOT'][0]
         ev_widg.configure(state='normal')
         if dialogs[dialog_key].get('action'):
            name_item = dialogs[dialog_key].get('action')
            if not Type_Item.find_by_name(name_item):
               Type_Item.add(name_item)
            if not Item.find_by_player(self.player, Type_Item.find_by_name(name_item).id):
               Item.add('КЛЮЧ', Player.find_by_name(self.player.name), Type_Item.find_by_name(name_item), 'Ключ от комода')
               print('FIND1111111111', Item.find_by_player(self.player, Type_Item.find_by_name(name_item).id).count)
            elif Item.find_by_player(self.player, Type_Item.find_by_name(name_item).id).count == 0:
               Item.find_by_player(self.player, Type_Item.find_by_name(name_item).id).count += 1
               print('FIN2222222222222', Item.find_by_player(self.player, Type_Item.find_by_name(name_item).id).count)
            self.ACTION_STATUS['DOOR_DIALOG'] = 1
            door.configure(state='normal')






   def get_player_invetory(self):
      Inventory(self.master, self.player)




#
#    def player_table(self):
#       for i in range(len(self.player.game_list)):
#          self.frame_player_table=Frame(self.frame_player_2, relief=SOLID)
#
#          self.numtable=i
#          self.player_label_res=ttk.Label(self.frame_player_2,
#                                          text=f"Сумма {sum(self.card_deck_dict[i]  for i in self.player.game_list[i])}")
#
#          self.choice_btn_1=ttk.Button(self.frame_player_2,
#                                       text='Еще карту?')
#
#          self.player_label_res.grid(column=i*4, row=3, columnspan=2)
#
#          self.choice_btn_1.grid(column=i*4, row=5)
#          self.choice_btn_1.bind('<Button-1>', self.add_card)
#          self.add_card_img(self.player,len(self.player.game_list))
#
#
#
#    def split_game_table(self):
#       self.split_btn.destroy()
#
#       self.player_balance.config(text=f"Баланс {self.player.balance}")
#       crd=self.player.game_list[self.numtable].pop(0)
#       self.player.game_list=player_game(self.card_deck, self.player,self.numtable)
#
#       self.player.game_list.append([crd])
#       self.player.game_list=player_game(self.card_deck, self.player, self.numtable+1)
#       self.player_table()
#
#
#    def add_card(self,event):
#       if self.split_btn:
#          self.split_btn.destroy()
#       grid_info = event.widget.grid_info()
#       if sum(self.card_deck_dict[i]  for i in self.player.game_list[grid_info['column']//3])>21:
#          mb.showwarning(message='Перебор')
#       elif sum(self.card_deck_dict[i]  for i in self.player.game_list[grid_info['column']//3])==21:
#          mb.showinfo(message='У Вас 21')
#       else:
#          r=player_game(self.card_deck, self.player,grid_info['column']//3)
#          self.add_card_img(self.player,len(self.player.game_list) )
#          if r[grid_info['column']//3][-1][-1]=='A':
#             if self.if_As(r[grid_info['column']//3][-1]):
#                r[grid_info['column']//3][-1]=r[grid_info['column']//3][-1][0]+'1'
#          #print(r)
#          for widget in self.frame_player_2.winfo_children():
#             if widget.widgetName.split('::')[-1]=='label':
#                if widget.grid_info()['column']==grid_info['column'] and widget.grid_info()['row']==grid_info['row']-2:
#
#                   widget.config(text=f" Сумма {sum(self.card_deck_dict[i]  for i in r[grid_info['column']//3])}")
#
#
#
#    def no_card(self):
#       self.choice_btn_1.destroy()
#       self.choice_btn_2.destroy()
#       self.add_croupier()
#
#    def add_croupier(self):
#
#       self.Croupier.game_list=player_game(self.card_deck, self.Croupier,0)
#       if self.Croupier.sum_res()[0]==21:
#          for widget in self.frame_desk.winfo_children():
#             widget.destroy()
#          self.desk_label=ttk.Label(self.frame_desk)
#          self.desk_label.grid(column=0, row=0)
#
#          self.croupier_label_res.config(text=f" Сумма {sum(self.card_deck_dict[i]  for i in self.Croupier.game_list[0])}")
#          self.add_card_img(self.Croupier,1)
#
#          self.desk_label.config(text=f"Все игроки проиграли раунд")
#          self.player.balance=self.player.balance+-self.bet*len(self.player.game_list)
#          self.player_balance.config(text=f"Баланс {self.player.balance}")
#
#
#       else:
#          r=game_croupier(self.card_deck,self.Croupier)
#          self.croupier_label_res.config(text=f" Сумма {sum(self.card_deck_dict[i]  for i in r[len(self.Croupier.game_list)-1])}")
#          self.add_card_img(self.Croupier,1)
#          self.result_game(self.bet)
#
#    def result_game(self, bet):
#       winners=WhoWin(self.Croupier, self.player)
#       wins=''
#       for k, v in winners.items():
#          if len(v)>0:
#             wins+=','.join(v)+' игрока '+k
#       w=len(winners[self.player.name])*2-len(self.player.game_list)
#       for widget in self.frame_desk.winfo_children():
#             widget.destroy()
#       self.desk_label=ttk.Label(self.frame_desk)
#       self.desk_label.grid(column=0, row=0)
#       if len(wins)>0:
#          self.desk_label.config(text=f"Победили столы {wins}", font=('Arial', 14))
#       else:
#          self.desk_label.config(text=f"Все игроки проиграли раунд",font=('Arial', 14))
#
#       self.player.balance=self.player.balance+self.bet*(len(winners[self.player.name])*2-len(self.player.game_list))
#       self.player_balance.config(text=f"Баланс {self.player.balance}")
#
#    def is_split(self, pl):
#       self.split_btn=ttk.Button(self.frame_player_2, text="Сплит?", command=self.split_game_table)
#       if self.card_deck_dict[pl.game_list[len(self.player.game_list)-1][0]]==self.card_deck_dict[pl.game_list[len(self.player.game_list)-1][1]]:
#
#          self.split_btn.grid(column=1, row=5)
#
#    def is_stop(self,s):
#       if s>21:
#          self.choice_btn_1.destroy()
#          self.choice_btn_2.destroy()
#          self.add_croupier()
#    def if_BJ(self,s):
#       if s==21:
#          self.player.balance=self.player.balance+self.bet
#          self.choice_btn_1.destroy()
#          self.choice_btn_2.destroy()
#          mb.showinfo(message="У Вас БлекДжек! Вы выиграли")
#          self.add_croupier()
#
#    def if_As(self,card):
#       self.as_dialog=as_dialog(self.master)
#       self.as_choice=self.as_dialog.go()
#       return self.as_choice
#
#    def rules(self):
#
#       rules(self.master)
#
#
#    def add_card_img(self, pl,pos):
#       if pl.name=='Croupier':
#          widget_im=self.frame_croupier
#       else:
#          widget_im=self.frame_player_2
#       pl.image_list=[[]]
#
#
#       for i in range(len(pl.game_list)):
#          pl.image_list.append([])
#          for j in range(len(pl.game_list[i])):
#             self.cards_images=tk.Canvas(widget_im, height=130, width=90)
#             path=str(pl.game_list[i][j])+'.png'
#
#             file_name = os.path.join("cards", path)
#             im=tk.PhotoImage(file=file_name)
#             pl.image_list[i].append(im)
#
#             image = self.cards_images.create_image(0, 0, anchor='nw',image=pl.image_list[i][j])
#             self.cards_images.grid(column=j+4*i, row=4,pady=1)
#
#

   def exitMethod(self):
       self.dialog = yesno(self.master)
       self.returnValue = self.dialog.go('question',
                                         'Вы хотите выйти?')
       if self.returnValue:
         self.master.destroy()
      
       
root = Tk()

Main(root)


# def game_window(self, file):
#    # path = "355.png"
#    # file_name = os.path.join("images", path)
#    # image = PIL.Image.open(file_name),
#    # print(image)
#    # im = PIL.ImageTk.PhotoImage(image)#file=file_name, width=100, height=100)
#    # print(im)
#    # self.frame_main_game_window.config(image=im)
#    #
#    # self.canvas = tk.Canvas(self.frame_main_game_window, width=100, height=100)
#    # self.canvas.create_image(0,0,anchor='nw',image=im)
#    # self.canvas.pack()
#    for i in range(30): self.frame_main_game_window.columnconfigure(index=i, weight=1)
#    for j in range(20): self.frame_main_game_window.rowconfigure(index=j, weight=1)
#    for i in range(30):
#       for j in range(20):
#          if (i, j) == THE_BOT[0]:
#             btn = tk.Button(self.frame_main_game_window, text=THE_BOT[3], cursor="circle",
#                             borderwidth=1)  # , width=2,height=1)
#             # btn=ttk.Button(self.frame_main_game_window, text=f'{i}:{j}',cursor= "circle")
#             btn.bind('<Button-1>', self.bot_gialog)
#             btn.grid(column=i, row=j, columnspan=THE_BOT[1], rowspan=THE_BOT[2], sticky='nsew')
#          elif (i, j) == THE_SAFE[0]:
#             btn = tk.Button(self.frame_main_game_window, text=THE_SAFE[3], cursor="circle", borderwidth=1, width=2,
#                             height=1)
#             # else:
#             # btn = tk.Button(self.frame_main_game_window, text=f'{i}:{j}',cursor="arrow",borderwidth=1, width=2, height=1)
#             # btn = ttk.Button(self.frame_main_game_window, text=f'{i}:{j}',cursor='arrow')
#             btn.bind('<Button-1>', self.safe_quest)
#             btn.grid(column=i, row=j, columnspan=THE_SAFE[1], rowspan=THE_SAFE[2], sticky='nsew')
#
#    # lbl = ttk.Label(self.frame_main_game_window, text= 'rRR', background='lightgreen')
#    # lbl.grid(column=1, row=1)
#    self.frame_tools_window_segment_1 = Frame(self.frame_tools_window, borderwidth=1)
#    for c in range(3): self.frame_tools_window_segment_1.columnconfigure(index=c, weight=1)
#    self.frame_tools_window_segment_2 = Frame(self.frame_tools_window, relief=SOLID, borderwidth=1)
#    for c in range(1): self.frame_tools_window_segment_2.columnconfigure(index=c, weight=1)
#    self.frame_tools_window_segment_3 = Frame(self.frame_tools_window, relief=SOLID, borderwidth=1)
#    for c in range(3): self.frame_tools_window_segment_3.columnconfigure(index=c, weight=1)
#    self.frame_tools_window_segment_1.grid(row=0, column=0, sticky='ew')
#    self.frame_tools_window_segment_2.grid(column=1, row=0, sticky='ew', columnspan=3)
#    self.frame_tools_window_segment_3.grid(column=4, row=0, sticky='ew')
#
#    # self.main_game_window_lbl = ttk.Label(self.frame_main_game_window, text='DIALOG',background="lightgreen", anchor='center')
#
#    self.tool_segment_1_btn_1 = ttk.Button(self.frame_tools_window_segment_1, text='Инвентарь',
#                                           command=self.get_player_invetory)
#    self.tool_segment_1_btn_2 = ttk.Button(self.frame_tools_window_segment_1, text='2')
#    self.tool_segment_1_btn_3 = ttk.Button(self.frame_tools_window_segment_1, text='3')
#
#    self.tool_segment_2_lbl = ttk.Label(self.frame_tools_window_segment_2, text='Ответы', anchor='center',
#                                        background="lightblue", )
#
#    self.tool_segment_3_btn_1 = ttk.Button(self.frame_tools_window_segment_3, text='1')
#    self.tool_segment_3_btn_2 = ttk.Button(self.frame_tools_window_segment_3, text='2')
#    self.tool_segment_3_btn_3 = ttk.Button(self.frame_tools_window_segment_3, text='3')
#
#    # self.main_game_window_lbl.pack(fill=BOTH,expand=1)
#
#    self.tool_segment_1_btn_1.grid(column=0, row=0, sticky='ew')
#    self.tool_segment_1_btn_2.grid(column=1, row=0, sticky='ew')
#    self.tool_segment_1_btn_3.grid(column=2, row=0, sticky='ew')
#
#    self.tool_segment_2_lbl.grid(sticky='ew')
#
#    self.tool_segment_3_btn_1.grid(column=0, row=0, sticky='ew')
#    self.tool_segment_3_btn_2.grid(column=1, row=0, sticky='ew')
#    self.tool_segment_3_btn_3.grid(column=2, row=0, sticky='ew')


# def bot_gialog(self, event):
#    self.DIALOG_PLAYER_STATUS += 1
#    if THE_PLAYER_DIALOG['state'].get(self.DIALOG_PLAYER_STATUS):
#       # new_text = StringVar()
#       # new_text.set(THE_PLAYER_DIALOG['state'][self.DIALOG_PLAYER_STATUS]['text'])
#       print(THE_PLAYER_DIALOG['state'][self.DIALOG_PLAYER_STATUS]['text'])
#       self.tool_segment_2_lbl.config(text=THE_PLAYER_DIALOG['state'][self.DIALOG_PLAYER_STATUS]['text'])
#       self.tool_segment_2_lbl.update()
#    sleep(1)
#    if self.DIALOG_PLAYER_STATUS - self.DIALOG_BOT_STATUS == 1:
#       self.DIALOG_BOT_STATUS += 1
#       if THE_BOT_DIALOG['state'].get(self.DIALOG_BOT_STATUS):
#          print(THE_BOT_DIALOG['state'][self.DIALOG_BOT_STATUS]['text'])
#          self.tool_segment_2_lbl.config(text=THE_BOT_DIALOG['state'][self.DIALOG_BOT_STATUS]['text'])
#          self.ACTION_STATUS = THE_BOT_DIALOG['state'][self.DIALOG_BOT_STATUS]['act']