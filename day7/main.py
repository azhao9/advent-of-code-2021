from typing import List
from numpy import sqrt

def main():
    print("part 1")
    print(part1("day7/test_input.txt"))
    print(part1('day7/input.txt'))

    print('part 2')
    print(part2('day7/test_input.txt'))
    print(part2('day7/input.txt'))

def parse(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()
    
    return [int(pos) for pos in lines[0].split(',')]

def part1(path: str):
    positions = parse(path)
    positions.sort()
    if len(positions) % 2 == 1:
        mid = positions[int(len(positions) / 2)]
        return _calculate_fuel(positions, mid)
    else:
        mid1, mid2 = positions[int(len(positions) / 2)], positions[int(len(positions) / 2) + 1]
        return min(_calculate_fuel(positions, mid1), _calculate_fuel(positions, mid2 + 1))

def _calculate_fuel(positions: List[int], target: int):
    total = 0
    for position in positions:
        total += abs(position - target)
    return total

def _calculate_fuel_2(positions: List[int], target: int):
    total = 0
    for position in positions:
        total += int(((position - target) ** 2 + abs(position - target)) / 2)
    return total

def part2(path: str):
    positions = parse(path)
    positions.sort()

    mean = int(sum(positions) / len(positions))
    median = positions[int(len(positions) / 2)]

    min_fuel = float('inf')
    min_target = -1
    for target in range(min(mean, median) - 1, max(mean, median) + 2):
        min_fuel = min(min_fuel, _calculate_fuel_2(positions, target))

    return min_fuel

if __name__ == '__main__':
    main()
