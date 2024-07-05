def IsPrime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


file = open('liczby15.txt', 'r')
counter = 0

for line in file:
    line = line.strip()
    line = int(line)

    if IsPrime(line):
        counter += 1

print(counter)

file.close()
