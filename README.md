# Sudoku Solver

A Python Sudoku solver that gives you insight on the solvability with specified tricks.

## Features

* Solve any proper Sudoku using a brute-force technique.
* Visualize the solving process with colored output.
* Track how many cells were filled per trick.
* Tell you at each iteration, how many cells can be filled per trick.

## Installation

```bash
git clone 'https://github.com/Benjaminreinhard/sudoku_solver/'
cd sudoku_solver
pip install .
```

## Usage

```bash
python main.py <states_file> <state_number>
```

* `<states_file>`: Path to a file containing one or more Sudoku states.
* `<state_number>`: The state number in the file to solve (e.g., `1` for `#1`).

## License

GPL v3 License
