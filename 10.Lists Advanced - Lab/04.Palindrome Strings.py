palindromes = [i for i in input().split(" ") if i == i[::-1]]
wanted_palindrome = input()
number = palindromes.count(wanted_palindrome)

print(palindromes)
print(f"Found palindrome {number} times")