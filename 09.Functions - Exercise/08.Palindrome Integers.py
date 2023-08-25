def palindrome_integers(string):
    numbers = [i for i in string.split(", ")]
    results = []
    for i in numbers:
        if i == i[::-1]:
            results.append(True)
        else:
            results.append(False)
    return results


print(*palindrome_integers(input()), sep="\n")