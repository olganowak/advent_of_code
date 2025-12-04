# Read input as grid (list of lists so we can mutate)
with open("input.txt") as f:
    grid: list[list[str]] = [list(line.rstrip("\n")) for line in f if line.strip()]

# Dimensions
R = len(grid)
C = len(grid[0]) if R > 0 else 0

# 8 neighbor offsets (N, NE, E, SE, S, SW, W, NW)
NEIGHBORS: list[tuple[int, int]] = [
    (-1,  0), (-1,  1), (0,  1), (1,  1),
    (1,   0), (1,  -1), (0, -1), (-1, -1),
]

def in_bounds(r: int, c: int) -> bool:
    return 0 <= r < R and 0 <= c < C

def count_adjacent_papers(g: list[list[str]], r: int, c: int) -> int:
    """Return number of neighbouring '@' around (r, c)."""
    cnt = 0
    for dr, dc in NEIGHBORS:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc) and g[nr][nc] == "@":
            cnt += 1
    return cnt

def fewer_than_4(g: list[list[str]], r: int, c: int) -> bool:
    """True if the paper at (r,c) has < 4 neighbors."""
    return count_adjacent_papers(g, r, c) < 4


# ---------- PART 1 ----------
def part1(g: list[list[str]]) -> int:
    total = 0
    for r in range(R):
        for c in range(C):
            if g[r][c] == "@" and fewer_than_4(g, r, c):
                total += 1
    return total

print("Result 1:", part1(grid))


# ---------- PART 2 ----------
def part2(g: list[list[str]]) -> int:
    """Mutates the grid in place: when a cell qualifies it is removed immediately."""
    total_removed = 0
    current = [row[:] for row in g]  # make a copy

    while True:
        removed_this_round = 0
        for r in range(R):
            for c in range(C):
                if current[r][c] == "@" and fewer_than_4(current, r, c):
                    current[r][c] = "."
                    removed_this_round += 1

        if removed_this_round == 0:
            break

        total_removed += removed_this_round

    return total_removed

print("Result 2:", part2(grid))
