hand = [4, 10, 6, 8, 7, 4, 5, 2, 1]

card_indexes = [int(index) - 1 for index in sorted(input("Choose cards \n"), reverse=True)]

print(card_indexes)

played = [hand.pop(index) for index in card_indexes][::-1]

print(played)