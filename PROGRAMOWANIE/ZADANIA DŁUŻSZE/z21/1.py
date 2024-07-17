def Factorize(number):
	factors = []
	factor = 2
	while factor*factor <= number:
		while number % factor == 0:
			factors.append(factor)
			number //= factor
		factor += 1
	if number > 1:
		factors.append(number)

	return factors[0], factors[1]


file = open('klucze.txt', 'r')
lowest_prime = float('inf')
highest_prime = 0

for line in file:
	line = line.split()

	n = int(line[0])
	e = int(line[1])
	d = int(line[2])

	p, q = Factorize(n)

	if p > highest_prime:
		highest_prime = p

	if p < lowest_prime:
		lowest_prime = p

	if q > highest_prime:
		highest_prime = q

	if q < lowest_prime:
		lowest_prime = q

print(lowest_prime, highest_prime)

file.close()
