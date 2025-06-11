from classes import *

import random



def init_enemies() -> list[Enemy]:
    enemy_deck:list[Enemy] = []
    for enemy in enemies_infos:
        enemies_color:list[Enemy] = []
        for suit in suits:
            enemies_color.append(Enemy(value=enemy["attack"], suit=Suit(color=suit), health=enemy["health"], name=enemy["name"]))
        random.shuffle(enemies_color)
        enemy_deck.extend(enemies_color)
    return enemy_deck

def init_players_hand(players:list[Player]):
    max_hand_size = 9 - len(players)
    for player in players:
        for _ in range(0, max_hand_size):
            player.hand.append(tavern_deck.pop())

def main():
    tavern_deck = TavernDeck(jesters=False)
    enemies_deck = init_enemies()

    alice = Player(name="Alice")
    bob = Player(name="Bob")

    max_hands_size = 7
    player_number = 2
    players: list[Player] = [alice, bob]

    init_players_hand(players)

    alice.show_hand()
if __name__ == "__main__":
    main()