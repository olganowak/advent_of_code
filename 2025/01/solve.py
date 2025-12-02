with open('input.txt') as f:
    turns = [line.strip() for line in f]

moves = [(t[0], int(t[1:])) for t in turns]

# PART 1
position = 50
zeros = 0
for direction, num in moves:
    if direction == "L":
        position = (position - num) % 100
    elif direction == "R":
        position = (position + num) % 100
    else:
        raise ValueError(f"Unknown direction: {direction!r}")
    if position == 0:
        zeros += 1

print("Result 1:", zeros)

# PART 2
position = 50
zeros = 0
for direction, num in moves:
    if direction == "L":
        if (position - num) < 0:
            zeros += abs((100 + position - num) // 100)
            if position != 0:
                zeros += 1
        position = (position - num) % 100
        if position == 0:
            zeros += 1
    elif direction == "R":
        zeros += (position + num) // 100
        position = (position + num) % 100
    else:
        raise ValueError(f"Unknown direction: {direction!r}")
result2 = zeros
print("Result 2:", result2)
