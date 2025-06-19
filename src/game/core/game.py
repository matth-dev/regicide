from .classes import *
from ..utils import constants
import random
from typing import Optional

class RegicideGame:
    def __init__(self, players:list[Player], jesters:bool = False):
        self.enemies = self._init_enemies()
        self.tavern_deck = TavernDeck(jesters=jesters)
        self.players = players
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

    def _init_players_hand(self) -> None:
        max_hand_size = 9 - len(self.players)

        for _ in range(0, max_hand_size):
            for player in self.players:
                player.hand.append(self.tavern_deck.deck.pop())

    def get_cards_value(self, cards:list[Card]) -> int:
        return sum([card.value for card in cards])

    def calculate_attack_value(self, enemy:Enemy, cards:list[Card]) -> tuple[int, int]:
        #TODO: Properly handle animal companions
        damage_value = 0
        lower_attack_value = 0
        if cards:
            for card in cards:
                damage_value += card.value

                if card.suit.name == "Club":
                    if enemy.suit.name != "Club" or not enemy.immune:
                        damage_value += card.value

                if card.suit.name == "Spade":
                    if enemy.suit.name != "Spade" or not enemy.immune:
                        lower_attack_value += card.value

        return damage_value, lower_attack_value
    
    def cards_to_shield(self, player:Player, enemy:Enemy) -> list[Card]:
        while True:
            print(enemy)
            print(f"Choose cards to shield yourself against the current enemy damage.")
            cards = player.choose_cards()
            if self.get_cards_value(cards) >= enemy.attack:
                self.tavern_deck.discard_pile.extend(cards)
                return cards
            else:
                print("Not enough value to shield, please try again")
                player.hand.extend(cards)

    def cards_to_attack(self, player:Player) -> list[Card]:
        while True:
            cards = player.choose_cards()
            if self.check_playability(cards) == True:
                self.tavern_deck.discard_pile.extend(cards)
                return cards
            else:
                print("This move is not allowed.")
                player.hand.extend(cards)


    def check_playability(self, cards:list[Card]) -> bool:
        values = [card.value for card in cards]
        # If at most one card is played, no need to check anything.
        if len(values) <= 1:
            return True
        else:
        # If multiples cards are played
            # If all cards have the same value
            if len(set(values)) == 1:
                # Check if total value inferior or equal to 10
                if sum(values) <= 10:
                    return True
            else:
            # If cards have a different value
                # Check that only two cards are played and contains an animal companion (Aces)
                if len(values) == 2 and 1 in values:
                    return True
        return False


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
                print(f"There are {len(game.tavern_deck.discard_pile)} cards in the discard pile")
                print(current_enemy)
                cards = game.cards_to_attack(alice)

                damage_value, lower_attack_value = game.calculate_attack_value(current_enemy, cards)
                current_enemy.health -= damage_value
                current_enemy.attack -= lower_attack_value

                if current_enemy.health <= 0:
                    print(f"{current_enemy.name} died.")
                    game.enemies.pop(0)
                    current_enemy = game.enemies[0]

                if current_enemy.attack > 0:
                    if alice.get_hand_value() < current_enemy.attack:
                        print("You can't shield. You lost")
                        game_on = False
                    else:
                        cards = game.cards_to_shield(alice, current_enemy)

            else:
                print("No more cards")
                game_on = False
        else:
            print("You won")
            game_on = False
    print("Game Over")

if __name__ == "__main__":
    main()