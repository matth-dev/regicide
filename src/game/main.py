from classes import *
import random

suits = ["♠", "♥", "♦", "♣"]

enemies_infos = [
    {
        "name": "Jack",
        "attack":10,
        "health": 20
    },
    {
        "name": "Queen",
        "attack": 15,
        "health": 30
    },
    {
        "name": "King",
        "attack": 20,
        "health": 40
    }
]

def init_deck() -> list[Card]:
    deck:list[Card] = []
    for suit in suits:
        for i in range(1, 11):
            deck.append(Card(value=i, suit=Suit(color=suit)))
    return deck

def init_enemies() -> list[Enemy]:
    pass

tavern_deck = init_deck()

random.shuffle(starting_deck)

print(starting_deck)