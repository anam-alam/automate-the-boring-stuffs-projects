
def pic_grid(grid):

    num_row = len(grid[0])
    num_col = len(grid)

    for row in range(0,num_row):
        for col in range(0,num_col):
            print(grid[col][row], end="")
        print()


if __name__ == '__main__':
    grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

    pic_grid(grid)