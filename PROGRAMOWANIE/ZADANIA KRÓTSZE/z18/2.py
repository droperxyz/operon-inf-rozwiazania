def CheckSystem(numbers):
    first_num = numbers[0]
    second_num = numbers[1]
    third_num = numbers[2]

    for system in range(2, 17):
        try:
            first_num_converted = int(first_num, system)
            second_num_converted = int(second_num, system)
            third_num_converted = int(third_num, system)
            if first_num_converted + second_num_converted == third_num_converted:
                return first_num_converted, second_num_converted, third_num_converted
        except:
            continue


file = open('trzyliczby.txt', 'r')
numbers = []
for line in file:
    line = line.split()
    first, second, third = CheckSystem(line)

    numbers.append(first)
    numbers.append(second)
    numbers.append(third)

print(f"Najmniejsza: {min(numbers)}")
print(f"Najwieksza: {max(numbers)}")
