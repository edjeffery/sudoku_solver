import numpy as np
import time

class Sudoku:

    def __init__(self, board):
        self.board = board

    def constraint_propagation(self):
        # If zeros still on board, sudoku is not solved
        while not self.is_constraint_propagation_complete(self.get_empty_cells()):
            empty_cells = self.get_empty_cells()
            for cell in empty_cells:
                possible_values = self.get_possible_values(cell)

                # If cell is zero and has one possible value, put that value in
                if len(possible_values) == 1:
                    self.board[cell[0], cell[1]] = possible_values[0]

    def is_complete(self):
        for i in range(9):
            for j in range(9):
                if self.board[i, j] == 0:
                    return False
        return True

    def is_constraint_propagation_complete(self, empty_cells):
        for cell in empty_cells:
            possible_values = self.get_possible_values(cell)

            if len(possible_values) == 1:
                return False
        return True

    def unsolvable_board(self):
        for i in range(9):
            for j in range(9):
                self.board[i, j] = -1
        return self.board

    def get_empty_cells(self):
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if self.board[i, j] == 0:
                    empty_cells.append((i, j))
        return empty_cells

    def find_min_domain(self):
        min_domain = [0] * 10
        min_domain_row = 0
        min_domain_col = 0
        for i in range(9):
            for j in range(9):
                possible_values = self.get_possible_values((i, j))
                if 0 < len(possible_values) < len(min_domain) and self.board[i, j] == 0:
                    min_domain = possible_values
                    min_domain_row = i
                    min_domain_col = j

        return min_domain_row, min_domain_col, min_domain

    def get_possible_values(self, cell):
        i = cell[0]
        j = cell[1]
        possible_values = []

        # Sets the row
        row = self.board[i]
        # Sets the lower and upper row boundaries for the 3x3 grid square
        row_low = (i // 3) * 3
        row_high = row_low + 3

        # Sets the column
        col = self.board[:, j]
        # Sets the lower and upper column boundaries for the 3x3 grid square
        col_low = (j // 3) * 3
        col_high = col_low + 3

        # Sets the 3x3 grid square
        grid = self.board[row_low:row_high, col_low:col_high]

        # If a value is not in the same row, column or grid square then it is a possible value
        for x in range(1, 10):
            if x not in row:
                if x not in col:
                    if x not in grid:
                        possible_values.append(x)

        return possible_values


def backtrack(sudoku):
    if sudoku.is_complete():
        return True
    empty_cells = sudoku.get_empty_cells()
    # Get domain lengths for each empty cell
    domain_lengths = []
    for cell in empty_cells:
        possible_values = sudoku.get_possible_values(cell)
        domain_lengths.append(len(possible_values))

    # Sort cells by increasing domain length
    sorted_empty_cells = [x for _, x in sorted(zip(domain_lengths, empty_cells))]

    # For each empty cell, try move, constraint propagate
    # and if it gets stuck, recursively call backtracking algorithm
    for cell in sorted_empty_cells:
        possible_values = sudoku.get_possible_values(cell)
        for move in possible_values:
            sudoku.board[cell[0], cell[1]] = move
            board_clone = np.copy(sudoku.board)
            sudoku.constraint_propagation()
            if sudoku.is_complete():
                return True
            else:
                sudoku.board = board_clone
            if backtrack(sudoku):
                return True
            else:
                sudoku.board[cell[0], cell[1]] = 0
        return False


def sudoku_solver(board):
    # Initialise sudoku and try to solve via constraint propagation
    # If this does not solve the sudoku, try the backtracking algorithm
    s = Sudoku(board)
    s.constraint_propagation()
    if s.is_complete():
        return s.board
    else:
        if backtrack(s):
            return s.board
        else:
            return s.unsolvable_board()



# Load sudokus
sudokus = np.load("resources/data/sudokus.npy")
thousandsudokus = np.load("resources/data/sudoku-sample-1000.npy")
impossiblesudokus = np.load("resources/data/sudoku-sample-15-unsolvable.npy")

# Load solutions
solutions = np.load("resources/data/solutions.npy")

hard_test = np.array([[0,0,0,7,0,0,0,0,0],
                      [1,0,0,0,0,0,0,0,0],
                      [0,0,0,4,3,0,2,0,0],
                      [0,0,0,0,0,0,0,0,6],
                      [0,0,0,5,0,9,0,0,0],
                      [0,0,0,0,0,0,4,1,8],
                      [0,0,0,0,8,1,0,0,0],
                      [0,0,2,0,0,0,0,5,0],
                      [0,4,0,0,0,0,3,0,0]], np.int32)


t = time.process_time()

for i in range(1000):
    s = sudoku_solver(thousandsudokus[i])
    #print(s)

#s = sudoku_solver(hard_test)
#print(s)

elapsed_time = time.process_time() - t
print(elapsed_time)