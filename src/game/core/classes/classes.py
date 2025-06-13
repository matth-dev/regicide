import random
from ...utils import constants
from enum import Enum

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
    
class Player:
    def __init__(self, name:str):
        self.name = name
        self.hand:list[Card] = []

    def show_hand(self) -> list[str]:
        return [str(card) for card in self.hand]
    
    def get_hand_value(self) -> int:
        return sum([card.value for card in self.hand])
    
    def choose_cards(self) -> list[Card]:
        while True:
            print(self.show_hand())
            card_indexes = [(int(index) - 1) for index in input("Choose cards \n")] # Transform "45" in [3, 4]
            try:
                return [self.hand.pop(index) for index in sorted(card_indexes, reverse=True)]
            except IndexError:
                print(f"Please try choosing existing cards")

    
    def get_cards_value(self, cards:list[Card]) -> int:
        return sum([card.value for card in cards])
    
    def take_damage(self, enemy_attack_value:int):
        
        while self.get_cards_value(self.choose_cards()) < enemy_attack_value:
            continue

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

class GamePhase(Enum):
    SETUP = "setup"
    PLAYER_TURN = "player_turn"
    CARD_POWER = "card_power"
    ENEMY_TURN = "enemy_turn"
    GAME_OVER = "game_over"

class GameState:
    def __init__(self):
        pass