def next_version(sting):
    new_version = [int(i) for i in sting.split(".")]
    if new_version[2] < 9:
        new_version[2] += 1
    if new_version[2] >= 9:
        new_version[2] = 0
        new_version[1] += 1
    if new_version[1] > 9:
        new_version[1] = 0
        new_version[0] += 1
    return new_version


print(*next_version(input()), sep=".")