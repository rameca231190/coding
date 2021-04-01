# 2D list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# where [0] is the first line of the list and second [0] is the second line of the list.
print(number_grid[2][1])

# Nested loop, loop inside another loop

for row in number_grid:
    for col in row:
        print(col)
