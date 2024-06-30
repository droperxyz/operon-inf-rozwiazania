def GetFibElements():
    fib_elements = [1, 1]

    while fib_elements[-1] < 1000000000:
        fib_elements.append(fib_elements[-2] + fib_elements[-1])
    return fib_elements

def IsPrime(line):
    number = line
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


file = open('liczby14.txt', 'r')
fib_elements = GetFibElements()
prime_numbers = []
for line in file:
    line = int(line.strip())
    if line in fib_elements and IsPrime(line):
        prime_numbers.append(line)

prime_numbers.sort()
print(prime_numbers)

file.close()