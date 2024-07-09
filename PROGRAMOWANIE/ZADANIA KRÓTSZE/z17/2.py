def CheckPesel(pesel):
    weight = "1379137913"
    sum_of_pesel_digits = 0
    control_digit_in_given_pesel = int(pesel[-1])

    for i in range(len(pesel) - 1):
        temp = int(weight[i]) * int(pesel[i])
        sum_of_pesel_digits += temp % 10

    control_digit = 10 - sum_of_pesel_digits % 10

    return control_digit == control_digit_in_given_pesel


file = open('pesel.txt', 'r')
incorrect = []

for line in file:
    line = line.strip()
    if not CheckPesel(line):
        incorrect.append(line)

print(incorrect)
