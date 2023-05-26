grid = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
]

#apply this to future functions to print properly
def properly_aligned(grid):
    for row in grid:
        print(row)


def alternate_vertical(grid, row, col, row2, char):
    row -= 1 
    col -= 1
    flag = True
    for x in range(row, row2):
        if flag == True:
            grid[x][col] = char
            flag = False
        elif flag == False:
            flag = True
            continue
    return grid
#properly_aligned(alternate_vertical(grid, 1, 1, 10, 1))


#creation of vertical line 
def vertical_line(grid, row, col, row2, char):
    row -= 1
    col -= 1
    for x in range(row, row2):
        grid[x][col] = char
    return grid
#properly_aligned(vertical_line(grid, 1, 1, 8, 1))


#horizontal line
def horizontal_line(grid, row, col, col2, char):
    row -= 1
    col -= 1
    for x in range(col, col2):
        grid[row][x] = char
    return grid
#properly_aligned(horizontal_line(grid, 2, 2, 9, 1))


#diagonal line
def diagonal_line(grid, row, col, row2, char):
    index = col
    for x in range(row, row2):
        grid[x][index] = char
        index += 1
    return grid
#properly_aligned(diagonal_line(grid, 1, 1, 10, 1))
        

#get all corners of the map marked
def four_corners(grid):
    row_length = len(grid[0]) - 1
    col_length = len(grid) - 1
    grid[0][0] = 1
    grid[0][row_length] = 1
    grid[col_length][0] = 1
    grid[col_length][row_length] = 1
    return grid
#properly_aligned(four_corners(grid))


#exchange individual point on the map with int of your choosing
def pin_point(grid, row, col, char):
    grid[row-1][col-1] = char
    return grid
#properly_aligned(pin_point(grid, 1, 1, 7))