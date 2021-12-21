import os
from typing import List

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
    return [[int(v) for v in line.rstrip()] for line in lines]

DIRECTIONS = [(1, 1), (1, -1), (-1, 1), (-1, -1), (0, 1), (1, 0), (0, -1), (-1, 0)]

def part1(path: str):
    grid = parse(path)

    flashes = 0
    for i in range(100):
        _step(grid)
        flashes += _iterate(grid)
    
    return flashes


def _get_neighbors(row, col, grid):
    neighbors = []
    for dr, dc in DIRECTIONS:
        if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
            neighbors.append((row + dr, col + dc))
    return neighbors

def _iterate(grid: List[List[int]]):
    to_flash = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 9:
                to_flash.add((row, col))
    
    count = 0
    flashed = set(to_flash)
    while to_flash:
        next = set()

        for row, col in to_flash:
            count += 1
            for nr, nc in _get_neighbors(row, col, grid):
                grid[nr][nc] += 1
                if grid[nr][nc] > 9 and (nr, nc) not in flashed:
                    flashed.add((nr, nc))
                    next.add((nr, nc))

        to_flash = set(next)

    for row, col in flashed:
        grid[row][col] = 0
    
    return count

def _step(grid: List[List[int]]):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            grid[row][col] += 1

def part2(path: str):
    grid = parse(path)
    grid_size = len(grid) * len(grid[0])

    flashed = 0
    count = 0
    while flashed != grid_size:
        count += 1
        _step(grid)
        flashed = _iterate(grid)
    
    return count

if __name__ == '__main__':
    main()
