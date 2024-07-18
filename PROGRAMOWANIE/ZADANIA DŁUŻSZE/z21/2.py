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

def NWD(a,b):
	while b != 0:
		r = a % b
		a = b
		b = r
	return a


file = open('klucze.txt', 'r')

wrong_keys = []
for line in file:
	line = line.split()

	n = int(line[0])
	e = int(line[1])
	d = int(line[2])

	p, q = Factorize(n)
	x = (p-1) * (q-1)

	if not NWD(e, x) or (e*d) % x != 1:
		wrong_keys.append(n)


for wrong_key in wrong_keys:
	print(wrong_key)

file.close()
