with open('input.txt', 'r') as file:
    reports = [[int(num) for num in line.strip().split(' ')] for line in file.readlines()]

result1 = 0

for report in reports:
    steps = [num - report[i+1] for i, num in enumerate(report) if i != len(report)-1]

    all_positive = all([step > 0 for step in steps])
    all_negative = all([step < 0 for step in steps])
    max_3 = all([abs(step)<= 3 for step in steps])

    if (all_positive or all_negative) and max_3:
        result1 += 1

print('Result 1:', result1)

result2 = 0

for report in reports:
    for index in range(len(report)):
        report_removed = [num for i, num in enumerate(report) if i != index]
        steps = [num - report_removed[i+1] for i, num in enumerate(report_removed) if i != len(report_removed)-1]

        all_but_1_positive = all([step > 0 for step in steps])
        all_negative = all([step < 0 for step in steps])
        max_3 = all([abs(step)<= 3 for step in steps])

        if (all_but_1_positive or all_negative) and max_3:
            result2 += 1
            break

print('Result 2:', result2)
