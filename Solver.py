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

        while 0 in board:

            for i in range(0, 9):
                row = board[i]
                for j in range(0,9):
                    #print(board[i, j])
                    col = board[:, j]
                    row_low = (i // 3) * 3
                    row_high = row_low + 3
                    col_low = (j // 3) * 3
                    col_high = col_low + 3
                    grid = board[row_low:row_high, col_low:col_high]

                    possible_values = []
                    for x in range(1, 10):
                        if x not in row:
                            if x not in col:
                                if x not in grid:
                                    possible_values.append(x)

                    if len(possible_values) == 1 and board[i, j] == 0:
                        board[i, j] = possible_values[0]

        solved_sudoku = np.copy(board)

        return solved_sudoku
