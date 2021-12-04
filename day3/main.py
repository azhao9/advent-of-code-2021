from numpy import loadtxt
from typing import List, Tuple, Callable

def main():
    print('part 1')
    print(part1('day3/test_input.txt'))
    print(part1('day3/input.txt'))

    print('part 2')
    print(part2('day3/test_input.txt'))
    print(part2('day3/input.txt'))

def most_common(numbers: List[str], position: int) -> int:
    count = 0
    for number in numbers:
        count += int(number[position])

    return int(count >= len(numbers) / 2)

def least_common(numbers: List[str], position: int) -> int:
    return 1 - most_common(numbers, position)

def filter_numbers(numbers: List[str], position: int, func: Callable):
    if len(numbers) == 1:
        return numbers

    result = []
    value_to_compare = func(numbers, position)
    for number in numbers:
        if int(number[position]) == value_to_compare:
            result.append(number)
    return filter_numbers(result, position + 1, func)

def part1(path: str):
    lines = loadtxt(path, dtype=str)
    
    most_common_arr = [most_common(lines, position) for position in range(len(lines[0]))]
    least_common_arr = [least_common(lines, position) for position in range(len(lines[0]))]
    gamma = int(''.join(str(bit) for bit in most_common_arr), 2)
    epsilon = int(''.join(str(bit) for bit in least_common_arr), 2)
    return gamma * epsilon

def part2(path: str):
    lines = loadtxt(path, dtype=str)

    o2 = filter_numbers(lines, 0, most_common)
    co2 = filter_numbers(lines, 0, least_common)
    
    return int(o2[0], 2) * int(co2[0], 2)

if __name__ == '__main__':
    main()