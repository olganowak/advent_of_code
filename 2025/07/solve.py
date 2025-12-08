with open("input.txt") as f:
    grid = f.read().split()   # one string per row


def find_start(grid):
    """Return (row, col) of the 'S' start position."""
    for r, row in enumerate(grid):
        if "S" in row:
            return r, row.index("S")
    raise ValueError("No S found in grid")


# ---------- PART 1: classical manifold ----------

def count_splits(grid):
    """
    Simulate the classical manifold:
    - One beam goes down from S.
    - Beam passes through '.'.
    - At '^' it splits into left/right.
    Returns the total number of splits.
    """
    start_row, start_col = find_start(grid)
    cols = {start_col}
    splits = 0

    # We only care about rows below S
    for row in grid[start_row + 1:]:
        next_cols = set()
        last_col_idx = len(row) - 1

        for c in cols:
            cell = row[c]
            if cell == ".":
                # beam continues straight down
                next_cols.add(c)
            elif cell == "^":
                # beam is split
                splits += 1
                if c > 0:
                    next_cols.add(c - 1)
                if c < last_col_idx:
                    next_cols.add(c + 1)
            # (nothing happens for any other char, which shouldn't appear)

        cols = next_cols

    return splits

print("Result 1:", count_splits(grid))

# ---------- PART 2: quantum / timelines ----------

def count_timelines(grid):
    """
    Simulate the quantum manifold:
    - We track how many timelines have a beam at each column.
    - '.' keeps the count in same column.
    - '^' splits each count into left and right.
    Returns total number of active timelines at the end.
    """
    start_row, start_col = find_start(grid)
    counts = {start_col: 1}  # column -> number of timelines with a particle here

    for row in grid[start_row + 1:]:
        next_counts = {}
        last_col_idx = len(row) - 1

        for c, n in counts.items():
            cell = row[c]
            if cell == ".":
                # all n timelines continue straight
                next_counts[c] = next_counts.get(c, 0) + n
            elif cell == "^":
                # all n timelines split into left and right
                if c > 0:
                    next_counts[c - 1] = next_counts.get(c - 1, 0) + n
                if c < last_col_idx:
                    next_counts[c + 1] = next_counts.get(c + 1, 0) + n

        counts = next_counts

    return sum(counts.values())


print("Result 2:", count_timelines(grid))
