def GetFibElements():
    fib_elements = [1, 1]


    while fib_elements[-1] < 1000000000:
        fib_elements.append(fib_elements[-2] + fib_elements[-1])
    return fib_elements

def CategoryPMOne(fib_elements, line):
    number = int(line)
    plus_one = number + 1
    minus_one = number - 1

    if number in fib_elements:
        return False

    if plus_one in fib_elements or minus_one in fib_elements:
        return True

    return False

def CategoryPMTwo(fib_elements, line):
    number = int(line)
    plus_two = number + 2
    minus_two = number - 2

    if number in fib_elements:
        return False

    if plus_two in fib_elements or minus_two in fib_elements:
        return True

    return False

def CategoryPMThree(fib_elements, line):
    number = int(line)
    plus_three = number + 3
    minus_three = number - 3

    if number in fib_elements:
        return False

    if plus_three in fib_elements or minus_three in fib_elements:
        return True

    return False

fib_elements = GetFibElements()
p_m_one_numbers = []
p_m_two_numbers = []
p_m_three_numbers = []

file = open('liczby14.txt', 'r')

for line in file:
    line = int(line.strip())

    if CategoryPMOne(fib_elements, line):
        p_m_one_numbers.append(line)

    if CategoryPMTwo(fib_elements, line):
        p_m_two_numbers.append(line)

    if CategoryPMThree(fib_elements, line):
        p_m_three_numbers.append(line)

p_m_one_numbers.sort()
p_m_two_numbers.sort()
p_m_three_numbers.sort()
print(f"Bliskie +- 1: {p_m_one_numbers}\nBliskie +- 2: {p_m_two_numbers}\nBliskie +- 3: {p_m_three_numbers}")



