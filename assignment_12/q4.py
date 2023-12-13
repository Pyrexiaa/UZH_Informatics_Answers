def evolve(world, steps):
    if not isinstance(world, tuple) or not all(isinstance(row, str) for row in world):
        raise Warning("The world must be a tuple of strings.")
    
    valid_characters = {'-', '|', '#', ' '}
    if any(any(char not in valid_characters for char in row) for row in world):
        raise Warning("Invalid character in the world.")
    
    if len(world) == 0:
        raise Warning("The tuple is empty")
    
    width = len(world[0])
    if any(len(row) != width for row in world):
        raise Warning("All rows in the world must have the same length.")
    
    height = len(world)
    if height < 4 or width < 4:
        raise Warning("The world dimensions (including the frame) must be greater than 2.")
    
    if not isinstance(steps, int) or steps <= 0:
        raise Warning("The number of steps must be a positive integer.")
    
    def count_neighbors(world, x, y):
        count = 0
        # Because we want to check 3x3 surrounding the coordinate
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if world[y + i][x + j] == '#':
                    count += 1
        return count
    
    for _ in range(steps):
        new_world = list(world)
        num_populated = 0
        
        for y in range(1, height - 1):
            row = ""
            for x in range(1, width - 1):
                cell = world[y][x]
                neighbor_count = count_neighbors(world, x, y)
                
                if cell == '#':
                    if neighbor_count <= 1 or neighbor_count >= 4:
                        row += ' '
                    else:
                        row += '#'
                        num_populated += 1
                else:
                    if neighbor_count == 3:
                        row += '#'
                        num_populated += 1
                    else:
                        row += ' '

            # Get the first and last frame |
            new_world[y] = new_world[y][:1] + row + new_world[y][-1:]
        
        world = tuple(new_world)

    return world, num_populated # placeholder

field = (
    "--------------",
    "|            |",
    "|   ###      |",
    "|   #        |",
    "|    #       |",
    "|            |",
    "--------------"
)
steps = 4

result, alive_cells = evolve(field, steps)

print(f"Game of Life after {steps} moves:")
for row in result:
    print(row)
print(f"{alive_cells} are alive.")

