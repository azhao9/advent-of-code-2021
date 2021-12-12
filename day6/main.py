from typing import List, Dict
from collections import defaultdict

def main():
    print("part 1")
    print(part1("day6/test_input.txt"))
    print(part1('day6/input.txt'))

    print('part 2')
    print(part2('day6/test_input.txt'))
    print(part2('day6/input.txt'))

ITERATIONS = 80
ITERATIONS_2 = 256
NEW_AGE = 8

def parse(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()
    
    fishes = [int(fish) for fish in lines[0].split(',')]
    
    counts = {}
    for fish in fishes:
        counts[fish] = counts.get(fish, 0) + 1
    return counts 

def part1(path: str):
    counts = parse(path)

    for i in range(ITERATIONS):
        counts = _iterate(counts)
    
    return sum(counts.values())

def _iterate(counts: Dict[int, int]):
    new_counts = defaultdict(int)
    for timer, count in counts.items():
        if timer == 0:
            new_counts[NEW_AGE] += count
            new_counts[6] += count
        else:
            new_counts[timer - 1] += count
    
    return new_counts


def part2(path: str):
    counts = parse(path)

    for i in range(ITERATIONS_2):
        counts = _iterate(counts)
    
    return sum(counts.values())

if __name__ == '__main__':
    main()