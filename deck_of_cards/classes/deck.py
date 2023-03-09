from . import card
from random import randint

class Deck:
    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append(card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()
        return self
            
    def shuffle(self):
        for i in range(len(self.cards)):
            rng = randint(0, i)
            self.cards[i], self.cards[rng] = self.cards[rng], self.cards[i]
        return self
    
    def deal(self):
        return self.cards.pop()

