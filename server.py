# > width = 8
# > height = 4
# > number_of_mines = 8
# > generate_board(width, height, number_of_mines)
# *112*100
# 123*3222
# 01**31**
# 013*2122

# board = list
# each row of the board = list - 4 with 8 items inside (start all items with 0)
# randomizing the mines: random index for the row, random index for item inside the row
# iterate through each item, count how many mines next to that item
# if the item is a mine, skip it
# look at the item indexed lower and higher in the row, also look at the rows above and below the item, index higher, the same, and lower
# counting up the mines and replacing the 0 with the new count
# generate in terminal by printing each row

from random import randint

def generate_board(width, height, number_of_mines):
    """Generate minesweeper board"""
    
    board = []
    for i in range(height):
        row = []
        for i in range(width):
            row.append(0)
        board.append(row)
        
    mines = set()
    
    while len(mines) < number_of_mines:
        row_index = randint(0, height - 1)
        item_index = randint(0, width - 1)
        mines.add((row_index, item_index))
        
    for mine in mines:
        board[mine[0]][mine[1]] = '*'
        
    for row in range(height):
        for item in range(width):
            count = 0
            if board[row][item] == '*':
                continue
            else:
                if item > 0:
                    if board[row][item - 1] == '*':
                        count += 1
                if item < width - 2:
                    if board[row][item + 1] == '*':
                        count += 1
            board[row][item] = count                      
        
    print(board)
    
    
generate_board(4, 4, 2)