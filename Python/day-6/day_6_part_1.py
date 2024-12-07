def locate_guard(grid):
    try:
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "^":
                    return int(y), int(x)
    except IndexError:
        print("Index out of range")

def main():
    with open("input") as f:
        grid = [list(line.strip()) for line in f.readlines()]

    seen_cells = []
    # Locate initial guard location
    guard_coord_y, guard_coord_x = locate_guard(grid)
    print(grid[0])
    while True:
        current_location = grid[guard_coord_y][guard_coord_x]
        seen_cells.append((guard_coord_y, guard_coord_x))
        # Check which cardinal direction guard is facing

        if current_location == "^":
            # First check bounds
            if guard_coord_y == 0:
                break
            # If there's an obstacle turn clockwise
            if grid[guard_coord_y - 1][guard_coord_x] == "#":
                grid[guard_coord_y][guard_coord_x] = ">"
            else:
                # Else go forwards
                grid[guard_coord_y][guard_coord_x] = "."
                guard_coord_y -= 1
                grid[guard_coord_y][guard_coord_x] = "^"


        if current_location == "v":
            if guard_coord_y == len(grid) - 1:
                break
            if grid[guard_coord_y + 1][guard_coord_x] == "#":
                grid[guard_coord_y][guard_coord_x] = "<"
            else:
                grid[guard_coord_y][guard_coord_x] = "."
                guard_coord_y += 1
                grid[guard_coord_y][guard_coord_x] = "v"



        if current_location == ">":
            if guard_coord_x == len(grid[0]):
                break
            if grid[guard_coord_y][guard_coord_x + 1] == "#":
                grid[guard_coord_y][guard_coord_x] = "v"
            else:
                grid[guard_coord_y][guard_coord_x] = "."
                guard_coord_x += 1
                grid[guard_coord_y][guard_coord_x] = ">"

        if current_location == "<":
            if guard_coord_x == 0:
                break
            if grid[guard_coord_y][guard_coord_x - 1] == "#":
                grid[guard_coord_y][guard_coord_x ] = "^"
            else:
                grid[guard_coord_y][guard_coord_x] = "."
                guard_coord_x -= 1
                grid[guard_coord_y][guard_coord_x] = "<"
        print("Updated grid:")
        for row in grid:
            print("".join(row))
        print()
    # Remove Duplicates
    seen_cells = set(seen_cells)
    print(sum(1 for cell in seen_cells))
if __name__ == "__main__":
    main()