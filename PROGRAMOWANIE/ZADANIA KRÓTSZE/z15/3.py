def IsPrime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


file = open('liczby15.txt', 'r')
prime_numbers = []
solution = {}

for line in file:
    line = int(line.strip())
    if IsPrime(line):
        prime_numbers.append(line)

prime_numbers.sort()

for i in range(len(prime_numbers)):
    for j in range(len(prime_numbers) - 1):
        if abs(int(prime_numbers[i]) - prime_numbers[j] == 2):
            print(prime_numbers[i], prime_numbers[j])

file.close()
