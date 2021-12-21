import os
from typing import List
from collections import deque


def main():
    folder = os.path.dirname(os.path.abspath(__file__))

    print("part 1")
    print(part1(folder + "/test_input.txt"))
    print(part1(folder + "/input.txt"))

    print("part 2")
    print(part2(folder + "/test_input.txt"))
    print(part2(folder + "/input.txt"))


def parse(path: str):
    with open(path, "r") as f:
        lines = f.readlines()

    floor = [[int(h) for h in line.rstrip()] for line in lines]
    return floor


def _get_low_points(floor: List[List[int]]):
    res = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for row in range(len(floor)):
        for col in range(len(floor[0])):
            neighbors = [(row + dr, col + dc) for (dr, dc) in directions]
            if all(_get_height(r, c, floor) > floor[row][col] for (r, c) in neighbors):
                res.append((row, col))
    return res


def _get_height(row, col, floor):
    if not (0 <= row < len(floor) and 0 <= col < len(floor[0])):
        return float("inf")
    return floor[row][col]


def part1(path: str):
    floor = parse(path)

    total = 0
    for row, col in _get_low_points(floor):
        total += floor[row][col] + 1

    return total


def part2(path: str):
    floor = parse(path)

    low_points = _get_low_points(floor)

    basin_sizes = []
    visited = set()
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for low_point in low_points:
        frontier = [low_point]
        visited.add(low_point)
        basin_size = 0
        while frontier:
            next = []
            for (row, col) in frontier:
                if floor[row][col] == 9:
                    continue

                basin_size += 1

                neighbors = [
                    (row + dr, col + dc)
                    for (dr, dc) in directions
                    if _in_range(row + dr, col + dc, floor)
                    and _get_height(row + dr, col + dc, floor) > floor[row][col]
                    and (row + dr, col + dc) not in visited
                ]
                for neighbor in neighbors:
                    visited.add(neighbor)
                    next.append(neighbor)
            frontier = list(next)

        basin_sizes.append(basin_size)

    product = 1
    for bs in sorted(basin_sizes, reverse=True)[:3]:
        product *= bs
    return product


def _in_range(row, col, floor):
    return 0 <= row < len(floor) and 0 <= col < len(floor[0])


if __name__ == "__main__":
    main()
