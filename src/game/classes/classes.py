class Suit:
    def __init__(self, color:str):
        self.color = color

class Card:
    def __init__(self, value:int, suit:Suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return str(self.value)+self.suit.color

class Enemy(Card):
    def __init__(self, value:int, suit:Suit, health:int):
        super().__init__(value, suit)
        self.health=health
        self.immune=True

    def __str__(self):
        return f"{str(self.value)}+{self.suit.color} // Health remaining: {self.health}. Immune: {self.immune}"
