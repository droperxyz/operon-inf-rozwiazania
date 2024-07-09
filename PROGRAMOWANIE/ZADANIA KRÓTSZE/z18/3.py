def CountChars(numbers):
    first_str = numbers[0]
    second_str = numbers[1]
    third_str = numbers[2]
    number_of_chars = len(first_str) + len(second_str) + len(third_str)

    temp = {
        "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
        "6": 0, "7": 0, "8": 0, "9": 0,
        "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0
    }

    for i in range(16):
        if i >= 10:
            base = 55
            to_check = chr(base + i)
        else:
            to_check = str(i)

        icount_f = first_str.count(to_check)
        icount_s = second_str.count(to_check)
        icount_t = third_str.count(to_check)

        temp[to_check] += icount_f
        temp[to_check] += icount_s
        temp[to_check] += icount_t

    return temp, number_of_chars


def CalculateOccurence(letter, amount, total_letters):
    percent = 100 * (amount / total_letters)
    return letter, percent


file = open('trzyliczby.txt', 'r')
total_letters = 0

all_chars = {
    "0":0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
    "6": 0, "7": 0, "8": 0, "9": 0,
    "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0
}

occurences = {
    "0":0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0,
    "6": 0, "7": 0, "8": 0, "9": 0,
    "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0
}

for line in file:
    line = line.split()
    temp, number_of_chars = CountChars(line)
    print(number_of_chars)
    total_letters += number_of_chars

    for key, value in temp.items():
        all_chars[key] += value

    for key, value in all_chars.items():
        letter, percent = CalculateOccurence(key, value, total_letters)
        percent = round(percent, 2)
        occurences[letter] = percent

print(occurences)
