import time
from .classes import *
from ..utils import constants
import random

class RegicideGame:
    def __init__(self, players:list[Player], jesters:bool = False):
        self.enemies = RegicideGame.init_enemies()
        self.players = players
        self.max_hand_size = 9 - len(players)
        self.tavern_deck = TavernDeck(player_count=len(players))
        self.player_index = 0
        self.draw_cards(draw_value=(self.max_hand_size * len(players)))

    # May move to helpers
    @staticmethod
    def init_enemies() -> list[Enemy]:
            enemy_deck:list[Enemy] = []

            for enemy in constants.enemies_infos:
                enemies_color:list[Enemy] = []

                for suit in constants.suits:
                    enemies_color.append(Enemy(value=enemy["attack"], suit=Suit(name=suit[0], color=suit[1]), health=enemy["health"], name=enemy["name"]))

                random.shuffle(enemies_color)
                enemy_deck.extend(enemies_color)

            return enemy_deck

    def get_cards_value(self, cards:list[Card]) -> int:
        return sum([card.value for card in cards])

    def calculate_attack_value(self, enemy:Enemy, cards:list[Card]) -> tuple[int, int, int, int]:
        value = self.get_cards_value(cards)
        if value > 0:
            suits_played = [card.suit.name for card in cards]
            heal_value = value if "Heart" in suits_played and (enemy.immune == False or enemy.suit.name != "Heart") else 0
            draw_value = value if "Diamond" in suits_played and (enemy.immune == False or enemy.suit.name != "Diamond") else 0
            
            lower_attack_value = value if "Spade" in suits_played and (enemy.immune == False or enemy.suit.name != "Spade") else 0
            damage_value = value*2 if "Club" in suits_played and (enemy.immune == False or enemy.suit.name != "Club") else value
            return heal_value, draw_value, damage_value, lower_attack_value
        else:
            return 0, 0, 0, 0

    def cards_to_shield(self, player:Player, enemy:Enemy) -> list[Card]:
        while True:
            # print(enemy.get_enemy_infos())
            # print(f"Choose cards to shield yourself against the current enemy damage.")
            cards = player.choose_cards()
            if self.get_cards_value(cards) >= enemy.attack:
                self.tavern_deck.discard_pile.extend(cards)
                return cards
            else:
                # print("Not enough value to shield, please try again")
                player.add_cards(cards=cards)

    def cards_to_attack(self, player:Player) -> list[Card]:
        while True:
            cards = player.choose_cards()
            if self.check_playability(cards):
                return cards
            else:
                # if not player.is_ai:
                    # print("This move is not allowed.")
                player.add_cards(cards=cards)


    def heal(self, heal_value):
        random.shuffle(self.tavern_deck.discard_pile)
        i = min(heal_value, len(self.tavern_deck.discard_pile))
        self.tavern_deck.deck.extend([card for card in [self.tavern_deck.discard_pile.pop() for _ in range(i)]])

    def draw_cards(self, draw_value:int):
        player_index = self.player_index
        while draw_value and not all([len(p.hand) == self.max_hand_size for p in self.players]) and self.tavern_deck.deck:
            player = self.players[player_index]
            if len(player.hand) < self.max_hand_size:
                player.add_cards([self.tavern_deck.deck.pop()])
                draw_value -= 1

            player_index += 1

            if player_index >= len(self.players): player_index = 0


    # May move to helpers
    def check_playability(self, cards:list[Card]) -> bool:
        values = [card.value for card in cards]
        # If at most one card is played, no need to check anything.
        if not values:
            return True
        if len(values) <= 1:
            return True
        else:
        # If multiples cards are played
            # If all cards have the same value
            if len(set(values)) == 1:
                # Check if total value inferior or equal to 10
                if sum(values) <= 10:
                    # Check for multiple jesters played together
                    if sum(values) == 0:
                        return False
                    return True
            else:
            # If cards have a different value
                # Check that only two cards are played and contains an animal companion (Aces)
                if len(values) == 2 and 1 in values:
                    return True
        return False

    def choose_next_player(self, player:Player) -> int:
        while True:
            # [print(f"{num}: {player.show_player_infos()}") for num, player in enumerate(self.players, 1)]
            if not player.is_ai:
                index = int(input("Choose who is playing next:"))
            else:
                index = random.randint(1, len(self.players))
            try:
                if 0 > index > len(self.players): raise IndexError
                return index
            except IndexError:
                pass
                # print("Please choose an existing player")


def main():
    alice = Player(name="Alice", is_ai=True)
    bob = Player(name="Bob")
    kevin = Player(name="Kevin")
    julie = Player(name="Julie")

    players:list[Player] = [alice, bob, kevin, julie]

    # random.shuffle(players)

    game = RegicideGame(players=players)

    game_on = True

    kills = 0

    player = players[game.player_index]

    while game_on:
        current_enemy = None
        if game.enemies:
            # ATTACK PHASE
            if not current_enemy: current_enemy = game.enemies[0]
            if player.hand:
                # print(f"Tavern deck {len(game.tavern_deck.deck)}")
                # print(f"Discard Pile({len(game.tavern_deck.discard_pile)}): {[str(card) for card in game.tavern_deck.discard_pile]}")
                # print(current_enemy.get_enemy_infos())
                # print(f"It's your turn {player.name}")
                cards = game.cards_to_attack(player)

                # print(f"Cards played: {[str(card) for card in cards]}")

                if not cards:
                    pass
                    # print("You yield.")
                elif "S" in [card.name for card in cards]:
                    current_enemy.immune = False
                    game.tavern_deck.discard_pile.extend(cards)
                    game.player_index = game.choose_next_player(player) - 1
                    player = players[game.player_index]
                    continue
                else:
                    heal_value, draw_value, damage_value, lower_attack_value = game.calculate_attack_value(current_enemy, cards)
                    if heal_value:
                        game.heal(heal_value)
                        # print(f"Heal: {heal_value}")

                    if draw_value:
                        game.draw_cards(draw_value=draw_value)
                        # print(f"Draw: {draw_value}")

                    # print(f"damage: {damage_value}, lower_attack: {lower_attack_value}")
                    current_enemy.health -= damage_value
                    current_enemy.attack -= lower_attack_value
                    current_enemy.attack = max(0, current_enemy.attack)

                game.tavern_deck.discard_pile.extend(cards)

                if current_enemy.health <= 0:
                    # print(f"{current_enemy} died.")
                    kills += 1
                    if current_enemy.health == 0: game.tavern_deck.discard_pile.append(current_enemy)
                    game.enemies.pop(0)
                    current_enemy = game.enemies[0]
                    continue
                

                # SHIELD PHASE
                if current_enemy.attack > 0:
                    if player.get_hand_value() < current_enemy.attack:
                        # print("You can't shield")
                        game_on = False
                        break
                    else:
                        cards = game.cards_to_shield(player, current_enemy)
                
            else:
                # print("No more cards")
                game_on = False
        else:
            # print("You won")
            game_on = False
        game.player_index += 1
        if game.player_index >= len(players): game.player_index = 0
        player = players[game.player_index]
    # print("Game Over")
    print(f"Regents killed: {kills}")
    if kills >= 8:
        input("wow")

if __name__ == "__main__":
    for i in range(1, 20000):
        print(f"Playing game number {i}...")
        main()
