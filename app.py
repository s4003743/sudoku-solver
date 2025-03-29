from flask import Flask, render_template, request

app = Flask(__name__)


# example code (placeholder)
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

@app.route('/', methods=["GET", "POST"])
def hello():

    if request.method == "GET":
        # provide placeholder
        example_board = [
            [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
            [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
            [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

            [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
            [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
            [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

            [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
            [6, 7, -1,   1, -1, 5,   -1, 4, -1],
            [1, -1, 9,   -1, -1, -1,   2, -1, -1]
        ]

        return render_template("sudoku.html", grid=example_board, can_solve=True)

    else:
        # add inputs to data struct, then solve
        input_board = [
            [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
            [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
            [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

            [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
            [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
            [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

            [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
            [6, 7, -1,   1, -1, 5,   -1, 4, -1],
            [1, -1, 9,   -1, -1, -1,   2, -1, -1]
        ]
        row = 0
        col = 0
        for n in range(81):
            try:
                input_board[row][col] = int(request.form.get(str(n)))
            except ValueError:
                input_board[row][col] = -1
            col += 1
            if col == 9:
                col = 0
                row += 1

        # check valid input
        for r in range(9):
            for c in range(9):
                if not is_valid_guess(input_board[r][c], input_board, r, c) and input_board[r][c] != -1:
                    return render_template("sudoku.html", grid=input_board, can_solve=False)

        can_solve = solve_sudoku(input_board)
        return render_template("sudoku.html", grid=input_board, can_solve=can_solve)


def is_valid_guess(guess, grid, row, col):
    # check row
    for n in range(9):
        if guess == grid[row][n] and n != col:
            return False

    # check column
    for n in range(9):
        if guess == grid[n][col] and n != row:
            return False

    # check 3x3
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if grid[r][c] == guess and r != row and c != col:
                return False

    # passed all checks, therefore valid
    return True


def find_empty(grid):
    # search left to righ, top to bottom for empty
    for r in range(9):
        for c in range(9):
            if grid[r][c] == -1:
                return r, c

    # if none are found
    return None, None

def solve_sudoku(grid):

    row, col = find_empty(grid)

    # None left; puzzle solved
    if row == None or col == None:
        return True

    for guess in range(1, 10):

        # add guess if valid
        if is_valid_guess(guess, grid, row, col):
            grid[row][col] = guess

            if solve_sudoku(grid):
                return True

        # reset if no valid guess (no valid means one or more prev entries were incorrect)
        grid[row][col] = -1

    # failure to solve (initial grid was unsolvable)
    return False

