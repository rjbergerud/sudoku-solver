from utils import *
import pdb

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    reduce_puzzle(values);

    # Choose one of the unfilled squares with the fewest possibilities
    #Check for squares with more than one possibility (base case for recursion)
    unresolved_keys = [k for k,v in values.items() if len(v) > 1]
    # print(unresolved_keys)
    empty_keys = [k for k,v in values.items() if len(v) == 0]
    solution = None
    if (len(unresolved_keys) > 0 and len(empty_keys) == 0):
        min_index = unresolved_keys[0] #Want to make sure this has more than one value.
        for index in unresolved_keys:

            min_index = min_index if len(values[min_index]) < len(values[index]) else index

        # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!

        candidates = list(values[min_index])
        while len(candidates) > 0 and solution == None:
            print(candidates, min_index)
            display(values)
            candidate_board = {k:v for k,v in values.items() }
            # pdb.set_trace()
            # print(candidate_board, values)
            candidate_board[min_index] = candidates.pop()

            solution = search(candidate_board)
    elif (len(empty_keys) > 0):
        solution = None
    else:
        solution = values
    return solution

grid2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
values = grid_values(grid2)
values = search(values)
display(values)
