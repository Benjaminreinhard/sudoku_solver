# Imports
# -------

from utils import *

# Tricks
# ------

trick_1 = {
	'name': 'Counting Trick',
	'func': lambda state: only_choice_in_cell_trick(possibility_matrix(state))
}

trick_2 = {
	'name': 'Scannig Trick',
	'func': lambda state: only_choice_in_cell_range_trick(possibility_matrix(state))
}