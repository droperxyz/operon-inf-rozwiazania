def NWD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


file = open('liczby16.txt', 'r')
numbers = []
counter = 0

for line in file:
    line = line.strip()
    numbers.append(line)

for i in range(len(numbers)):
    for j in range(len(numbers) - 1 - i):
        if NWD(int(numbers[i]), int(numbers[j+i+1])) == 1:
            counter += 1

print(counter)

file.close()
