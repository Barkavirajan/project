def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check the left side of the current row
        for i in range(col):
            if board[row][i] == 'Q':
                return False

        # Check upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check lower-left diagonal
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(row):
        if row == n:
            # Found a valid solution, record it
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(row + 1)
                board[row][col] = '.'

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve(0)
    return solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions, start=1):
        print(f"Solution {i}:")
        for row in solution:
            print(row)
        print()

# Input: N representing the size of the chessboard
N = 8  # Example, you can change N to any positive integer >= 4
solutions = solve_n_queens(N)
print_solutions(solutions)
