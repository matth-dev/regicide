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

def calculate_values(enemy:Enemy, card:Card) -> tuple[int, int]:
    damage_value = card.value
    enemy_attack_value = enemy.attack

    if card.suit.name == "Club":
        if enemy.suit.name != "Club" and not enemy.immune:
            damage_value *= 2

    if card.suit.name == "Spade":
        if enemy.suit.name != "Spade" and not enemy.immune:
            enemy_attack_value -= damage_value

    return (damage_value, enemy_attack_value)

def check_playability(enemies_deck:list[Enemy], player:Player, card:Card) -> bool:
    (damage_value, enemy_attack_value) = calculate_values(enemies_deck[0], card)

    
    return True

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

        if enemies_deck:
            if alice.hand:
                print(alice.show_hand())
                print(current_enemy)

                choice = int(input(f"Choose a card from 1 to {len(alice.hand)}. To yield, press 0\n"))
                if choice == 0:
                    print(f"You yielded.")
                else:
                    card = alice.hand.pop(choice - 1)

                    print(f"You played card {card}")

                if current_enemy.health <= 0:
                    enemies_deck.pop(0)
            else:
                print("No more cards")
                game = False
        else:
            print("You won")
            game = False
    print("Game Over")

if __name__ == "__main__":
    main()