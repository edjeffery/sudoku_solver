import numpy as np
import time

class Sudoku:

    def __init__(self, board):
        self.board = board

    def constaint_propagation(self):

        #board = np.copy(sudoku)

        iteration = 1

        # If zeros still on board, sudoku is not solved
        while not self.is_constraint_propagation_complete():

            print("\nIteration ", iteration, "\n")
            #print("\nBeginning of iteration\n", board)

            prev_board = np.copy(self.board)

            min_domain = [0] * 10
            min_domain_row = 0
            min_domain_col = 0

            count = 0

            for i in range(0, 9):
                # Sets the row
                row = self.board[i]
                # Sets the lower and upper row boundaries for the 3x3 grid square
                row_low = (i // 3) * 3
                row_high = row_low + 3
                for j in range(0, 9):
                    # Sets the column
                    col = self.board[:, j]
                    # Sets the lower and upper column boundaries for the 3x3 grid square
                    col_low = (j // 3) * 3
                    col_high = col_low + 3

                    # Sets the 3x3 grid square
                    grid = self.board[row_low:row_high, col_low:col_high]

                    possible_values = []
                    # If a value is not in the same row, column or grid square then it is a possible value
                    for x in range(1, 10):
                        if x not in row:
                            if x not in col:
                                if x not in grid:
                                    possible_values.append(x)

                    if 0 < len(possible_values) < len(min_domain) and self.board[i, j] == 0:
                        min_domain = possible_values
                        min_domain_row = i
                        min_domain_col = j

                    #print(i, j, possible_values)

                    # If cell is zero and has one possible value, put that value in
                    if len(possible_values) == 1 and self.board[i, j] == 0:
                        self.board[i, j] = possible_values[0]
                        print("Change: ", i, j, self.board[i, j])

                    # If cell is zero and no possible values, then impossible sudoku
                    if len(possible_values) == 0 and self.board[i, j] == 0:
                        for x in range(9):
                            for y in range(9):
                                self.board[x, y] = -1
                        return self.board

                    if self.board[i, j] != 0:
                        count += 1
            print("Count: ", count)

            print(min_domain_row, min_domain_col, min_domain)

            # If one full iteration results in unchanged board, need to use search and backtracking to solve
            if np.array_equal(prev_board, self.board):
                print("Before sending to backtrack: \n", self.board)
                self.backtrack_solve(min_domain_row, min_domain_col, min_domain, self.board)

            iteration += 1
        #solved_sudoku = np.copy(board)

        #return self.board

    def is_complete(self):
        for i in range(9):
            for j in range(9):
                if self.board[i, j] == 0:
                    return False
        return True

    def is_constraint_propagation_complete(self):
        for i in range(9):
            for j in range(9):
                if self.get_possible_values() == 1:
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
                pass

    def get_possible_values(self):
        possible_values = []
        for i in range(9):
            for j in range(9):
                # If a value is not in the same row, column or grid square then it is a possible value
                for x in range(1, 10):
                    if x not in row:
                        if x not in col:
                            if x not in grid:
                                possible_values.append(x)


    def backtrack_solve(self, row, col, domain, board):
        print("To backtrack with: ", row, col, domain)
        temp_board = np.copy(board)
        print(temp_board)
        choice = np.random.choice(domain) # Rather than make a random choice here, could use LCV instead
        print("Choice: ", choice)
        temp_board[row, col] = choice
        print(temp_board)
        attempt_solve = self.sudoku_solver(temp_board)
        #if attempt_solve is solution:
        #    return board
        #else:
        #    domain.remove(choice)
        #    backtrack(row, col, domain, temp_board)



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

#t = time.process_time()

# for i in range(100):
#     #print("Solution of Sudoku:")
#     #print(solutions[i], "\n")
#     solver = Solver()
#     #print("My solution:")
#     solver.sudoku_solver(sudokus[i])

def sudoku_solver(board):

    s = Sudoku(board)
    s.constaint_propagation()
    if s.is_complete():
        return s
    else:
        s.backtrack_solve()
        if s.is_complete():
            return s
        else:
            return s.unsolvable_board()

sudoku_solver(hard_test)

#elapsed_time = time.process_time() - t
#print(elapsed_time)