import numpy as np
from itertools import combinations

with open("input.txt") as f:
    points = [np.array([int(x) for x in line.split(",")]) for line in f.read().split()]

C = 1_000

pairs = list(combinations(points, 2))

distances = {}
for p1, p2 in pairs:
    distances[np.linalg.norm(p2 - p1)] = [tuple(p1), tuple(p2)]

distances = dict(sorted(distances.items()))

circuits = {}
for i, point in enumerate(points):
    circuits[i+1] = [tuple(point)]

points = {}
for c, p in circuits.items():
    for point in p:
        points[point] = c

def part1(distances, circuits, points, connections):
    counter = 0
    for distance, (p1, p2) in distances.items():
        c1 = points[p1]
        c2 = points[p2]
        if c1 != c2:
            for p in circuits[max(c1,c2)]:
                circuits[min(c1, c2)].append(p)
            del circuits[max(c1,c2)]
        points = {}
        for c, p in circuits.items():
            for point in p:
                points[point] = c
        counter += 1
        if counter == connections:
            break
    len_circuits = []
    for c, p in circuits.items():
        len_circuits.append(len(p))

    len_circuits.sort(reverse=True)

    return len_circuits[0] * len_circuits[1] * len_circuits[2]

result1 = part1(distances, circuits, points, C)
print("Result 1:", result1)

circuits = {}
for i, point in enumerate(points):
    circuits[i+1] = [tuple(point)]

points = {}
for c, p in circuits.items():
    for point in p:
        points[point] = c

def part2(distances, circuits, points):
    for distance, (p1, p2) in distances.items():
        c1 = points[p1]
        c2 = points[p2]
        if c1 != c2:
            for p in circuits[max(c1,c2)]:
                circuits[min(c1, c2)].append(p)
            del circuits[max(c1,c2)]
        points = {}
        for c, p in circuits.items():
            for point in p:
                points[point] = c
        if len(circuits) == 1:
            return p1[0] * p2[0]

result2 = part2(distances, circuits, points)

print("Result 2:", result2)
