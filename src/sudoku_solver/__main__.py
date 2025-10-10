# Imports
# -------

from sys import argv

from sudoku_solver.tricks import s_c, s_s, i_c, i_s, a_c, a_s, e_c, e_s
from sudoku_solver.logic_utils import brute_solve, trick_solve
from sudoku_solver.render_utils import (
    title_print,
    render_states,
    render_counts_of_used_tricks,
    render_counts_of_available_steps,
)

# Functions
# ---------

def parse_state(file_path, state_nr):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    lines = [line for line in lines if line != '']

    lines = [line.replace(' ', '') for line in lines]

    state_index = lines.index(f"#{state_nr}")

    lines = lines[state_index+1:state_index+10]

    lines = [list(line) for line in lines]

    state = [[int(j) for j in line] for line in lines]

    return state



def main():
    if len(argv) != 3:
        print('ERROR: You must provide exactly two arguments:')
        print('       First argument is the file path of the state.')
        print('       Second argument is the state number.')
        exit()

    initial_state = parse_state(argv[1], argv[2])

    trick_order = [s_c, s_s, i_c, i_s, a_c, a_s, e_c, e_s]

    coloring_enabled = True

    num_of_entries_per_row = 20

    state = [initial_state[i].copy() for i in range(9)]

    solutions = brute_solve(state)
    num_of_solutions = len(solutions)

    if num_of_solutions != 1:
        print(
            f"Your sudoku is improper, i.e. it has {num_of_solutions} solutions instead of 1."
        )
        exit()

    state = [initial_state[i].copy() for i in range(9)]

    outline = trick_solve(state, trick_order)

    state_infos = [
        {"header": "Initial state", "state": initial_state},
        {"header": "After tricks", "state": state, "comparison_state": initial_state},
        {"header": "Solution", "state": solutions[0], "comparison_state": state},
    ]

    title_print("\n1. States\n", coloring_enabled)
    render_states(state_infos, coloring_enabled)

    title_print("2. Counts of used steps per trick:\n", coloring_enabled)
    render_counts_of_used_tricks(trick_order, outline)

    title_print("3. Counts of available steps per trick and iteration:\n", coloring_enabled)
    render_counts_of_available_steps(trick_order, outline, num_of_entries_per_row)

if __name__ == "__main__":
    main()
