n = int(input())
word = input()
string = [input() for i in range(n)]
filtered = [string[i] for i in range(len(string)) if str(string[i]).find(word) >= 0]
print(string)
print(filtered)