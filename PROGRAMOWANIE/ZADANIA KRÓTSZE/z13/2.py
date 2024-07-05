def DecToAny(number, system):
    number = int(number)
    converted = ""
    base = 55

    while number > 0:
        digit = number % system

        if digit >= 10:
            char = chr(digit + base)
            converted += char
        else:
            converted += str(number % system)
    
        number //= system

    return converted[::-1]

def CountHighestValues(base_5, base_7, base_13):
    base_5_biggest_value_counter = 0
    base_7_biggest_value_counter = 0
    base_13_biggest_value_counter = 0
   
    for i in range(len(base_5)):
        if base_5[i] == "4":
            base_5_biggest_value_counter += 1
    
    for i in range(len(base_7)):
        if base_7[i] == "6":
           base_7_biggest_value_counter += 1

    for i in range(len(base_13)):
       if base_13[i] == "C":
           base_13_biggest_value_counter += 1

    return base_5_biggest_value_counter, base_7_biggest_value_counter, base_13_biggest_value_counter

file = open("liczby13.txt", "r")

base_5_highest_value_greatest_occurences = 0
base_7_highest_value_greatest_occurences = 0
base_13_highest_value_greatest_occurences = 0

base_5_with_most_of_highest_value = []
base_7_with_most_of_highest_value = []
base_13_with_most_of_highest_value = []

for line in file:
    line = line.replace("\n", "")

    base_5 = DecToAny(line, 5)
    base_7 = DecToAny(line, 7)
    base_13 = DecToAny(line, 13)

    highest_values_counter = CountHighestValues(base_5, base_7, base_13)

    if highest_values_counter[0] == base_5_highest_value_greatest_occurences:
        base_5_with_most_of_highest_value.append(line)
    elif highest_values_counter[0] > base_5_highest_value_greatest_occurences:
        base_5_with_most_of_highest_value.clear()
        base_5_highest_value_greatest_occurences = highest_values_counter[0]
        base_5_with_most_of_highest_value.append(line)
    
    if highest_values_counter[1] == base_7_highest_value_greatest_occurences:
        base_7_with_most_of_highest_value.append(line)
    elif highest_values_counter[1] > base_7_highest_value_greatest_occurences:
        base_7_with_most_of_highest_value.clear()
        base_7_highest_value_greatest_occurences = highest_values_counter[1]
        base_7_with_most_of_highest_value.append(line)

    if highest_values_counter[2] == base_13_highest_value_greatest_occurences:
        base_13_with_most_of_highest_value.append(line)
    elif highest_values_counter[2] > base_13_highest_value_greatest_occurences:
        base_13_with_most_of_highest_value.clear()
        base_13_highest_value_greatest_occurences = highest_values_counter[2]
        base_13_with_most_of_highest_value.append(line)

print(base_5_with_most_of_highest_value, base_7_with_most_of_highest_value, base_13_with_most_of_highest_value)
