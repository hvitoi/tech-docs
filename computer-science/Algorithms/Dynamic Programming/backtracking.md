# Backtracking

- It's a exploratory analysis is a given choice is actually valid given the global objetive
- If the choice is not suitable, then this value is rolled back (and also the ones performed in the upper layers in the stack) and another one is tried

## Steps

1. `The Choice`
    - E.g., place 1-9 in an empty cell (sudoku)

2. `The Constraints`
    - E.g., placement can't break the board (sudoku)

3. `The Goal`
    - E.g., fill the board (sudoku)