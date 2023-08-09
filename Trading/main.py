import math
import copy


def distance(x, y):
    x0, x1 = x
    y0, y1 = y
    return math.sqrt((x0 - y0) * (x0 - y0) + (x1 - y1) * (x1 - y1))


def findClosest(coordinates, x, size):
    if size <= 3:
        min_val = 10000000000
        for i in range(size):
            j = i + 1
            while j < size:
                temp_distance = distance(coordinates[i], coordinates[j])
                if min_val > temp_distance:
                    min_val = temp_distance
                j += 1
        return min_val
    middle_value = math.floor(size / 2)
    midPoint = coordinates[middle_value]
    left_coord = []
    right_coord = []
    for z in range(middle_value):
        left_coord.append(coordinates[z])
    for y in range(middle_value, size):
        right_coord.append(coordinates[y])
    smallest_left = findClosest(left_coord, x, middle_value)
    smallest_right = findClosest(right_coord, x, size - middle_value)
    smallest_distance = min(smallest_left, smallest_right)
    stripP = []
    stripQ = []
    lr = left_coord + right_coord
    for i in range(size):
        if abs(lr[i][0] - midPoint[0]) < smallest_distance:
            stripP.append(lr[i])
        if abs(x[i][0] - midPoint[0]) < smallest_distance:
            stripQ.append(x[i])
    stripP.sort(key=lambda point: point[1])
    min_val_a = min(smallest_distance, strip(stripP, len(stripP), smallest_distance))
    min_val_b = min(smallest_distance, strip(stripQ, len(stripQ), smallest_distance))
    closest_distance = min(min_val_a, min_val_b)
    return closest_distance


def strip(strip, size, smallest_distance):
    for a in range(size):
        b = a + 1
        while b < size and strip[b][1] - strip[a][1] < smallest_distance:
            smallest_distance = distance(strip[a], strip[b])
            b += 1
    return smallest_distance


coordinates = []
numStars = int(input())
for i in range(numStars):
    temp = []
    x, y = input().split()
    x = float(x)
    y = float(y)
    temp.append(x)
    temp.append(y)
    coordinates.append(temp)
while numStars != 0:
    coordinates.sort(key=lambda coordinates: coordinates[0])
    x = copy.deepcopy(coordinates)
    x.sort(key=lambda coordinates: coordinates[1])
    closest = findClosest(coordinates, x, len(coordinates))
    closest = float(closest)
    if closest < 10000.0:
        print("%.4f" % closest)
    else:
        print("infinity")
    coordinates.clear()
    numStars = int(input())
    for i in range(numStars):
        temp = []
        x, y = input().split()
        x = float(x)
        y = float(y)
        temp.append(x)
        temp.append(y)
        coordinates.append(temp)
