from classes import *

deck:list[Card] = []

suits = ["♠", "♥", "♦", "♣"]

for suit in suits:
    for i in range(1, 11):
        deck.append(Card(value=i, suit=Suit(color=suit)))

print(deck)