def word_filter(string):
    return list(i for i in string.split() if len(i) % 2 == 0)


print(*word_filter(input()), sep="\n")