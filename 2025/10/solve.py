from itertools import combinations

with open("input.txt") as f:
    input_text = f.read().strip()

manual = []
for line in input_text.split("\n"):
    diagram = [x for x in line.split("]")[0][1:]]
    buttons = [tuple(int(y) for y in x[1:-1].split(",")) for x in line.split("]")[1].split("{")[0].strip().split(" ")]
    machine = [diagram, buttons]
    manual.append(machine)

def fewest_button_presses(goal_diagram, buttons):
    for n_combinations in range(1, len(buttons) + 1):
        for combination in list(combinations(buttons, n_combinations)):
            start_diagram = ["." for x in range(len(goal_diagram))]
            for button in combination:
                for num in button:
                    if start_diagram[num] == ".":
                        start_diagram[num] = "#"
                    elif start_diagram[num] == "#":
                        start_diagram[num] = "."
            if start_diagram == goal_diagram:
                return n_combinations


button_presses = []
for goal_diagram, buttons in manual:
    start_diagram = ["." for x in range(len(goal_diagram))]
    button_presses.append(fewest_button_presses(goal_diagram, buttons))

print("Result 1:", sum(button_presses))
