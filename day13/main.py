import os
from typing import List, Tuple

def main():
    folder = os.path.dirname(os.path.abspath(__file__))

    print("part 1")
    print(part1(folder + "/test_input.txt"))
    print(part1(folder + '/input.txt'))

    print('part 2')
    print(part2(folder + '/test_input.txt'))
    print(part2(folder + '/input.txt'))

def parse(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()

    points = []
    folds = []
    on_points = True

    for line in lines:
        if line == '\n':
            on_points = False
        elif on_points:
            col, row = line.rstrip().split(',')
            points.append((int(row), int(col)))
        else:
            axis, value = line.rstrip().split(' ')[2].split('=')
            folds.append((axis, int(value)))
    
    return points, folds

def part1(path: str):
    points, folds = parse(path)
    grid = init_grid(points, folds)
    for axis, value in folds[:1]:
        grid = flip(grid, axis, value)

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            count += grid[row][col]
    return count

def flip(grid: List[List[bool]], axis: str, value: int) -> List[List[bool]]:
    if axis == 'y':
        new_grid = [[grid[row][col] for col in range(len(grid[0]))] for row in range(value)]
        for row in range(len(new_grid)):
            for col in range(len(new_grid[0])):
                new_grid[row][col] = new_grid[row][col] or grid[2 * value - row][col]
        return new_grid
    elif axis == 'x':
        new_grid = [[grid[row][col] for col in range(value)] for row in range(len(grid))]
        for row in range(len(new_grid)):
            for col in range(len(new_grid[0])):
                new_grid[row][col] = new_grid[row][col] or grid[row][2 * value - col]
        return new_grid

def init_grid(points, folds):
    max_row = 0
    max_col = 0
    for row, col in points:
        max_row = max(max_row, row)
        max_col = max(max_col, col)

    x, y = False, False
    for axis, value in folds:
        if axis == 'x' and not x:
            max_col = max(max_col, 2 * value)
            x = True
        elif axis == 'y' and not y:
            max_row = max(max_row, 2 * value)
            y = True

    grid = [[0 for c in range(max_col + 1)] for r in range(max_row + 1)]
    for row, col in points:
        grid[row][col] = 1
    return grid

def part2(path: str):
    points, folds = parse(path)
    grid = init_grid(points, folds)
    for axis, value in folds:
        grid = flip(grid, axis, value)
    for row in grid:
        t = ['#' if c == 1 else '.' for c in row]
        print(''.join(t))

if __name__ == '__main__':
    main()
