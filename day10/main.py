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

ILLEGAL_SCORES = {')': 3, ']': 57, '}': 1197, '>': 25137, '': 0}
AUTO_SCORES = {')': 1, ']': 2, '}': 3, '>': 4}
PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>'}

def parse(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()
    return [line.rstrip() for line in lines]

def part1(path: str):
    lines = parse(path)

    score = 0
    for line in lines:
        score += _find_illegal(line)

    return score

def _find_illegal(line: str) -> str:
    stack = []
    for c in line:
        if c in PAIRS:
            stack.append(c)
        elif c == PAIRS[stack[-1]]:
            stack.pop()
        elif c != PAIRS[stack[-1]]:
            return ILLEGAL_SCORES[c]
    return 0

def part2(path: str):
    lines = parse(path)

    scores = []
    for line in lines:
        score = _get_closing(line)
        if score:
            scores.append(score)

    return sorted(scores)[len(scores) // 2]

def _get_closing(line: str):
    stack = []
    for c in line:
        if c in PAIRS:
            stack.append(c)
        elif c == PAIRS[stack[-1]]:
            stack.pop()
        elif c != PAIRS[stack[-1]]:
            return 0
    
    score = 0
    while stack:
        score = 5 * score + AUTO_SCORES[PAIRS[stack.pop()]]
    return score

if __name__ == '__main__':
    main()
