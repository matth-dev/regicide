class Suit:
    def __init__(self, color:str):
        self.color = color

class Card:
    def __init__(self, value:int, suit:Suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value)+self.suit.color