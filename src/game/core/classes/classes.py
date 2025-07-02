import random
from ...utils import constants
from enum import Enum
import time
import itertools
import random

class Suit:
    def __init__(self, name:str, color:str):
        self.name = name
        self.color = color

class Card:
    def __init__(self, name:str, value:int, suit:Suit | None):
        self.name = name
        self.value = value
        self.suit = suit

    def __str__(self):
        if self.suit:
            return self.name+self.suit.color
        else:
            return self.name

class Enemy(Card):
    def __init__(self, value:int, suit:Suit, health:int, name:str):
        super().__init__(name, value, suit)
        self.health=health
        self.attack = value
        self.immune = random.choice([True, False])

    def get_enemy_infos(self):
        return f"{self.name}{self.suit.color} // Attack: {str(self.attack)} // Health remaining: {self.health} // Immune: {self.immune}"
    
class Player:
    def __init__(self, name:str, is_ai:bool = True):
        self.name = name
        self._hand:list[Card] = []
        self.is_ai = is_ai
    
    @property
    def hand(self):
        return self._hand
    
    def add_cards(self, cards:list[Card]):
        self._hand.extend(cards)
        self._hand.sort(key=lambda x: x.value)

    def _show_hand(self) -> list[str]:
        return [str(card) for card in self.hand]
    
    def get_hand_value(self) -> int:
        return sum([card.value for card in self.hand])
    
    def choose_cards(self) -> list[Card]:
        while True:
            if not self.is_ai:
                print(self._show_hand())
                card_indexes = [(int(index) - 1) for index in input(f"Choose cards to play between 1 and {len(self.hand)}\n")]
            else:
                moves = [[0]]
                for i in range(1, 5):
                    moves.extend([play for play in itertools.combinations(iterable=range(1, len(self.hand)+1), r=i)])
                card_indexes = [(int(index) - 1) for index in random.choice(moves)]

            try:
                if not all(index >=-1 for index in card_indexes): raise IndexError
                if -1 in card_indexes:
                    return []
                return [self.hand.pop(index) for index in sorted(card_indexes, reverse=True)]
            except IndexError:
                print(f"Choose at least one existing card or press 0 to yield while in attack phase.")

    def show_player_infos(self) -> str:
        return f"{self.name}({len(self.hand)})"

class TavernDeck:
    def __init__(self, player_count:int):
        self.deck = []
        self.discard_pile:list[Card] = []
        self._create_deck(player_count)

    def _create_deck(self, player_count:int):
        for suit in constants.suits:
            for i in range(1, 11):
                self.deck.append(Card(name=str(i), value=i, suit=Suit(name=suit[0], color=suit[1])))
        if player_count >= 3:
            jesters_count = player_count - 2
            for _ in range(jesters_count):
                self.deck.append(Card(name="S", value=0, suit=None))
        random.shuffle(self.deck)

class GamePhase(Enum):
    SETUP = "setup"
    PLAYER_TURN = "player_turn"
    CARD_POWER = "card_power"
    ENEMY_TURN = "enemy_turn"
    GAME_OVER = "game_over"

class GameState:
    def __init__(self):
        pass