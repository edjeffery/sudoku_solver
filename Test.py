import numpy as np
from Solver import Solver

# Load sudokus
sudokus = np.load("resources/data/sudokus.npy")
print("Shape of sudokus array:", sudokus.shape, "; Type of array values:", sudokus.dtype)

# Load solutions
solutions = np.load("resources/data/solutions.npy")
print("Shape of solutions array:", solutions.shape, "; Type of array values:", solutions.dtype, "\n")

# Print the first sudoku...
print("Sudoku #1:")
print(sudokus[0], "\n")

# ...and its solution
print("Solution of Sudoku #1:")
print(solutions[0], "\n")

solver = Solver()
print("My solution:")
print(solver.sudoku_solver(sudokus[0]))
