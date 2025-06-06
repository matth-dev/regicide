from classes import *
import random

deck:list[Card] = []
enemies:list[Card] = []

suits = ["♠", "♥", "♦", "♣"]

for suit in suits:
    for i in range(1, 11):
        deck.append(Card(value=i, suit=Suit(color=suit)))

enemy1 = Enemy(value=10, suit=Suit(color=suits[0]), health=20)

print(enemy1)
# random.shuffle(deck)
#
# for card in deck:
#     print(card)