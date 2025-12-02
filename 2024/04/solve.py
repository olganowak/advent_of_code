with open('input.txt', 'r') as file:
    grid = file.readlines()

'''grid = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".split('\n')'''

appearances = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if j <= len(grid[0]) - 4 and (grid[i][j:j+4] == 'XMAS' or grid[i][j:j+4] == 'XMAS'[::-1]):
            appearances += 1
            #print(grid[i][j:j+4])
        if i <= len(grid) - 4:
            vertical = ''.join([grid[i+num][j] for num in range(4)])
            if vertical == 'XMAS' or vertical == 'XMAS'[::-1]:
                appearances += 1
                #print(vertical)
        if i <= len(grid) - 4 and j <= len(grid[0]) - 4:
            diagonal = ''.join([grid[i+num][j+num] for num in range(4)])
            if diagonal == 'XMAS' or diagonal == 'XMAS'[::-1]:
                appearances += 1
                ##print(diagonal)
        if i <= len(grid) - 4 and j >= 3:
            diagonal = ''.join([grid[i+num][j-num] for num in range(4)])
            #print(diagonal)
            if diagonal == 'XMAS' or diagonal == 'XMAS'[::-1]:
                appearances += 1

print("Result 1:", appearances)

appearances = 0
for i in range(1,len(grid)-1):
    for j in range(1,len(grid[0])-1):
        diagonal1 = grid[i-1][j-1]+grid[i][j]+grid[i+1][j+1]
        diagonal2 = grid[i-1][j+1]+grid[i][j]+grid[i+1][j-1]
        if (diagonal1 == "MAS" or diagonal1 == "SAM") and (diagonal2 == "MAS" or diagonal2 == "SAM"):
                appearances += 1

print("Result 2:", appearances)
