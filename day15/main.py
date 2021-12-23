import os
from typing import List
from heapq import heappop, heapify, heappush

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

    return [[int(r) for r in line.rstrip()] for line in lines]

def part1(path: str):
    grid = parse(path)
    return shortest_path(grid)
    
    
def get_neighbors(row, col, grid):
    res = []
    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
            res.append((row + dr, col + dc))
    return res

def get_full_grid(grid):
    full_grid = [[0 for col in range(5 * len(grid[0]))] for row in range(5 * len(grid))]

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for dr in range(5):
                for dc in range(5):
                    new = grid[row][col] + dr + dc
                    full_grid[row + dr * len(grid)][col + dc * len(grid[0])] = 9 if new == 9 else new % 9
    
    return full_grid

def shortest_path(grid):
    distances = {(0, 0): 0}
    unvisited = [(0, 0, 0)]
    
    while unvisited:
        d, row, col = heappop(unvisited)
        for nr, nc in get_neighbors(row, col, grid):
            alt = distances[(row, col)] + grid[nr][nc]
            if alt < distances.get((nr, nc), float('inf')):
                distances[(nr, nc)] = alt
                heappush(unvisited, (alt, nr, nc))
    
    return distances[(len(grid) - 1, len(grid[0]) - 1)]

def part2(path: str):
    grid = parse(path)
    full_grid = get_full_grid(grid)
    
    return shortest_path(full_grid)

if __name__ == '__main__':
    main()
