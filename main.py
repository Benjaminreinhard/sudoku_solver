# Imports
# -------

import example_states
import tricks
from utils import *

# Functions
# ---------

def render(states_with_infos):
	space_between = '     '

	header = ''

	for title, _, _ in states_with_infos:
		header += title[:10*2] + ': ' + ' ' * (10*2 - len(title)) + space_between
	header
	print(header)
	print()

	for i in range(9):
		row = ''
		for _, state, _ in states_with_infos:
			for j in range(9):
				if j in [3, 6]:
					row += '| '
				if state[i][j] == 0:
					row += '. '
				else:
					row += str(state[i][j]) + ' '
			row += space_between
		
		if i in [3, 6]:
			horizontal_line = ('------+-------+-------' + space_between) * len(states_with_infos)
			print(horizontal_line)

		print(row)
	print()

	max_index = max([len(infos) for _, _, infos in states_with_infos])
	for index in range(max_index):
		footer = ''
		for _, _, infos in states_with_infos:
			info = infos[index] if index < len(infos) else ''

			footer += info[:11*2] + ' ' * (11*2 - len(info)) + space_between
		print(footer)


# Main
# ----

initial_state = example_states.state_1

state = [initial_state[i].copy() for i in range(9)]

solutions = brute_solve(state)
num_of_solutions = len(solutions)

if num_of_solutions != 1:
	print(f'Your sudoku is improper, i.e. it has {num_of_solutions} solutions instead of 1.')
	exit()

state = [initial_state[i].copy() for i in range(9)]

trick_order = [tricks.trick_1, tricks.trick_2]

outline = trick_solve(state, trick_order)

render([['Initial state', initial_state, ['Initial state', 'ddddasd']], ['Initial state', state, ['After using tricks']], ['Initial state', solutions[0], ['s']]])
print()

trick_count = {}
for trick in trick_order:
	trick_count[trick['name']] = 0

for situation in outline:
	if situation['next_trick'] == None: break
	
	trick_count[situation['next_trick']] += 1

print('Count per Trick:\n')
for name in trick_count:
	print(f'{name}: {trick_count[name]}')
print()

for situation in outline:
	counts = {}
	for name in situation['cells_with_numbers']:
		counts[name] = len(situation['cells_with_numbers'][name])

	counts['total'] = sum(counts.values())

	situation['counts'] = counts

outline.sort(key = lambda x: x['counts']['total'])

print('Bottlenecks:\n')

states_with_titles = list(map(lambda x: [outline[x]['state'], str(outline[x]['iteration'])], range(3)))




