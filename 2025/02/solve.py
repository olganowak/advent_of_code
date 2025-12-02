with open("input.txt") as f:
    id_ranges = [tuple(int(y) for y in part.split("-")) for part in f.read().split(",")]

invalid_ids = []
for start, end in id_ranges:
    for num in range(start, end + 1):
        s = str(num)
        if len(s) % 2 == 0:
            half = len(s)//2
            if s[:half] == s[half:]:
                invalid_ids.append(num)

result1 = sum(invalid_ids)

print("Result 1:", result1)

invalid_ids = []
for start, end in id_ranges:
    for num in range(start, end + 1):
            invalid_ids_num = set()
            s = str(num)
            for part_len in range(1,len(s)//2+1):
                part = s[:part_len]
                if len(s) % part_len == 0:
                    if part * (len(s)//part_len) == s:
                        invalid_ids_num.add(num)
            for invalid_id in invalid_ids_num:
                invalid_ids.append(invalid_id)

result2 = sum(invalid_ids)

print("Result 2:", result2)
