from .classes import *
from src.regicide.utils import constants
import random

class RegicideGame:
    def __init__(self, players:list[Player]):
        self.enemies = self._create_enemies()
        self.players = players
        self.player_count = len(self.players)
        self.max_hand_size = 9 - self.player_count
        self.tavern_deck = TavernDeck(player_count=self.player_count)
        self.player_index = 0
        self.deal_cards(draw_value=(self.max_hand_size * self.player_count))

    def _create_enemies(self):
        enemies:list[Enemy] = []

        for enemy in constants.ENEMIES:
            face_set:list[Enemy] = []

            for suit in constants.SUITS:
                face_set.append(Enemy(value=enemy["attack"], suit=Suit(name=suit[0], symbol=suit[1]), health=enemy["health"], name=enemy["name"]))

            random.shuffle(face_set)
            enemies.extend(face_set)

        return enemies

    @staticmethod
    def get_cards_value(cards:list[Card]) -> int:
        return sum([card.value for card in cards])

    @staticmethod
    def calculate_attack_value(enemy:Enemy, cards:list[Card]) -> tuple[int, int, int, int]:
        value = RegicideGame.get_cards_value(cards)
        if value > 0:
            suits_played = [card.suit.name for card in cards]
            heal_value = value if "Heart" in suits_played and (enemy.immune == False or enemy.suit.name != "Heart") else 0
            draw_value = value if "Diamond" in suits_played and (enemy.immune == False or enemy.suit.name != "Diamond") else 0
            
            lower_attack_value = value if "Spade" in suits_played and (enemy.immune == False or enemy.suit.name != "Spade") else 0
            damage_value = value*2 if "Club" in suits_played and (enemy.immune == False or enemy.suit.name != "Club") else value
            return heal_value, draw_value, damage_value, lower_attack_value
        else:
            return 0, 0, 0, 0

    @staticmethod
    def cards_to_shield(player:Player, enemy:Enemy) -> list[Card]:
        while True:
            if not player.is_ai:
                print("Shield phase")
            cards = player.choose_cards()
            if RegicideGame.get_cards_value(cards) >= enemy.attack:
                return cards
            else:
                if not player.is_ai:
                    print("Not enough value")
                player.add_cards(cards=cards)

    @staticmethod
    def cards_to_attack(player:Player) -> list[Card]:
        while True:
            if not player.is_ai:
                print("Attack phase")
            cards = player.choose_cards()
            if RegicideGame.check_playability(cards):
                return cards
            else:
                player.add_cards(cards=cards)


    def heal(self, maximum_heal_value):
        random.shuffle(self.tavern_deck.discard_pile)
        heal_value = min(maximum_heal_value, len(self.tavern_deck.discard_pile))
        self.tavern_deck.deck.extend([card for card in [self.tavern_deck.discard_pile.pop() for _ in range(heal_value)]])

    def deal_cards(self, draw_value:int):
        player_index = self.player_index
        while draw_value and not all([len(p.hand) == self.max_hand_size for p in self.players]) and self.tavern_deck.deck:
            player = self.players[player_index]
            if len(player.hand) < self.max_hand_size:
                player.add_cards([self.tavern_deck.deck.pop(0)])
                draw_value -= 1

            player_index += 1

            if player_index >= len(self.players): player_index = 0


    @staticmethod
    def check_playability(cards:list[Card]) -> bool:
        # If at most one card is played, no need to check anything.
        if len(cards) <= 1:
            return True

        values = [card.value for card in cards]

        # If all cards have the same value
        if len(set(values)) == 1:
            # Check if total value inferior or equal to 10
            if sum(values) > 10:
                return False
            # Check for multiple jesters played together
            if sum(values) == 0:
                return False
            return True
        else:
            # If cards have a different value
            # Check that only two cards are played and contains an animal companion (Aces)
            return True if len(values) == 2 and 1 in values else False

    def choose_next_player(self, player:Player) -> int:
        while True:
            if not player.is_ai:
                print([f"{index}: {p.show_player_infos()}" for index, p in enumerate(self.players, 1)])
                index = int(input("Choose who is playing next:"))
            else:
                return random.randint(0, len(self.players)-1)
            try:
                if 0 >= index > len(self.players): raise IndexError
                return index - 1 
            except IndexError:
                pass


    def show_game_infos(self, enemy:Enemy) -> None:
        enemy_infos = enemy.get_enemy_infos()
        tavern_deck_infos = f"Tavern Deck ({len(self.tavern_deck.deck)})| Discard Pile({len(self.tavern_deck.discard_pile)}): {[str(card) for card in self.tavern_deck.discard_pile]}"
        player_cards_infos = [f"{player.name}({len(player.hand)})" for player in self.players] 
        print(enemy_infos)
        print(tavern_deck_infos)
        print(player_cards_infos)

def main():
    alice = Player(name="Alice", is_ai=False)
    bob = Player(name="Bob")
    kevin = Player(name="Kevin")
    julie = Player(name="Julie")

    players:list[Player] = [alice, bob, kevin, julie]

    game = RegicideGame(players=players)

    game_on = True

    # Only here to track stat
    kills = 0

    while game_on:
        player = players[game.player_index]
        current_enemy = None
        if game.enemies:
            # ATTACK PHASE
            if not current_enemy: current_enemy = game.enemies[0]
            if player.hand:
                game.show_game_infos(enemy=current_enemy)
                cards = RegicideGame.cards_to_attack(player)

                if not cards:
                    print(f"{player.name} yield")
                    pass
                elif "S" in [card.name for card in cards]:
                    print(f"{player.name} played a Jester!")
                    current_enemy.immune = False
                    game.tavern_deck.discard_pile.extend(cards)
                    game.player_index = game.choose_next_player(player)
                    player = players[game.player_index]
                    continue
                else:
                    heal_value, draw_value, damage_value, lower_attack_value = RegicideGame.calculate_attack_value(current_enemy, cards)
                    if heal_value:
                        game.heal(maximum_heal_value=heal_value)

                    if draw_value:
                        game.deal_cards(draw_value=draw_value)

                    
                    current_enemy.health -= damage_value
                    current_enemy.attack -= lower_attack_value
                    current_enemy.attack = max(0, current_enemy.attack)
                    # We are allowing the enemy health to be lower than 0 because of the perfect kill game mechanic

                    print(f"{player.name} played {[str(card) for card in cards]}")

                game.tavern_deck.discard_pile.extend(cards)

                if current_enemy.health <= 0:
                    kills += 1
                    if current_enemy.health == 0: game.tavern_deck.discard_pile.append(current_enemy)
                    game.enemies.pop(0)
                    current_enemy = game.enemies[0]
                    continue
                
                game.show_game_infos(enemy=current_enemy)

                # SHIELD PHASE
                if current_enemy.attack > 0:
                    if player.get_hand_value() < current_enemy.attack:
                        game_on = False
                    else:
                        cards = RegicideGame.cards_to_shield(player, current_enemy)
                        game.tavern_deck.discard_pile.extend(cards)
            else:
                game_on = False
        else:
            game_on = False

        game.player_index += 1
        if game.player_index >= len(players): game.player_index = 0

    print(f"Regents killed: {kills}")

if __name__ == "__main__":
    main()
