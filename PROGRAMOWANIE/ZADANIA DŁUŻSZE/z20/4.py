from itertools import permutations

def GenerateAnagrams(word):

    anagrams = []

    for i in permutations(word):
        anagrams.append(''.join(i))

    anagrams = sorted(list(set(anagrams)))

    return anagrams


file = open('wyrazy.txt', 'r')

for line in file:
    line = line.strip()
    anagrams = GenerateAnagrams(line)
    print(anagrams)
