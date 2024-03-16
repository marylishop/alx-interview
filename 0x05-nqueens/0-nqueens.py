#!/usr/bin/python3

"""
N Queens problem solver
"""

import sys


def solve_nqueens(size, current_row):
    """ Initialize the solver with an empty solution """
    partial_solutions = [[]]
    for row in range(current_row):
        # Place queens for each row
        partial_solutions = extend_solutions(row, size, partial_solutions)
    return partial_solutions


def extend_solutions(row, size, previous_solutions):
    """ extend to other solutions """
    new_solutions = []
    for solution in previous_solutions:
        for column in range(size):
            if is_safe_placement(row, column, solution):
                # If it's safe to place the queen, add the solution
                new_solutions.append(solution + [column])
    return new_solutions


def is_safe_placement(row, column, solution):
    """ Check if it's safe to place a queen at position (row, column)
    in the solution """
    if column in solution:
        return False
    else:
        # Check for diagonal conflicts
        return all(abs(solution[r] - column) != row - r for r in range(row))


def initialize_board_size():
    """ Handle command-line arguments and initialize the
    size of the chessboard """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        board_size = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def print_solutions(solutions):
    """ Print the solutions in the specified format """
    for solution in solutions:
        formatted_solution = [[row, column] for row, column
                              in enumerate(solution)]
        print(formatted_solution) 


def nqueens_solver():
    """ Main function to solve and print N Queens problem """
    board_size = initialize_board_size()
    solutions = solve_nqueens(board_size, board_size)
    print_solutions(solutions)


if __name__ == '__main__':
    """ Import control """
    nqueens_solver()
