import re

with open('input.txt', 'r') as file:
    memory = file.read()


matches = re.findall("mul[(]\\d{1,3},\\d{1,3}[)]", memory)

numbers = [re.findall('\\d{1,3}', match) for match in matches]

result1 = sum([int(num[0])*int(num[1]) for num in numbers])

print('Result 1:', result1)

matches = re.findall("(mul[(]\\d{1,3},\\d{1,3}[)]|don't[(][)]|do[(][)])", memory)

disabled = False
result2 = 0
for match in matches:
    if match == "don't()":
        disabled = True
    elif match == "do()":
        disabled = False
    elif match.startswith("mul(") and disabled == False:
        numbers = re.findall('\\d{1,3}', match)
        result2 += int(numbers[0]) * int(numbers[1])

print('Result 2:', result2)
