import math

def CalculateDistance(x, y):
    return math.sqrt(abs((0 - x) **2) + abs((0 + y)**2))


file = open('oddzialy.txt', 'r')
losses = 0
out_of_range = 0
soldiers_in_each_squad = 100
min_distance = 1
max_distance = 20

for line in file:
    line = line.split()
    x = int(line[0])
    y = int(line[1])
    distance_to_squad = CalculateDistance(x, y)

    if distance_to_squad < min_distance or distance_to_squad > max_distance:
        out_of_range += 1
    elif min_distance < distance_to_squad < max_distance:
        losses += soldiers_in_each_squad
    elif distance_to_squad == max_distance:
        losses += soldiers_in_each_squad * 0.25
    elif distance_to_squad == min_distance:
        losses += soldiers_in_each_squad * 0.25
        
file.close()

print(losses, out_of_range)
