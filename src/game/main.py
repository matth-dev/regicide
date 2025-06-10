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

def init_tavern_deck() -> list[Card]:
    deck:list[Card] = []
    for suit in suits:
        for i in range(1, 11):
            deck.append(Card(value=i, suit=Suit(color=suit)))
    random.shuffle(deck)
    return deck

def init_enemies() -> list[Enemy]:
    enemy_deck:list[Enemy] = []
    for enemy in enemies_infos:
        enemies_color:list[Enemy] = []
        for suit in suits:
            enemies_color.append(Enemy(value=enemy["attack"], suit=Suit(color=suit), health=enemy["health"], name=enemy["name"]))
        random.shuffle(enemies_color)
        enemy_deck.extend(enemies_color)
    return enemy_deck

tavern_deck = init_tavern_deck()

enemies_deck = init_enemies()

alice = Player(name="Alice")
bob = Player(name="Bob")

max_hands_size = 7
player_number = 2
players:list[Player] = [alice, bob]

for player in players:
    for _ in range(0, max_hands_size):
        player.hand.append(tavern_deck.pop())

print(len(alice.hand))
print(len(bob.hand))
print(len(tavern_deck))
print(enemies_deck[0])