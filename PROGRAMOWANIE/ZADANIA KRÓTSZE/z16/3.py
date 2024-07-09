file = open('liczby16.txt', 'r')
solution = []

for line in file:
    line = int(line.strip())
    divisors = []
    sum_of_divisors = 0

    for i in range(1, line):
        if line % i == 0:
            divisors.append(i)

    for i in range(len(divisors)):
        sum_of_divisors += divisors[i]

    if sum_of_divisors == line:
        solution.append(line)

print(solution)
