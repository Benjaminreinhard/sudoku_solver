# Constants
# ---------

ROWS = [[[i,j] for j in range(9)] for i in range(9)]
COLUMNS = [[[i,j] for i in range(9)] for j in range(9)]
BLOCKS = [[[i+k,j+l] for k in range(3) for l in range(3)] for i in [0,3,6] for j in [0,3,6]]

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

def generic_single_choice_trick(state, number_range_func):
	cells_with_numbers = []

	for cell_range in ROWS+COLUMNS+BLOCKS:
		banned_numbers = []

		for i, j in cell_range:
			for num in number_range_func(state, i,j):
				if num not in banned_numbers:
					if num not in [num_ for i_,j_,num_ in cells_with_numbers]:
						cells_with_numbers += [[i, j, num]]
					else:
						cells_with_numbers = [[i_,j_,num_] for i_, j_, num_ in cells_with_numbers if num_ != num]
						banned_numbers += [num]

	return cells_with_numbers

def single_choice_trick(state):
	return generic_single_choice_trick(state, allowed_numbers)

# Examples
# --------

if __name__ == '__main__':
	state = [
		[0,8,0,7,9,0,4,0,0],
		[6,0,1,0,4,2,0,0,0],
		[0,7,0,6,0,0,0,0,8],
		[7,0,6,0,0,0,0,2,0],
		[1,3,0,0,0,0,0,8,4],
		[0,2,0,0,0,0,6,0,9],
		[9,0,0,0,0,8,0,7,0],
		[0,0,0,2,1,0,8,0,3],
		[0,0,8,0,5,7,0,6,0]
	]

	solutions = brute_solve(state)
	print(single_choice_trick(state))


