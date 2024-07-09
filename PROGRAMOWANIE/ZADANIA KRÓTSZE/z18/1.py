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
                return system
        except:
            continue


file = open('trzyliczby.txt', 'r')
counter = {
    "2": 0, "3": 0, "4": 0, "5": 0,
    "6": 0, "7": 0, "8": 0, "9": 0,
    "10": 0, "11": 0, "12": 0, "13": 0,
    "14": 0, "15": 0, "16": 0
}

for line in file:
    line = line.split()
    system = CheckSystem(line)

    counter[str(system)] += 1

for key, value in counter.items():
    print(f"{key}: {value}")
