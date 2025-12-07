with open("input.txt") as f:
    lines = f.read().split("\n")[:-1]


def multiply(list_of_nums):
    """
    Multiply together all numbers in a list.

    Args:
        list_of_nums (list[int]): A list of integers. If empty, returns None.

    Returns:
        int or None: The product of the numbers, or None if the list is empty.
    """
    if not list_of_nums:
        return None
    result = list_of_nums[0]
    for num in list_of_nums[1:]:
        result *= num
    return result


def calculate_sum(list_of_nums, operators):
    """
    Apply a sequence of operations column-wise and return the summed result.

    For each list of numbers in `list_of_nums`, the corresponding operator in
    `operators` determines how they are reduced:
      - "*" multiplies all numbers together
      - "+" sums all numbers together

    Args:
        list_of_nums (list[list[int]]): A list of numeric columns (or groups).
        operators (list[str]): A list of operator symbols, one per column.

    Returns:
        int: The sum of all reduced column results.
    """
    results = []
    for nums, operator in zip(list_of_nums, operators):
        if operator == "*":
            results.append(multiply(nums))
        elif operator == "+":
            results.append(sum(nums))
    return sum(results)


# ------- PART 1 -------
operators = lines[-1].split()
data_lines = lines[:-1]


def part_1_numbers(lines):
    """
    Transform horizontal rows of integers into vertical columns.

    The input consists of space-separated numbers across multiple rows.
    This function rotates that matrix so each column becomes its own list.

    Example:
        Input rows:
            123 328  51 64
             45 64  387 23
              6 98  215 314
        Output columns:
            [[123, 45, 6], [328, 64, 98], [51, 387, 215], [64, 23, 314]]

    Args:
        lines (list[str]): Lines containing space-separated integers.

    Returns:
        list[list[int]]: A list where each inner list is a vertical column.
    """
    numbers_horizontal = [[int(x) for x in line.split()] for line in lines]
    num_columns = len(numbers_horizontal[0])

    numbers_vertical = []
    for index in range(num_columns):
        numbers_vertical.append([row[index] for row in numbers_horizontal])
    return numbers_vertical


print("Result 1:", calculate_sum(part_1_numbers(data_lines), operators))


# ----- PART 2 ------
def part_2_numbers(lines):
    """
    Extract numbers by reading the input grid column-by-column from right to left.

    Each column of characters (not space-separated numbers this time) is treated
    as a vertical string. These strings are reversed per row and stitched together
    to form integer values. Blank columns indicate separation between groups.

    Example concept:
        Input rows:
            "123 328  51 64 "
            " 45 64  387 23 "
            "  6 98  215 314"
        Output columns:
            [[4, 431, 623], [175, 581, 32], [8, 248, 369], [356, 24, 1]]

    Args:
        lines (list[str]): Raw character-based rows.

    Returns:
        list[list[int]]: A grouped list of integers extracted column-wise.
    """
    lines
    num_positions = len(lines[0])

    numbers = []
    numbers_right_to_left = []

    for index in range(num_positions):
        # Collect characters from each row at this column position (measured from the right)
        num = "".join([row[::-1][index] for row in lines])

        cleaned = num.strip()
        if cleaned == "":
            # Empty column → end of group
            numbers_right_to_left.append(numbers)
            numbers = []
        elif index == num_positions - 1:
            # Last column → finalize group
            numbers.append(int(cleaned))
            numbers_right_to_left.append(numbers)
        else:
            numbers.append(int(cleaned))

    return numbers_right_to_left


print("Result 2:", calculate_sum(part_2_numbers(data_lines), operators[::-1]))
