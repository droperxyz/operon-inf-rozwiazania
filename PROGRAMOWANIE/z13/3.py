def DecToHexa(number):
    number = int(number)
    converted = ""
    base = 55

    while number > 0:
        digit = number % 16

        if digit >= 10:
            char = chr(digit + base)
            converted += char
        else:
            converted += str(number % 16)
    
        number //= 16

    return converted[::-1]


file = open("liczby13.txt", "r")

for line in file:
    line = line.replace("\n", "")
    line_to_hexa = DecToHexa(line)
    
    if len(line_to_hexa) > 2:
        if line_to_hexa == line_to_hexa[::-1]:
            print(line)
    
    