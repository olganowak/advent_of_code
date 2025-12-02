with open('input.txt', 'r') as file:
    first_list = sorted([int(line.strip().split('   ')[0]) for line in file.readlines()])
    file.seek(0)
    second_list = sorted([int(line.strip().split('   ')[1]) for line in file.readlines()])

result1 = sum([abs(num - second_list[i]) for i, num in enumerate(first_list)])

print('Result 1:', result1)

result2 = sum([num * second_list.count(num) for num in first_list])

print('Result 2:', result2)
