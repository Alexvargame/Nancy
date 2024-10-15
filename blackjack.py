import random
from player import *



def begin_game(card_deck,pl1):
    
        
    pl1.game(card_deck.pop(card_deck.index(random.choice(card_deck))),0)
    pl1.game(card_deck.pop(card_deck.index(random.choice(card_deck))),0)
    #pl1.game_list=[['SA', 'HA']]
    if pl1.game_list[0][0][-1]==pl1.game_list[0][1][-1] and pl1.game_list[0][0][-1]=='A':
        pl1.game_list[0][0]='1'
    return pl1.game_list

def player_game(card_deck,pl1,i):
    pl1.game(card_deck.pop(card_deck.index(random.choice(card_deck))),i)
    return pl1.game_list



    
def game_croupier(card_deck,pl):
   

    while pl.sum_res()[0]<17:
        pl.game(card_deck.pop(card_deck.index(random.choice(card_deck))),0)

    return pl.game_list
            
        
        
def WhoWin(Croupier,*args):

    #results=[p.sum_res() for p in args]
    wdict={}
    for p in args:
##        key, value=p.name, *[[str(i+1) for i in range(len([p.sum_res() for p in args][j])) if
##                (Croupier.sum_res()[0]<[p.sum_res() for p in args][j][i] and [p.sum_res() for p in args][j][i]<=21)
##                              or Croupier.sum_res()[0]>21] for j in range(len([p.sum_res() for p in args]))]
        key, value=p.name, *[[str(i+1) for i in range(len([p.sum_res() for p in args][j])) if
                (Croupier.sum_res()[0]<[p.sum_res() for p in args][j][i] or Croupier.sum_res()[0]>21)
                             and [p.sum_res() for p in args][j][i]<=21]
                               for j in range(len([p.sum_res() for p in args]))]

        wdict[key]=value

    return wdict

    
    
  
    
