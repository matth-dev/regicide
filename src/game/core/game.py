from .classes import *
from ..utils import constants
import random

def init_enemies() -> list[Enemy]:
        enemy_deck:list[Enemy] = []

        for enemy in constants.enemies_infos:
            enemies_color:list[Enemy] = []

            for suit in constants.suits:
                enemies_color.append(Enemy(value=enemy["attack"], suit=Suit(name=suit[0], color=suit[1]), health=enemy["health"], name=enemy["name"]))

            random.shuffle(enemies_color)
            enemy_deck.extend(enemies_color)

        return enemy_deck

def init_players_hand(tavern_deck:TavernDeck, players:list[Player]):
    max_hand_size = 9 - len(players)
    
    for _ in range(0, max_hand_size):
        for player in players:
            player.hand.append(tavern_deck.deck.pop())

def main():
    tavern_deck = TavernDeck(jesters=False)
    enemies_deck = init_enemies()

    alice = Player(name="Alice")
    bob = Player(name="Bob")

    players: list[Player] = [alice]

    init_players_hand(tavern_deck, players)

    game = True

    while game:
        current_enemy = enemies_deck[0]

        if alice.hand:
            print(alice.show_hand())
            print(current_enemy)

            choice = int(input(f"Choose a card from 1 to {len(alice.hand)}\n"))
            card = alice.hand.pop(choice - 1)
            print(f"You choose card {card}")

            current_enemy.take_damage(card)

            if current_enemy.health <= 0:
                enemies_deck.pop(0)
        else:
            print("No more cards")
            game = False

    print("Game Over")

if __name__ == "__main__":
    main()