import numpy as np
from Solver import Solver
import time

# Load sudokus
sudokus = np.load("resources/data/sudokus.npy")
print("Shape of sudokus array:", sudokus.shape, "; Type of array values:", sudokus.dtype)

# Load solutions
solutions = np.load("resources/data/solutions.npy")
print("Shape of solutions array:", solutions.shape, "; Type of array values:", solutions.dtype, "\n")

t = time.process_time()

for i in range(100):
    #print("Solution of Sudoku:")
    #print(solutions[i], "\n")
    solver = Solver()
    #print("My solution:")
    solver.sudoku_solver(sudokus[i])

elapsed_time = time.process_time() - t
print(elapsed_time)

