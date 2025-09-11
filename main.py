# Classes 
# -------

class SudokuSolver:
	def __init__(self, initial_state, next_cell = None):
		self.initial_state = initial_state
		if next_cell == None: self.next_cell = self.default_next_cell
		self.reset()

	def reset(self):
		self.state = self.initial_state
		self.solutions = []

	def render(self, state):
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
		row = self.state[i]
		col = [self.state[k][j] for k in range(9)]
		i = i - (i % 3)
		j = j - (j % 3)
		block = [self.state[i+k][j+l] for k in range(3) for l in range(3)]

		return [x for x in range(1,10) if x not in row+col+block]

	def insert(self, i, j, num):
		self.state[i][j] = num

	def undo(self, i, j):
		self.state[i][j] = 0

	def copy(self):
		return [self.state[i].copy() for i in range(9)]

	def default_next_cell(self, i, j):
		return [i, j+1] if j < 8 else [i+1, 0]

	def solve_rec(self, i, j, single_solution):
		if i == 9:
			self.solutions += [self.copy()]
			return single_solution

		i_, j_ = self.next_cell(i, j)

		if self.state[i][j] != 0:
			return self.solve_rec(i_, j_, single_solution)
		else:
			for num in self.allowed_numbers(i, j):
				self.insert(i, j, num)

				res = False
				res = self.solve_rec(i_, j_, single_solution)
				if res: return res
				
				self.undo(i, j)

			return False

	def solve(self, single_solution = False):
		self.reset()
		self.solve_rec(0, 0, single_solution)

# Examples
# --------

if __name__ == '__main__':
	state = [
		[0,0,0,0,0,0,4,0,0],
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
	solver.solve()
	print(f"Number of solutions: {len(solver.solutions)}\n")
	for sol in solver.solutions:
		solver.render(sol)

