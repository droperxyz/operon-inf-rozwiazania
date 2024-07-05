def GetFibElements():
    fib_elements = [1, 1]

    while fib_elements[-1] < 1000000000:
        fib_elements.append(fib_elements[-2] + fib_elements[-1])
    return fib_elements


file = open('liczby14.txt', 'r')
fib_elements = GetFibElements()
fib_elements_in_file = 0
seen = []

for line in file:
    line = int(line.strip('\n'))

    if line in fib_elements and line not in seen:
        fib_elements_in_file += 1
    seen.append(line)

print(fib_elements_in_file)
