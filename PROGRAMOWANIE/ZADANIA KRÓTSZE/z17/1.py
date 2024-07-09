file = open('pesel.txt', 'r')

men = 0
womans = 0

for line in file:
    line = line.strip()
    if int(line[-2]) % 2 == 0:
        womans += 1
    else:
        men += 1

print(f"Kobiet: {womans} \nMężczyzn: {men}")

file.close()
