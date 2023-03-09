class Card:
    def __init__( self , suit , point_val , string_val ):
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val
        
    def __repr__(self) -> str:
        return f"{self.string_val} of {self.suit}"

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")
        
    def getPts(self):
        return self.point_val
    
    def getType(self):
        return self.string_val
    
    def getSuit(self):
        return self.suit