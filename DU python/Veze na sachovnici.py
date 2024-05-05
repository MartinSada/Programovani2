def canPlace(board, row, col, n):
    return row >= 0 and col >= 0 and row < n and col < n and board[row][col] == '.'

def isSafe(board, row, col, n):
    for i in range(n):
        if board[row][i] == 'V' or board[i][col] == 'V':
            return False
    return True

def placeTower(board, col, n):
    if col == n:
        return 1
    count = 0
    for i in range(n):
        if canPlace(board, i, col, n) and isSafe(board, i, col, n):
            board[i][col] = 'V'
            count += placeTower(board, col + 1, n)
            board[i][col] = '.'
    return count

def validArrangements(n, board):
    board = [list(row) for row in board]
    return placeTower(board, 0, n)

n = int(input())
board = [input() for _ in range(n)]

print(validArrangements(n, board))