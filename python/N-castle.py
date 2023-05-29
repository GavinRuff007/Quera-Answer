import numpy as np
def s(board, row, col):
    if np.sum(board[row, :]) > 0:
        return False
    if np.sum(board[:, col]) > 0:
        return False
    n = board.shape[0]
    diag1 = np.diag(board, col - row)
    diag2 = np.diag(np.fliplr(board), n - col - 1 - row)
    if np.sum(diag1) > 0 or np.sum(diag2) > 0:
        return False  
    return True
def solve_n_castle(board, n, col=0):
    if col >= n:
        return board 
    for row in range(n):
        if s(board, row, col):
            board[row, col] = 1
            result = solve_n_castle(board, n, col + 1)
            if result is not None:
                return result
            board[row, col] = 0
    return None
def n_castle(n):
    board = np.zeros((n, n), dtype=int)
    return solve_n_castle(board, n)
n = int(input())
result = n_castle(n)
print(result)