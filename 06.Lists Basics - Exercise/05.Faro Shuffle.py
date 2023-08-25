string = input().split()
n = int(input())
for shuffles in range(n):
    string = string
    shuffle = [[string[i], string[int(len(string)/2+i)]] for i in range(int(len(string)/2))]
    faro_shuffle = [word for words in shuffle for word in words]
    string = faro_shuffle

print(string)
