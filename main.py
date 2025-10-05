from example_states import *

# Constants
# ---------

ROW_CELL_RANGES = [[[i,j] for j in range(9)] for i in range(9)]
COLUMN_CELL_RANGES = [[[i,j] for i in range(9)] for j in range(9)]
BLOCK_CELL_RANGES = [[[i+k,j+l] for k in range(3) for l in range(3)] for i in [0,3,6] for j in [0,3,6]]

CELL_RANGES = ROW_CELL_RANGES+COLUMN_CELL_RANGES+BLOCK_CELL_RANGES

# Functions
# ---------

def render(state):
	for i in range(9):
		row = ''
		for j in range(9):
			if j in [3, 6]:
				row += '| '
			if state [i][j] == 0:
				row += '. '
			else:
				row += str(state[i][j]) + ' '
		if i in [3, 6]:
			print('------+-------+-------')
		print(row)
	print()

def allowed_numbers(state, i, j):
	if state[i][j] != 0: return []

	row = state[i]
	col = [state[k][j] for k in range(9)]
	i = i - (i % 3)
	j = j - (j % 3)
	block = [state[i+k][j+l] for k in range(3) for l in range(3)]

	return [x for x in range(1,10) if x not in row+col+block]

def possibility_matrix(state, level = 0):
	matrix = [[allowed_numbers(state, i, j) for j in range(9)] for i in range(9)]

	if level == 0: return matrix

	for cell_range in BLOCK_CELL_RANGES:
		for num in range(1,10):
			cells_having_num = []
			for i, j in cell_range:
				if num in matrix[i][j]:
					cells_having_num += [[i,j]]

			if cells_having_num == []: continue

			row_match, col_match = True, True
			row_index, col_index = cells_having_num[0]
			for i, j in cells_having_num[1:]:
				if i != row_index:
					row_match = False
				if j != col_index:
					col_match = False

			if row_match:
				for i, j in ROW_CELL_RANGES[row_index]:
					if [i, j] not in cells_having_num and num in matrix[i][j]:
						matrix[i][j].remove(num)

			if col_match:
				for i, j in COLUMN_CELL_RANGES[col_index]:
					if [i, j] not in cells_having_num and num in matrix[i][j]:
						matrix[i][j].remove(num)

	return matrix

def brute_solve_rec(state, solutions, i, j, single_solution):
	if i == 9:
		solutions += [[state[i].copy() for i in range(9)]]
		return single_solution

	i_, j_ = [i, j+1] if j < 8 else [i+1, 0]

	if state[i][j] != 0:
		return brute_solve_rec(state, solutions, i_, j_, single_solution)
	else:
		for num in allowed_numbers(state, i, j):
			state[i][j] = num

			res = False
			res = brute_solve_rec(state, solutions, i_, j_, single_solution)
			if res: return res
			
			state[i][j] = 0

		return False

def brute_solve(state, single_solution = False):
	solutions = []
	brute_solve_rec(state, solutions, 0, 0, single_solution)
	return solutions

def trick_solve(state, trick_order):
	index = 0
	while index < len(trick_order):
		trick = trick_order[index]

		cells_with_numbers = trick(state)
		if cells_with_numbers == []:
			index += 1
		else:
			for i, j, num in cells_with_numbers:
				state[i][j] = num
			index = 0

def counting_trick(state):
	cells_with_numbers = []
	for i in range(9):
		for j in range(9):
			if (state[i][j] == 0) and (len(allowed_numbers(state, i, j)) == 1):
				num = allowed_numbers(state, i, j)[0]
				cells_with_numbers += [[i, j, num]]

	return cells_with_numbers

def generic_single_choice_trick(possibility_matrix):
	cells_with_numbers = []

	for cell_range in CELL_RANGES:
		banned_numbers = []
		cells_with_numbers_for_cell_range = []

		for i, j in cell_range:
			for num in possibility_matrix[i][j]:
				if num not in banned_numbers:
					if num not in [num_ for i_,j_,num_ in cells_with_numbers_for_cell_range]:
						cells_with_numbers_for_cell_range += [[i, j, num]]
					else:
						cells_with_numbers_for_cell_range = [[i_,j_,num_] for i_, j_, num_ in cells_with_numbers_for_cell_range if num_ != num]
						banned_numbers += [num]

		cells_with_numbers += cells_with_numbers_for_cell_range

	return cells_with_numbers

def single_choice_trick(state):
	return generic_single_choice_trick(possibility_matrix(state))

# Examples
# --------

if __name__ == '__main__':
	# m_1 = possibility_matrix(state_1)
	# m_2 = possibility_matrix(state_1, level = 1)
	# for i in range(9):
	# 	for j in range(9):
	# 		if m_1[i][j] != m_2[i][j]:
	# 			print(i, j, m_1[i][j], m_2[i][j])
	# print()
	render(state_1)
	print()

	print(single_choice_trick(state_1))


