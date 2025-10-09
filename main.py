# Imports
# -------

import example_states
import tricks
from logic_utils import brute_solve, trick_solve
from render_utils import (
    title_print,
    render_states,
    render_counts_of_used_tricks,
    render_counts_of_available_steps,
)

# User inputs
# -----------

initial_state = example_states.empty_state

trick_order = [
    tricks.s_c,
    tricks.s_s,
    tricks.i_c,
    tricks.i_s,
    tricks.a_c,
    tricks.a_s,
    tricks.e_c,
    tricks.e_s,
]

coloring_enabled = True

num_of_entries_per_row = 20

# Main
# ----

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
