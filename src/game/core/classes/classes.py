import random
from ...utils import constants

class Suit:
    def __init__(self, name:str, color:str):
        self.name = name
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
        self.attack = value
        self.immune = True

    def __str__(self):
        return f"Name: {self.name}{self.suit.color} // Attack: {str(self.attack)} // Health remaining: {self.health} // Immune: {self.immune}"
    
    def take_damage(self, card:Card) -> None:
        value = card.value
        if card.suit.name == "Spade":
            if self.suit.name != "Spade" or not self.immune:
                value *= 2

        if card.suit.name == "Club":
            if self.suit.name != "Club" or not self.immune:
                self.attack = max(0, self.attack - card.value)

        self.health -= value
        print(f"{self.name} took {value} damage.")
    
class Player:
    def __init__(self, name:str):
        self.name = name
        self.hand:list[Card] = []

    def show_hand(self) -> list[str]:
        return [str(card) for card in self.hand]
    
    def get_hand_value(self) -> int:
        return sum([card.value for card in self.hand])

class TavernDeck:
    def __init__(self, jesters=False):
        deck = []
        for suit in constants.suits:
            for i in range(1, 11):
                deck.append(Card(value=i, suit=Suit(suit[0], suit[1])))
        if jesters:
            pass
            # add jesters to deck
        random.shuffle(deck)
        
        self.deck:list[Card] = deck
