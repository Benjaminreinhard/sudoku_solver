class Sudoku:
	def __init__(self, state):
		self.state = state

	def render(self):
		for i in range(9):
			row = ''
			for j in range(9):
				if j in [3, 6]:
					row += '| '
				if self.state [i][j] == 0:
					row += '. '
				else:
					row += str(self.state[i][j]) + ' '
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

		return [x for x in range(9) if x not in row+col+block]

	def solve_rec(self, i, j):
		if i == 8 and j == 8:
			return

		if self.state[i][j] != 0:
			if j < 8:
				self.solve_rec(i, j+1)
			else:
				self.solve_rec(i+1, 0)
		else:
			for x in self.allowed_numbers(i, j):
				self.state[i][j] = x
				
				if j < 8:
					self.solve_rec(i, j+1)
				else:
					self.solve_rec(i+1, 0)
				
				self.state[i][j] = 0



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

	sudoku = Sudoku(state)

	sudoku.solve_rec(0,0)
	sudoku.render()


