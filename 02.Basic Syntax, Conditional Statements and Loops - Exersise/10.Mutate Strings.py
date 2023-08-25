word1 = input()
word2 = input()
mutated_words = [word2[:i+1] + word1[i+1:] for i in range(len(word1)) if word1[i] != word2[i]]

print(*mutated_words, sep="\n")