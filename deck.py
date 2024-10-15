
def get_deck(n=4):

    
    CardSuit=['Spades','Clubs','Diamonds','Hearts']
    Nominal=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
#    Points=[]
    card_deck_dict={}

#    points_dict={}

##    for nom in Nominal:
##        key, value=nom, int(nom) if nom.isdigit() else 10
##        points_dict[key]=value
##    points_dict['1']=1
##    points_dict['A']=11

    CardSuitDeck=[cs[0].upper()+j for j in Nominal for cs in CardSuit]
    for cs in CardSuitDeck:
        key,value=cs, int(cs[1:]) if cs[1:].isdigit() else 10
        card_deck_dict[key]=value
    for k in card_deck_dict.keys():
        if k[-1]=='A':
            card_deck_dict[k]=11
    card_deck_dict['S1']=1
    card_deck_dict['C1']=1
    card_deck_dict['D1']=1
    card_deck_dict['H1']=1
    #print(card_deck_dict)
    #print(CardSuitDeck,card_deck_dict)
            
    return CardSuitDeck*n, card_deck_dict


def main():
    
     get_deck()
    


if __name__ == "__main__":
    main()

    
