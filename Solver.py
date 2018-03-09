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

        for row in range(0, 9):
            r = board[row]
            count = np.count_nonzero(r == 0)

        for col in range(0, 9):
            c = board[:, col]
            count = np.count_nonzero(c == 0)

        for i in range(0, 9):
            row = board[i]
            for j in range(0,9):
                print(board[i, j])
                col = board[:, j]
                row_low = (i // 3) * 3
                row_high = row_low + 3
                col_low = (j // 3) * 3
                col_high = col_low + 3
                #print(row_low, row_high, col_low, col_high)
                grid = board[row_low:row_high, col_low:col_high]
                #print("Row: ", row)
                #print("Col: ", col)
                #print(grid)

                possible_values = []
                for x in range(1,10):
                    if x not in row:
                        if x not in col:
                            if x not in grid:
                                possible_values.append(x)
                print(i, j, possible_values)

                

        solved_sudoku = sudoku #deep copy


        return solved_sudoku
