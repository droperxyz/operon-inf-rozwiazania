import math

def CalculateDistance(x_coor, y_coor, x_squad, y_squad):
    return math.sqrt(abs((x_coor - x_squad) ** 2) + abs((y_coor - y_squad) ** 2))


def GoingToSD(x, y):
    if CalculateDistance(x_coor, y_coor, 0, 0) <= 2:
        return True
    return False


file = open('oddzialy.txt', 'r')
losses = 0
losses_temp = 0
where_shot = []

for x_coor in range(0, 21):
    for y_coor in range(0, 21):
        if not GoingToSD(x_coor, y_coor):
            losses_temp = 0
            file.seek(0)
            for line in file:
                line = line.split()
                x_squad = int(line[0])
                y_squad = int(line[1])

                distance_to_squad = CalculateDistance(x_coor, y_coor, x_squad, y_squad)

                if 0 < distance_to_squad < 2:
                    losses_temp += 100
                elif distance_to_squad == 2:
                    losses_temp += 75

                if losses_temp > losses:
                    where_shot.clear()
                    losses = losses_temp
                    where_shot = [x_coor, y_coor]

file.close()

print(losses, where_shot)
