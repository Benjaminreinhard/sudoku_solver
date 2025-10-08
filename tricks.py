# Imports
# -------

from logic_utils import *

# Tricks
# ------

def s_c(state):
	matrix = possibility_matrix(state)
	return only_choice_in_cell_trick(matrix)

def s_s(state):
	matrix = possibility_matrix(state)
	return only_choice_in_cell_range_trick(matrix)

def i_c(state):
	matrix = possibility_matrix(state, reduction_techniques = [reduction_by_aligned_nums_in_block], max_iterations = 1)
	return only_choice_in_cell_trick(matrix)

def i_s(state):
	matrix = possibility_matrix(state, reduction_techniques = [reduction_by_aligned_nums_in_block], max_iterations = 1)
	return only_choice_in_cell_range_trick(matrix)

def a_c(state):
	matrix = possibility_matrix(state, reduction_techniques = [reduction_by_same_nums_in_cells], max_iterations = 1)
	return only_choice_in_cell_trick(matrix)

def a_s(state):
	matrix = possibility_matrix(state, reduction_techniques = [reduction_by_same_nums_in_cells], max_iterations = 1)
	return only_choice_in_cell_range_trick(matrix)

def e_c(state):
	matrix = possibility_matrix(state, reduction_techniques = [reduction_by_same_nums_in_cells, reduction_by_aligned_nums_in_block], max_iterations = float('inf'))
	return only_choice_in_cell_trick(matrix)

def e_s(state):
	matrix = possibility_matrix(state, reduction_techniques = [reduction_by_same_nums_in_cells, reduction_by_aligned_nums_in_block], max_iterations = float('inf'))
	return only_choice_in_cell_range_trick(matrix)