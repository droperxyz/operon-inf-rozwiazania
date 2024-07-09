file = open('liczby16.txt', 'r')
solution = []

for line in file:
    line = int(line.strip())
    divisors = []

    for i in range(1, line+1):
        if line % i == 0:
            divisors.append(i)

    if len(divisors) == 9:
        solution.append(line)

print(solution)

file.close()
