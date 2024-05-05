def can_place(board, row, col, n):
    # Kontrola, zda je políčko na souřadnicích (row, col) použitelné
    return row >= 0 and col >= 0 and row < n and col < n and board[row][col] == '.'

def is_safe(board, row, col, n):
    # Kontrola, zda je políčko na souřadnicích (row, col) bezpečné pro umístění věže
    # Kontrola řádku a sloupce
    for i in range(n):
        if board[row][i] == 'V' or board[i][col] == 'V':
            return False
    # Kontrola diagonál
    for i in range(n):
        for j in range(n):
            if (i + j == row + col or i - j == row - col) and board[i][j] == 'V':
                return False
    return True

def place_queens(board, col, n):
    # Rekurzivní funkce pro umístění všech věží
    if col == n:
        # Pokud jsme umístili všechny věže, jedno platné řešení je nalezeno
        return 1

    count = 0
    for i in range(n):
        if can_place(board, i, col, n) and is_safe(board, i, col, n):
            # Pokud je políčko bezpečné, umístíme věž na toto políčko
            board[i][col] = 'V'
            # Rekurzivně umístíme věže na další sloupce
            count += place_queens(board, col + 1, n)
            # Vrátíme políčko zpět do původního stavu pro další kombinace
            board[i][col] = '.'
    return count

def count_valid_arrangements(n, board):
    # Inicializace šachovnice
    board = [list(row) for row in board]
    # Spustíme rekurzivní funkci pro umístění věží
    return place_queens(board, 0, n)

# Načtení vstupu
n = int(input())
board = [input() for _ in range(n)]

# Výpočet a výpis výsledku
print(count_valid_arrangements(n, board))