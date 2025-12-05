with open("input.txt") as f:
    content = f.read().split("\n\n")
    valid_ranges = [tuple(int(num) for num in line.split("-")) for line in content[0].split("\n")]
    ingredients = [int(line) for line in content[1].strip().split("\n")]

def in_ranges(ingredient, ranges):
    for start, end in valid_ranges:
        if ingredient >= start and ingredient <= end:
            return True
    return False

fresh_ingredients = 0
for ingredient in ingredients:
    if in_ranges(ingredient, valid_ranges):
        fresh_ingredients += 1

print("Result 1:", fresh_ingredients)

# Merge overlapping/adjacent ranges
def merge_ranges(ranges):
    if not ranges:
        return []
    # sort by start
    ranges_sorted = sorted(ranges, key=lambda x: x[0])
    merged = [ranges_sorted[0]]
    for s, e in ranges_sorted[1:]:
        last_s, last_e = merged[-1]
        # If current start is <= last_end + 1 we merge (treat adjacent as contiguous)
        if s <= last_e + 1:
            # extend the last range if needed
            if e > last_e:
                merged[-1] = (last_s, e)
        else:
            merged.append((s, e))
    return merged

merged_ranges = merge_ranges(valid_ranges)

valid_ids = 0
for start, end in merged_ranges:
    valid_ids += end - start + 1

print("Result 2:", valid_ids)
