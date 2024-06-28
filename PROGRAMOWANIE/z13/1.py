file = open("liczby13.txt", "r")

def DecToBin(number):
    number = int(number)
    binary = ""

    while number > 0:
        binary += str(number % 2)
        number //= 2

    return binary[::-1]


def CountZerosAndOnes(number):

    zeros = 0
    ones = 0

    for i in range(len(number)):
        if number[i] == "0":
            zeros += 1
        else:
            ones += 1

    return zeros, ones


number_counter = 0

for line in file:
    line = line.replace("\n", "")
    line_in_bin = DecToBin(line)
    zeros, ones = CountZerosAndOnes(line_in_bin)

    if zeros == ones:
        number_counter += 1

print(number_counter)


    
    



