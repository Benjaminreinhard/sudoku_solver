# Constants
# ---------

ROW_CELL_RANGES = [[[i, j] for j in range(9)] for i in range(9)]

COLUMN_CELL_RANGES = [[[i, j] for i in range(9)] for j in range(9)]

BLOCK_CELL_RANGES = [
    [[i + k, j + L] for k in range(3) for L in range(3)]
    for i in [0, 3, 6]
    for j in [0, 3, 6]
]

CELL_RANGES = ROW_CELL_RANGES + COLUMN_CELL_RANGES + BLOCK_CELL_RANGES

# Functions
# ---------

def copy_state(state):
    return [[state[i].copy() for i in range(9)]]

def allowed_numbers(state, i, j):
    if state[i][j] != 0:
        return []

    row = state[i]
    col = [state[k][j] for k in range(9)]
    i = i - (i % 3)
    j = j - (j % 3)
    block = [state[i + k][j + L] for k in range(3) for L in range(3)]

    return [x for x in range(1, 10) if x not in row + col + block]


def brute_solve_rec(state, solutions, i, j, single_solution):
    if i == 9:
        solutions += copy_state(state)
        return single_solution

    i_, j_ = [i, j + 1] if j < 8 else [i + 1, 0]

    if state[i][j] != 0:
        return brute_solve_rec(state, solutions, i_, j_, single_solution)
    else:
        for num in allowed_numbers(state, i, j):
            state[i][j] = num

            res = False
            res = brute_solve_rec(state, solutions, i_, j_, single_solution)
            if res:
                return res

            state[i][j] = 0

        return False


def brute_solve(state, single_solution=False):
    solutions = []
    brute_solve_rec(state, solutions, 0, 0, single_solution)
    return solutions


def reduction_by_aligned_nums_in_block(matrix):
    reduction_found = False
    for cell_range in BLOCK_CELL_RANGES:
        for num in range(1, 10):
            cells_having_num = [[i, j] for i, j in cell_range if num in matrix[i][j]]

            if not cells_having_num:
                continue

            row_index, col_index = cells_having_num[0]
            row_match, col_match = True, True
            for i, j in cells_having_num[1:]:
                row_match = row_match and (i == row_index)
                col_match = col_match and (j == col_index)

            if row_match:
                for i, j in [
                    c for c in ROW_CELL_RANGES[row_index] if c not in cells_having_num
                ]:
                    if num in matrix[i][j]:
                        matrix[i][j].remove(num)
                        reduction_found = True

            elif col_match:
                for i, j in [
                    c
                    for c in COLUMN_CELL_RANGES[col_index]
                    if c not in cells_having_num
                ]:
                    if num in matrix[i][j]:
                        matrix[i][j].remove(num)
                        reduction_found = True

    return matrix, reduction_found


def reduction_by_same_nums_in_cells(matrix):
    reduction_found = False
    for cell_range in CELL_RANGES:
        for num in range(1, 10):
            cells_having_num = [[i, j] for i, j in cell_range if num in matrix[i][j]]

            if not cells_having_num:
                continue

            cells_not_having_num = [c for c in cell_range if c not in cells_having_num]

            nums_in_cells_having_num = set(
                [n for i, j in cells_having_num for n in matrix[i][j]]
            )
            nums_in_cells_not_having_num = set(
                [n for i, j in cells_not_having_num for n in matrix[i][j]]
            )
            nums_only_in_cells_having_num = (
                nums_in_cells_having_num - nums_in_cells_not_having_num
            )

            if len(nums_only_in_cells_having_num) != len(cells_having_num):
                continue

            for i, j in cells_having_num:
                for n in [
                    n for n in matrix[i][j] if n not in nums_only_in_cells_having_num
                ]:
                    matrix[i][j].remove(n)
                    reduction_found = True

    return matrix, reduction_found


def possibility_matrix(state, reduction_techniques, max_iterations):
    matrix = [[allowed_numbers(state, i, j) for j in range(9)] for i in range(9)]

    reduction_found = True
    iteration = 0
    while reduction_found and iteration < max_iterations:
        reduction_found = False
        iteration += 1

        for technique in reduction_techniques:
            matrix, rf = technique(matrix)
            reduction_found = reduction_found or rf

    return matrix


def only_choice_in_cell_trick(possibility_matrix):
    cells_with_numbers = []
    for i in range(9):
        for j in range(9):
            if len(possibility_matrix[i][j]) == 1:
                num = possibility_matrix[i][j][0]
                cells_with_numbers += [[i, j, num]]

    return cells_with_numbers


def only_choice_in_cell_range_trick(possibility_matrix):
    cwns = []

    for cell_range in CELL_RANGES:
        banned_numbers = []
        cwns_for_cell_range = []

        for i, j in cell_range:
            for num in possibility_matrix[i][j]:
                if num not in banned_numbers:
                    if num not in [n for _, _, n in cwns_for_cell_range]:
                        cwns_for_cell_range += [[i, j, num]]
                    else:
                        cwns_for_cell_range = [
                            [i_, j_, n_]
                            for i_, j_, n_ in cwns_for_cell_range
                            if n_ != num
                        ]
                        banned_numbers += [num]

        cwns += cwns_for_cell_range

    cells_with_numbers = []
    for cwn in cwns:
        if cwn not in cells_with_numbers:
            cells_with_numbers += [cwn]

    return cells_with_numbers


def trick_solve(state, trick_order, without_bottlenecks=False):
    outline = []

    iteration = 0
    while True:
        situation = {
            "iteration": iteration,
            "state": [state[i].copy() for i in range(9)],
            "cells_with_numbers": {},
            "next_trick": None,
        }

        for trick in trick_order:
            name = trick.__name__
            cells_with_numbers = trick(state)

            situation["cells_with_numbers"][name] = cells_with_numbers

            if cells_with_numbers and situation["next_trick"] is None:
                situation["next_trick"] = name

            if without_bottlenecks:
                break

        if situation["next_trick"] is None:
            break

        name = situation["next_trick"]
        cells_with_numbers = situation["cells_with_numbers"][name]

        for i, j, num in cells_with_numbers:
            state[i][j] = num

        outline += [situation]
        iteration += 1

    return outline
