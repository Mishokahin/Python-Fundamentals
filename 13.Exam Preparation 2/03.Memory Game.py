def is_valid_index(idx, seq):
    return 0 <= idx < seq


def indexes_are_valid(index1, index2, seq):
    return is_valid_index(index1, seq) and is_valid_index(index2, seq) and index1 != index2


cards = input().split(" ")
command = input()
moves = 0

while command != "end":
    moves += 1
    idx1, idx2 = [int(el) for el in command.split()]
    if indexes_are_valid(idx1, idx2, len(cards)):
        if cards[idx1] == cards[idx2]:
            found_card = cards[idx1]
            print(f"Congrats! You have found matching elements - {cards[idx1]}!")
            cards = [card for card in cards if card != found_card]
        else:
            print("Try again!")
    else:
        print("Invalid input! Adding additional elements to the board")
        cards.insert(int(len(cards)/2), f"-{moves}a")
        cards.insert(int(len(cards) / 2), f"-{moves}a")

    if len(cards) == 0:
        print(f"You have won in {moves} turns!")
        exit()

    command = input()

print("Sorry you lose :(")
print(f"{' '.join(cards)}")