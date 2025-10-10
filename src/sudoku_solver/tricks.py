from sudoku_solver.logic_utils import (
    possibility_matrix,
    only_choice_in_cell_trick,
    only_choice_in_cell_range_trick,
    reduction_by_aligned_nums_in_block,
    reduction_by_same_nums_in_cells,
)


def s_c(state):
    reduction_techniques = []
    max_iterations = 1
    trick_func = only_choice_in_cell_trick

    return trick_func(possibility_matrix(state, reduction_techniques, max_iterations))


def s_s(state):
    reduction_techniques = []
    max_iterations = 1
    trick_func = only_choice_in_cell_range_trick

    return trick_func(possibility_matrix(state, reduction_techniques, max_iterations))


def i_c(state):
    reduction_techniques = [reduction_by_aligned_nums_in_block]
    max_iterations = 1
    trick_func = only_choice_in_cell_trick

    return trick_func(possibility_matrix(state, reduction_techniques, max_iterations))


def i_s(state):
    reduction_techniques = [reduction_by_aligned_nums_in_block]
    max_iterations = 1
    trick_func = only_choice_in_cell_range_trick

    return trick_func(possibility_matrix(state, reduction_techniques, max_iterations))


def a_c(state):
    reduction_techniques = [reduction_by_same_nums_in_cells]
    max_iterations = 1
    trick_func = only_choice_in_cell_trick

    return trick_func(possibility_matrix(state, reduction_techniques, max_iterations))


def a_s(state):
    reduction_techniques = [reduction_by_same_nums_in_cells]
    max_iterations = 1
    trick_func = only_choice_in_cell_range_trick

    return trick_func(possibility_matrix(state, reduction_techniques, max_iterations))


def e_c(state):
    reduction_techniques = [
        reduction_by_aligned_nums_in_block,
        reduction_by_same_nums_in_cells,
    ]
    max_iterations = float("inf")
    trick_func = only_choice_in_cell_trick

    return trick_func(possibility_matrix(state, reduction_techniques, max_iterations))


def e_s(state):
    reduction_techniques = [
        reduction_by_aligned_nums_in_block,
        reduction_by_same_nums_in_cells,
    ]
    max_iterations = float("inf")
    trick_func = only_choice_in_cell_range_trick

    return trick_func(possibility_matrix(state, reduction_techniques, max_iterations))
