import numpy as np
from Sudoku import Sudoku
import time

# Load sudokus
sudokus = np.load("resources/data/sudokus.npy")
print("Shape of sudokus array:", sudokus.shape, "; Type of array values:", sudokus.dtype)

# Load solutions
solutions = np.load("resources/data/solutions.npy")
print("Shape of solutions array:", solutions.shape, "; Type of array values:", solutions.dtype, "\n")

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

# for i in range(100):
#     #print("Solution of Sudoku:")
#     #print(solutions[i], "\n")
#     solver = Solver()
#     #print("My solution:")
#     solver.sudoku_solver(sudokus[i])

sudoku = Sudoku()
print(sudoku.constaint_propagation(hard_test))

elapsed_time = time.process_time() - t
print(elapsed_time)

