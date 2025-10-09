# Imports
# -------

from logic_utils import (
    possibility_matrix,
    only_choice_in_cell_trick,
    only_choice_in_cell_range_trick,
    reduction_by_aligned_nums_in_block,
    reduction_by_same_nums_in_cells,
)

# Constants
# ---------

INF = float('inf')

# Tricks
# ------

def make_trick(trick_func, reduction_techniques, max_iterations):
	def trick(state):
		return trick_func(possibility_matrix(state, reduction_techniques, max_iterations))

	return trick

s_c = make_trick(only_choice_in_cell_trick, [], 1)

s_s = make_trick(only_choice_in_cell_range_trick, [], 1)

i_c = make_trick(only_choice_in_cell_trick, [reduction_by_aligned_nums_in_block], 1)

i_s = make_trick(only_choice_in_cell_range_trick, [reduction_by_aligned_nums_in_block], 1)

a_c = make_trick(only_choice_in_cell_trick, [reduction_by_same_nums_in_cells], 1)

a_s = make_trick(only_choice_in_cell_range_trick, [reduction_by_same_nums_in_cells], 1)

e_c = make_trick(only_choice_in_cell_trick, [reduction_by_aligned_nums_in_block, reduction_by_same_nums_in_cells], INF)

e_s = make_trick(only_choice_in_cell_range_trick, [reduction_by_aligned_nums_in_block, reduction_by_same_nums_in_cells], INF)
