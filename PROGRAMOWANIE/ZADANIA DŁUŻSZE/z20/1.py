file = open('anagramy.txt', 'r')
counter = 0

for line in file:
    line = line.split()
    first_word = list(line[0])
    second_word = list(line[1])

    first_word.sort()
    second_word.sort()

    if first_word == second_word:
        counter += 1

print(counter)
