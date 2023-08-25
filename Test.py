import random

suits = [u"\u2666", u"\u2665", u"\u2663", u"\u2660"]
num_cards = [str(i) for i in range(2, 10)]
face_cards = ["T", "J", "Q", "K", "A"]
all_cards = num_cards + face_cards
deck = []
for suit in suits:
    for card in all_cards:
        deck.append(suit + card)


def card_value(hand):
    value = 0
    for c in hand:
        if c[1] in num_cards:
            value += int(c[1])
        elif c[1] in face_cards[0:4]:
            value += 10
        else:
            value += 11
    return value
