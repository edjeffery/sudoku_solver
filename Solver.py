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

        for row in range(0,9):
            r = sudoku[row]
            print(r)
            count = np.count_nonzero(r == 0)
            print(count)

        for col in range(0,9):
            c = sudoku[:, col]
            print(c)
            count = np.count_nonzero(c == 0)
            print(count)

        for i in range(0,9):
            row = sudoku[row]
            for j in range(0,9):
                col = sudoku[:, j]
                

        solved_sudoku = sudoku


        return solved_sudoku
