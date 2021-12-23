from collections import defaultdict
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

    template = ''
    rules = {}
    for i in range(len(lines)):
        if i == 0:
            template = lines[i].rstrip()
        elif i == 1:
            continue
        else:
            pair, result = lines[i].rstrip().split(' -> ')
            rules[(pair[0], pair[1])] = result
    return template, rules


def part1(path: str):
    template, rules = parse(path)

    pair_counts = defaultdict(int)
    letter_counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair_counts[(template[i], template[i+1])] += 1
        letter_counts[template[i]] += 1
    letter_counts[template[-1]] += 1
    
    ITERATIONS = 10
    for i in range(ITERATIONS):
        new_pair_counts = defaultdict(int)
        for (c1, c2), count in pair_counts.items():
            new_pair_counts[(c1, rules[(c1, c2)])] += count
            new_pair_counts[(rules[(c1, c2)], c2)] += count
            letter_counts[rules[(c1, c2)]] += count
        pair_counts = new_pair_counts
    
    sorted_count = sorted([(count, letter) for letter, count in letter_counts.items()])
    return sorted_count[-1][0] - sorted_count[0][0]

def part2(path: str):
    template, rules = parse(path)

    pair_counts = defaultdict(int)
    letter_counts = defaultdict(int)
    for i in range(len(template) - 1):
        pair_counts[(template[i], template[i+1])] += 1
        letter_counts[template[i]] += 1
    letter_counts[template[-1]] += 1
    
    ITERATIONS = 40
    for i in range(ITERATIONS):
        new_pair_counts = defaultdict(int)
        for (c1, c2), count in pair_counts.items():
            new_pair_counts[(c1, rules[(c1, c2)])] += count
            new_pair_counts[(rules[(c1, c2)], c2)] += count
            letter_counts[rules[(c1, c2)]] += count
        pair_counts = new_pair_counts
    
    sorted_count = sorted([(count, letter) for letter, count in letter_counts.items()])
    return sorted_count[-1][0] - sorted_count[0][0]
    
    
if __name__ == '__main__':
    main()
