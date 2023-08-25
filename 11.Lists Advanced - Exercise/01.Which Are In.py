def which_are_in(string1, string2):
    items = list(i for i in string1 for j in string2 if i in j)
    result = [i for n, i in enumerate(items) if i not in items[:n]]
    return result


print(which_are_in(input().split(", "), input().split(", ")))