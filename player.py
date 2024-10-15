


class Player:

    def __init__(self, name, items=[], balance=0,status='new'):
        self.name = name
        self.items= items
        self.balance = balance
        self.status = status

    def add_item(self,item):
        self.items.append(item)

    # def game(self, card,i):
    #     self.game_list[i].append(card)
    #     return self.game_list
    # def sum_res(self):
    #     _, self.card_dect_dict=get_deck()
        
       # return [sum([self.card_dect_dict[i]  for i in self.game_list[j]]) for j in range(len(self.game_list))]
    def __repr__(self):
       return "<name:%s starus:%s balance:%s, items :%s >" % (self.name, self.status, self.balance, self.items)
    def __str__(self):
        return "%s %s %s %s" % (self.name, self.status, self.balance, self.items)

        
    
