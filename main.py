# Classes 
# -------

class SudokuSolver:
	def __init__(self, initial_state):
		self.initial_state = initial_state
		self.reset()

	def reset(self):
		self.state = self.initial_state
		self.solutions = []

	def render(self, state = None):
		if state == None:
			state = self.state

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

	def allowed_numbers(self, i, j):
		if self.state[i][j] != 0: return []

		row = self.state[i]
		col = [self.state[k][j] for k in range(9)]
		i = i - (i % 3)
		j = j - (j % 3)
		block = [self.state[i+k][j+l] for k in range(3) for l in range(3)]

		return [x for x in range(1,10) if x not in row+col+block]

	def brute_solve_rec(self, i, j, single_solution):
		if i == 9:
			self.solutions += [[self.state[i].copy() for i in range(9)]]
			return single_solution

		i_, j_ = [i, j+1] if j < 8 else [i+1, 0]

		if self.state[i][j] != 0:
			return self.solve_rec(i_, j_, single_solution)
		else:
			for num in self.allowed_numbers(i, j):
				self.state[i][j] = num

				res = False
				res = self.solve_rec(i_, j_, single_solution)
				if res: return res
				
				self.state[i][j] = 0

			return False

	def brute_solve(self, single_solution = False):
		self.reset()
		self.solve_rec(0, 0, single_solution)

	def counting_trick(self):
		cells_with_numbers = []
		for i in range(9):
			for j in range(9):
				if (self.state[i][j] == 0) and (len(self.allowed_numbers(i, j)) == 1):
					num = self.allowed_numbers(i, j)[0]
					cells_with_numbers += [[i, j, num]]

		return cells_with_numbers

	def single_choice_trick_for_cell_range(self, cell_range):
		cells_with_numbers = []
		banned_numbers = []

		for i, j in cell_range:
			for num in self.allowed_numbers(i,j):
				if num not in banned_numbers:
					if num not in [num_ for i_,j_,num_ in cells_with_numbers]:
						cells_with_numbers += [[i, j, num]]
					else:
						cells_with_numbers = [[i_,j_,num_] for i_, j_, num_ in cells_with_numbers if num_ != num]
						banned_numbers += [num]

		return cells_with_numbers

	def single_choice_trick_for_rows(self):
		cells_with_numbers = []
		for cell_range in [[[i,j] for j in range(9)] for i in range(9)]:
			cells_with_numbers += self.single_choice_trick_for_cell_range(cell_range)

		return cells_with_numbers

	def single_choice_trick_for_columns(self):
		cells_with_numbers = []
		for cell_range in [[[i,j] for i in range(9)] for j in range(9)]:
			cells_with_numbers += self.single_choice_trick_for_cell_range(cell_range)

		return cells_with_numbers

	def single_choice_trick_for_blocks(self):
		cells_with_numbers = []

		for cell_range in [[[i+k,j+l] for k in range(3) for l in range(3)] for i in [0,3,6] for j in [0,3,6]]:
			cells_with_numbers += self.single_choice_trick_for_cell_range(cell_range)

		return cells_with_numbers

	def trick_solve(self, trick_order):
		self.reset()

		index = 0
		while index < len(trick_order):
			trick = trick_order[index]

			cells_with_numbers = trick()
			if cells_with_numbers == []:
				index += 1
			else:
				for i, j, num in trick():
					self.state[i][j] = num
				index = 0


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

	solver = SudokuSolver(state)
	solver.render()

	trick_order = [solver.counting_trick, solver.single_choice_trick_for_rows, solver.single_choice_trick_for_blocks]
	solver.trick_solve(trick_order)
	solver.render()

	trick_order = [solver.counting_trick, solver.single_choice_trick_for_rows, solver.single_choice_trick_for_columns]
	solver.trick_solve(trick_order)
	solver.render()

	# solver.brute_solve()
	# print(f"Number of solutions: {len(solver.solutions)}\n")
	# for sol in solver.solutions:
	# 	solver.render(sol)

