import math

def CalculateDistance(x, y):
    return math.sqrt(abs((0 - x) **2) + abs((0 + y)**2))


file = open('oddzialy.txt', 'r')
losses = 0
out_of_range = 0
soldiers_in_each_squad = 100
min_distance = 0.1
max_distance = 20
farthest_squad = 0

for line in file:
    line = line.split()
    x = int(line[0])
    y = int(line[1])
    distance_to_squad = CalculateDistance(x, y)

    if distance_to_squad > farthest_squad:
        farthest_squad = distance_to_squad

file.close()

rounded = round(farthest_squad, 3)
rounded_incremented = round(rounded + 0.001, 3)
print(rounded_incremented)
