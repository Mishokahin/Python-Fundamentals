cipher = list([word for word in input().split()])
digit_indexes = []
for i, word in enumerate(cipher):
    digits = 0
    for k, letter in enumerate(word):
        if letter.isdigit():
            digits += 1
    digit_indexes.append(digits)

garbled = list(chr(int(cipher[i][:digit_indexes[i]])) for i in range(len(cipher)))
letters = list(cipher[i][digit_indexes[i]:] for i in range(len(cipher)))
deciphered = []

for i, word in enumerate(letters):
    words = ""
    for k, letter in enumerate(word):
        if k == 0:
            words += word[len(word)-1]
        elif k == len(word)-1:
            words += word[0][0]
        else:
            words += letter
    deciphered.append(garbled[i] + words)

print(*deciphered)