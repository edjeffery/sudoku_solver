import numpy as np
import time

class Sudoku:

    def __init__(self, board):
        self.board = board

    def constaint_propagation(self):
        #print("test")
        # If zeros still on board, sudoku is not solved
        while not self.is_constraint_propagation_complete(self.get_empty_cells()):
            #print("Iteration")
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
        #print("Is constraint propagation complete?")
        for cell in empty_cells:
            possible_values = self.get_possible_values(cell)
            #print(possible_values)
            if len(possible_values) == 1:
                #print("False")
                return False
        #print("True")
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

    def backtrack_solve(self, board):
        print("backtrack solve")
        d = self.find_min_domain() # Think might need to pass board to find_min_domain
        print(d)
        row = d[0]
        col = d[1]
        domain = d[2]
        if len(domain) == 0:
            print("False")
            return False
        else:
            for move in domain:
                print(row, col, move)
                temp_board = np.copy(board)
                print("Before:\n", temp_board)
                temp_board[row, col] = move
                print("After:\n",temp_board)
                self.constaint_propagation()
                if self.is_complete():
                    return True
                else:
                    print("Still not solved after constraint propagation")
                    #domain.remove(move)
                    self.backtrack_solve(temp_board)
                    if self.is_complete():
                        return True
                    else:
                        temp_board[row, col] = 0
            return False



# Load sudokus
sudokus = np.load("resources/data/sudokus.npy")
print("Shape of sudokus array:", sudokus.shape, "; Type of array values:", sudokus.dtype)
thousandsudokus = np.load("resources/data/sudoku-sample-1000.npy")

# Load solutions
solutions = np.load("resources/data/solutions.npy")
print("Shape of solutions array:", solutions.shape, "; Type of array values:", solutions.dtype, "\n")

impossiblesudokus = np.load("resources/data/sudoku-sample-15-unsolvable.npy")


hard_test = np.array([[0,0,0,7,0,0,0,0,0],
                      [1,0,0,0,0,0,0,0,0],
                      [0,0,0,4,3,0,2,0,0],
                      [0,0,0,0,0,0,0,0,6],
                      [0,0,0,5,0,9,0,0,0],
                      [0,0,0,0,0,0,4,1,8],
                      [0,0,0,0,8,1,0,0,0],
                      [0,0,2,0,0,0,0,5,0],
                      [0,4,0,0,0,0,3,0,0]], np.int32)



# for i in range(100):
#     #print("Solution of Sudoku:")
#     #print(solutions[i], "\n")
#     solver = Solver()
#     #print("My solution:")
#     solver.sudoku_solver(sudokus[i])

def sudoku_solver(board):

    s = Sudoku(board)
    #print(s.board)
    s.constaint_propagation()
    #print("Gone past constraint propagation")
    if s.is_complete():
        return s.board
    else:
        print("Not complete")
        s.backtrack_solve(s.board)
        if s.is_complete():
            return s.board
        else:
            return s.unsolvable_board()

#t = time.process_time()
s = sudoku_solver(hard_test)
print(s)

#for i in range(1000):
#    s = sudoku_solver(thousandsudokus[i])
#    #print(s)

#s = sudoku_solver(sudokus[0])
#print(s)

#elapsed_time = time.process_time() - t
#print(elapsed_time)