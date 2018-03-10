import numpy as np


class Solver:

    #def __init__(self):


    def sudoku_solver(self, sudoku):
        """
        Solves a Sudoku puzzle and returns its unique solution.

        Input
            sudoku : 9x9 numpy array of integers
                Empty cells are designated by 0.

        Output
            9x9 numpy array of integers
                It contains the solution, if there is one. If there is no solution, all array entries should be -1.
        """

        board = np.copy(sudoku)

        # If zeros still on board, sudoku is not solved
        while 0 in board:

            for i in range(0, 9):
                # Sets the row
                row = board[i]
                # Sets the lower and upper row boundaries for the 3x3 grid square
                row_low = (i // 3) * 3
                row_high = row_low + 3
                for j in range(0, 9):
                    # Sets the column
                    col = board[:, j]
                    # Sets the lower and upper column boundaries for the 3x3 grid square
                    col_low = (j // 3) * 3
                    col_high = col_low + 3

                    # Sets the 3x3 grid square
                    grid = board[row_low:row_high, col_low:col_high]

                    possible_values = []
                    for x in range(1, 10):
                        if x not in row:
                            if x not in col:
                                if x not in grid:
                                    possible_values.append(x)

                    # if cell is zero and has one possible value, put that value in
                    if len(possible_values) == 1 and board[i, j] == 0:
                        board[i, j] = possible_values[0]

                    # if cell is zero and no possible values, then impossible sudoku
                    if len(possible_values) == 0 and board[i, j] == 0:
                        for x in range(9):
                            for y in range(9):
                                board[x, y] = -1
                        return board

        solved_sudoku = np.copy(board)

        return solved_sudoku
