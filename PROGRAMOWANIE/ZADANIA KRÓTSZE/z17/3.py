file = open('pesel.txt', 'r')

solution = {
    "<=18": 0,
    "19 - 50": 0,
    "51 - 100": 0,
    "100+": 0
}

for line in file:
    line = line.strip()
    age = 0
    yr_of_born = 0

    if int(line[2]) == 0 or int(line[2]) == 1:
        yr_of_born = 1900 + int(line[0:2])
        age = 2022 - yr_of_born
    elif int(line[2]) == 8:
        yr_of_born = 1800 + int(line[0:2])
        age = 2022 - yr_of_born
    elif int(line[2]) == 2:
        yr_of_born = 2000 + int(line[0:2])
        age = 2022 - yr_of_born
    elif int(line[2]) == 4:
        yr_of_born = 2100 + int(line[0:2])
        age = 2022 - yr_of_born
    elif int(line[2]) == 6:
        yr_of_born = 2200 + int(line[0:2])
        age = 2022 - yr_of_born

    if age <= 18:
        solution["<=18"] += 1
    elif 19 <= age <= 50:
        solution["19 - 50"] += 1
    elif 51 <= age <= 100:
        solution["51 - 100"] += 1
    elif age > 100:
        solution["100+"] += 1

for key, value in solution.items():
    print(f"{key}: {value}")

file.close()
