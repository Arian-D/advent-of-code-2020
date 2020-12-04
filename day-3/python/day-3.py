from typing import List, Tuple

def number_of_trees(slope: Tuple[int, int],
                    grid: List[List[bool]]) -> int:
    (dx, dy) = slope
    (x, y) = (0, 0)
    row_length = len(grid[0])
    col_length = len(grid)
    trees = 0
    while y < col_length - 1:
        y += dy
        y %= col_length
        x += dx 
        x %= row_length
        if grid[y][x]:
            trees += 1
    return trees

def main() -> None:
    grid: List[List[bool]] = []
    try:
        grid_str = open("input.txt").read().split('\n')[:-1]
        grid = [[(c == '#') for c in row] for row in grid_str]
    except FileNotFoundError:
        print("y no input.txt")
    print("Part 1 (with slope 3/1):",
          number_of_trees((3, 1), grid))
    prod = 1
    prod *= number_of_trees((1, 1), grid)
    prod *= number_of_trees((3, 1), grid)
    prod *= number_of_trees((5, 1), grid)
    prod *= number_of_trees((7, 1), grid)
    prod *= number_of_trees((1, 2), grid)
    print("Part 2 (product):",
          prod)
