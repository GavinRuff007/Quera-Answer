import numpy as np
def v(board, row, col):
    if np.sum(board[row,:]) > 0 or np.sum(board[:,col]) > 0:
        return False
    n = board.shape[0]
    for i in range(n):
        if (row-i >= 0 and col-i >= 0 and board[row-i,col-i] == 1) or \
           (row+i < n and col+i < n and board[row+i,col+i] == 1) or \
           (row-i >= 0 and col+i < n and board[row-i,col+i] == 1) or \
           (row+i < n and col-i >= 0 and board[row+i,col-i] == 1):
            return False
    return True
def solve(n):
    board = np.zeros((n,n), dtype=int)   
    def back(row):
        if row == n:
            return True  
        for col in range(n):
            if v(board, row, col):
                board[row,col] = 1
                if back(row+1):
                    return True
                board[row,col] = 0       
        return False   
    back(0)   
    return board
n = int(input())
board = solve(n)
print(board)