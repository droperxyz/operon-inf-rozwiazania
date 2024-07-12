from itertools import permutations

word = "bura"
anagrams = []

for i in permutations(word):
	anagrams.append(''.join(i))

anagrams = sorted(list(set(anagrams)))

print(anagrams)
