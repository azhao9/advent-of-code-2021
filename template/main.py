import os
from typing import List

def main():
    folder = os.path.dirname(os.path.abspath(__file__))

    print("part 1")
    # print(part1(folder + "/test_input.txt"))
    # print(part1(folder + '/input.txt'))

    print('part 2')
    # print(part2(folder + '/test_input.txt'))
    # print(part2(folder + '/input.txt'))

def parse(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()

def part1(path: str):
    pass

def part2(path: str):
    pass

if __name__ == '__main__':
    main()
