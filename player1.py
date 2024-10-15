from deck import *


class Player:

    def __init__(self, name):
        self.name=name
        self.game_list=[[]]
        self.image_list=[[]]
        self.balance=100
        

    def game(self, card,i):
        self.game_list[i].append(card)
        return self.game_list
    def sum_res(self):
        _, self.card_dect_dict=get_deck()
        
        return [sum([self.card_dect_dict[i]  for i in self.game_list[j]]) for j in range(len(self.game_list))]
    def __repr__(self):
       return "<name:%s balance:%s, game_list :%s >" % (self.name, self.balance, self.game_list)
    def __str__(self):
        return "%s %s %s" % (self.name, self.balance, self.game_list)

        
    
