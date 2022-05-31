import numpy
from Logic import *

grid = []

print('This program will solve your Sudoku puzzle.')
print('Enter 0 for blanks')
print('Enter your numbers of your puzzle row by row. There should not be any spaces between numbers.')

for i in range(1, 10):
    temp = []
    row = input(f'Enter row {i}: ')
    check_row = row.isnumeric()
    length = len(row)
    while not check_row or length != 9:
        if not check_row:
            print('You have not entered a number.')
            print('Enter 0 for blanks')
            print('Enter your numbers of your puzzle row by row. There should not be any spaces between numbers.')
            row = input(f'Enter row {i}: ')
            check_row = row.isnumeric()
            length = len(row)
        else:
            print('You have not entered 9 numbers.')
            row = input(f'Enter row {i}: ')
            check_row = row.isnumeric()
            length = len(row)
    for number in row:
        temp.append(int(number))
    grid.append(temp)

_, grid = solve(grid)
check = True
for y in range(9):
    if check == True:
        for x in range(9):
            if grid[y][x] == 0:
                check = False
                break
    else:
        break
if check == True:
    print(numpy.matrix(grid))
    with open('solution.txt', 'w') as f:
            f.write(str(numpy.matrix(grid)))
else:
    print('There is no solution.')
