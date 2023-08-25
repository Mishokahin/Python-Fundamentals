def no_vowels(string):
    vowels = list(['a', 'o', 'u', 'e', 'i']) + list(str(i).upper() for i in ['a', 'o', 'u', 'e', 'i'])
    return list([i for i in string if i not in vowels])


print(*no_vowels(input()), sep='')