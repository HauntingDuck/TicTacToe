
import random
GRID_SIZE = 3

def display_grid(X_pos, O_pos):
    print(X_pos)
    for row in range(GRID_SIZE):
        row_display = ""
        for col in range(GRID_SIZE):
            if (row,col) in X_pos:    
                row_display += "x "  #Player
            elif (row, col) in O_pos:
                row_display += "o "  #Bot
            else:
                row_display += ". "
        print(row_display)

X_pos= []
O_pos= []


# 1(0,0) 2(0,1) 3(0,2)
# 4(1,0) 5(1,1) 6(1,2)
# 7(2,0) 8(2,1) 9(2,2)

WINNING_COMBINATION  =[
    ((0,0), (0,1), (0,2)),
    ((1,0), (1,1), (1,2)),
    ((2,0), (2,1), (2,2)),
    ((0,0), (1,1), (2,2)),
    ((2,0), (1,1), (0,2)),
    ((0,0), (1,0), (2,0)),
    ((0,1), (1,1), (2,1)),
    ((0,2), (1,2), (2,2)),
]



# make_move -> board, row, col, player
# board[row][col] == ' '


def make_move(board,move,player):
    row,col = move
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    return False


def computer_move(board):
    pass

display_grid(1,3 , 1,2)

# print("__|__|__", "__|__|__", "  |  |  ", sep='\n')
