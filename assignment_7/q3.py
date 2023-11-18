def move(state, direction):
    movements = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }

    def is_within_bounds(row, col):
        return 0 <= row < len(state) and 0 <= col < len(state[0])
    
    # Check characters
    allowed_characters = {' ', '#', 'o'}
    if not all(all(c in allowed_characters for c in row) for row in state):
        raise Warning("Invalid characters")
    
    # Check the dimensions
    if len(state) == 0:
        raise Warning("Invalid game dimensions")

    # Check row length
    row_length = len(state[0])
    if not all(len(row) == row_length for row in state):
        raise Warning("Different row length")

    # Check if there is exactly one player 
    count_player = sum(row.count('o') for row in state)
    if count_player != 1:
        raise Warning("It has less or more than one player")

    # Find the current position of the player
    for row_idx, row in enumerate(state):
        if 'o' in row:
            col_idx = row.index('o')
            break

    # Check for valid move
    valid_movements = []
    for dir_name, offset in movements.items():
        check_row = row_idx + offset[0]
        check_col = col_idx + offset[1]
        if is_within_bounds(check_row, check_col) and state[check_row][check_col] == ' ':
            valid_movements.append(dir_name)
    valid_movements.sort()  # Sort directions alphabetically
    if not valid_movements:
        raise Warning("No possible valid moves")

    # Calculate the new position based on the given direction
    movement = movements.get(direction)
    new_row = row_idx + movement[0]
    new_col = col_idx + movement[1]

    # Check if the new position is within bounds and an empty space
    if is_within_bounds(new_row, new_col) and state[new_row][new_col] == ' ':
        new_state = [list(row) for row in state]
        new_state[row_idx][col_idx] = ' '
        new_state[new_row][new_col] = 'o'

        # Determine valid next movement directions in the new state
        valid_movements = []
        for dir_name, offset in movements.items():
            check_row = new_row + offset[0]
            check_col = new_col + offset[1]
            if is_within_bounds(check_row, check_col) and new_state[check_row][check_col] == ' ':
                valid_movements.append(dir_name)
        valid_movements.sort()  # Sort directions alphabetically

        if not valid_movements:
            raise ValueError("No valid moves")

        return (tuple(''.join(row) for row in new_state), tuple(valid_movements))
    
    else:
        # If the move is not possible, return the original state and empty tuple
        raise Warning("Invalid move")


# The following line calls the function and prints the return
# value to the Console.
s1 = (
    "#####   ",
    "###    #",
    "#   o ##",
    "   #####"
)
s2 = move(s1, "right")

print("= New State =")
print("\n".join(s2[0]))
print(f"\nPossible Moves: {s2[1]}")