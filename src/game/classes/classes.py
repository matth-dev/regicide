import random
from ..utils import constants

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
    def __init__(self, value:int, suit:Suit, health:int, name:str):
        super().__init__(value, suit)
        self.health=health
        self.name=name
        self.immune=True

    def __str__(self):
        return f"Name: {self.name} // {str(self.value)}+{self.suit.color} // Health remaining: {self.health}. Immune: {self.immune}"

class Player:
    def __init__(self, name:str):
        self.name = name
        self.hand:list[Card] = []

    def show_hand(self):
        return [str(card) for card in self.hand]

class TavernDeck:
    def __init__(self, jesters=False):
        deck = []
        for suit in constants.suits:
            for i in range(1, 11):
                deck.append(Card(value=i, suit=Suit(color=suit)))
        if jesters:
            pass
            # add jesters to deck
        random.shuffle(deck)
        self.deck:list[Card] = deck
