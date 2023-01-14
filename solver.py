def find_next_empty(puzzle):
    #to find squares on the puzzle that are not filled yet, 
    #parse the puzzle(a nested list) and return true or false
    #empty squares are squares that contain -1
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
                
    return None, None

def is_valid(guess, puzzle, row, col):
    #check the rows for guess
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #check the columns for guess
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #iterate over 3x3 grid to check if number has already been played
    row_start = (row//3) *3
    col_start = (col//3) *3

    for r in range(row_start, (row_start +3)):
        for c in range(col_start, (col_start +3)):
            if puzzle[r][c] == guess:
                return False
    
    return True

def solve_sudoku(puzzle):
    #find the empty rows and columns
    row, col = find_next_empty(puzzle)

    # when no squares remain sudoku has been solved
    if row == None:
        return True

    #if there is still a place to put a square then guess a valid number
    for guess in range(1,10):
        if is_valid(guess,puzzle, row, col):
            #if guess is valid then mutate the puzzle
            puzzle[row][col] = guess

            #solve recursively
            if solve_sudoku(puzzle):
                return True

        #reset puzzle and try a new number
        puzzle[row][col] = -1

    #if none of the combinations work than puzzle cannot be solved
    return False
    

if __name__ == "__main__":
    sample_problem = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]

    print(solve_sudoku(sample_problem))
    print(sample_problem)