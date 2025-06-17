from .classes import *
from ..utils import constants
import random
from typing import Optional

class RegicideGame:
    def __init__(self, players:list[Player], jesters:bool = False):
        self.enemies = self._init_enemies()
        self.tavern_deck = TavernDeck(jesters=jesters)
        self.players = players
        self.discard_pile:list[Card] = []
        self._init_players_hand()

    def _init_enemies(self) -> list[Enemy]:
            enemy_deck:list[Enemy] = []

            for enemy in constants.enemies_infos:
                enemies_color:list[Enemy] = []

                for suit in constants.suits:
                    enemies_color.append(Enemy(value=enemy["attack"], suit=Suit(name=suit[0], color=suit[1]), health=enemy["health"], name=enemy["name"]))

                random.shuffle(enemies_color)
                enemy_deck.extend(enemies_color)

            return enemy_deck

    def _init_players_hand(self):
        max_hand_size = 9 - len(self.players)

        for _ in range(0, max_hand_size):
            for player in self.players:
                player.hand.append(self.tavern_deck.deck.pop())

    def get_cards_value(self, cards:list[Card]) -> int:
        return sum([card.value for card in cards])

    def calculate_values(self, enemy:Enemy, cards:list[Card]) -> tuple[int, int]:
        damage_value = 0
        enemy_attack_value = enemy.attack
        if cards:
            for card in cards:
                damage_value += card.value

                if card.suit.name == "Club":
                    if enemy.suit.name != "Club" or not enemy.immune:
                        damage_value += card.value

                if card.suit.name == "Spade":
                    if enemy.suit.name != "Spade" or not enemy.immune:
                        enemy_attack_value -= damage_value

        return damage_value, enemy_attack_value

def check_playability(cards:list[Card]) -> bool:
    return True

def main():
    alice = Player(name="Alice")

    players: list[Player] = [alice]

    game = RegicideGame(players=players, jesters=False)

    game_on = True

    while game_on:
        current_enemy = None
        if game.enemies:
            if not current_enemy: current_enemy = game.enemies[0]
            if alice.hand:
                print(current_enemy)
                print("To yield in the attack phase, press 0.")
                cards = alice.choose_cards()
                if not cards: print("You yielded.")
                if check_playability(cards=cards):
                    damage_value, attack_value = calculate_values(current_enemy, cards=cards)
                    current_enemy.health -= damage_value
                    current_enemy.attack = max(0, attack_value)
                    game.discard_pile.extend(cards)
                else:
                    print(f"Can't do this move")
                    if cards: alice.hand.extend(cards)

                print(f"There are {len(game.discard_pile)} cards in the discard pile")
                if current_enemy.health <= 0:
                    print(f"{current_enemy.name} died.")
                    game.enemies.pop(0)
                    current_enemy = game.enemies[0]

                if current_enemy.attack > 0:
                    if alice.get_hand_value() < current_enemy.attack:
                        print("You can't shield. You lost")
                        game_on = False
                    else:
                        alice.take_damage(current_enemy)
            else:
                print("No more cards")
                game_on = False
        else:
            print("You won")
            game_on = False
    print("Game Over")

if __name__ == "__main__":
    main()