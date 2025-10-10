# Sudoku Solver

Sudoku solver that gives you insight on the solvability using specified tricks.

## Features

* Solve any proper Sudoku using a brute-force technique.
* Solve any proper Sudoku using specified tricks AS FAR AS POSSIBLE.
* Visualize the solving process with colored output.
* Track how many cells were filled per trick.
* Track how many cells can be filled per trick at each iteration.

## Installation

```bash
git clone 'https://github.com/Benjaminreinhard/sudoku_solver/'
cd sudoku_solver
python3 -m venv venv
source venv/bin/activate
pip install .
```

## Usage

Once installed, do:

```bash
python -m sudoku_solver <states_file> <state_number>
```

* `<states_file>`: Path to a file containing one or more Sudoku states.
* `<state_number>`: The state number in the file to solve (e.g., `1` for `#1`).

E.g. `python  -m sudoku_solver example_states.txt 3`.

## License

GPL v3 License



