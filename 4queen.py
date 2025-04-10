def is_safe(board, row, col):
    """Check if placing a queen at (row, col) is safe"""
    # Check same row to the left
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Check lower left diagonal
    for i, j in zip(range(row, len(board)), range(col, -1, -1)):  # Fixed this line
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queen(N):
    """Solves the N-Queens problem and prints the first solution"""
    board = [['.'] * N for _ in range(N)]

    def solve_util(col):
        """Recursive utility function to solve N-Queens"""
        if col >= N:
            return True

        for i in range(N):
            if is_safe(board, i, col):
                board[i][col] = 'Q'
                if solve_util(col + 1):
                    return True
                board[i][col] = '.'  # Backtrack

        return False

    if not solve_util(0):
        print("Solution doesn't exist")
        return False

    # Print the solution
    for row in board:
        print(' '.join(row))
    return True


N = int(input('Enter N: '))
solve_n_queen(N)