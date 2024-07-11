def IsAnagram(w1, w2):
    if len(w1) != len(w2):
        return False
    return sorted(w1) == sorted(w2)

def LetterAndIndex(w1, w2):
    w1 = list(w1)
    w2 = list(w2)

    w1_copy = w1.copy()
    w2_copy = w2.copy()

    for letter in reversed(w1_copy):
        if letter in w2_copy:
            w1_copy.remove(letter)
            w2_copy.remove(letter)

    return w1_copy, w2_copy


file = open('anagramy.txt', 'r')

for line in file:
    line = line.split()
    w1 = line[0]
    w2 = line[1]

    replacement, to_be_replaced = LetterAndIndex(w1, w2)
    if not (IsAnagram(w1, w2)):
        if len(w1) == len(w2):
            if len(replacement) == 1:
                index = w2.find(to_be_replaced[0])
                print(w1, w2, index+1, replacement[0])

file.close()
