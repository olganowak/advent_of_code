with open('input.txt', 'r') as file:
    rules = file.read().split('\n\n')[0]
    file.seek(0)
    pages = file.read().split('\n\n')[1]

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

rules = example.split('\n\n')[0]
pages = file.split('\n\n')[1]

rules = [[int(x) for x in line.split('|')] for line in rules.split('\n')]

pages = [[int(x) for x in line.strip().split(',')] for line in pages.split('\n') if line != '']

incorrect_pages = []
correct_pages = []
for page in pages:
    correct = True
    for i, num in enumerate(page):
        for rule in rules:
            if num == rule[0] and rule[1] in page:
                if page.index(rule[1]) < i:
                    correct = False
                    break
        if correct == False:
            break
    if correct == True:
        correct_pages.append(page)
    if correct == False:
        incorrect_pages.append(page)

result1 = sum([page[len(page)//2] for page in correct_pages])

print(correct_pages)

print("Result 1:", result1)

print(incorrect_pages)

for page in incorrect_pages:
    for i, num in enumerate(page):
        for rule in rules:
            if num == rule[0] and rule[1] in page:
                if page.index(rule[1]) < i:
