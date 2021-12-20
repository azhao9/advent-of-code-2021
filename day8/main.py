from typing import List, Set

def main():
    print("part 1")
    print(part1("day8/test_input.txt"))
    print(part1('day8/input.txt'))

    print('part 2')
    print(part2('day8/test_input.txt'))
    print(part2('day8/input.txt'))

def parse(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()
    
    signals, codes = [], []
    for line in lines:
        signal, code = line.split(' | ')

        signals.append([set(s) for s in signal.rstrip().split(' ')])
        codes.append([set(c) for c in code.rstrip().split(' ')])
    
    return signals, codes

def part1(path: str):
    signals, codes = parse(path)
    count = 0
    for code in codes:
        for c in code:
            count += int(len(c) in [2, 3, 4, 7])

    return count

def _signal_to_numbers(signal: List[Set[str]]):
    numbers = {}
    for s in signal:
        if len(s) == 2:
            numbers[1] = s
        elif len(s) == 3:
            numbers[7] = s
        elif len(s) == 4:
            numbers[4] = s
        elif len(s) == 5:
            if (2, 3, 5) in numbers:
                numbers[(2, 3, 5)].append(s)
            else:
                numbers[(2, 3, 5)] = [s]
        elif len(s) == 6:
            if (0, 6, 9) in numbers:
                numbers[(0, 6, 9)].append(s)
            else:
                numbers[(0, 6, 9)] = [s]
        elif len(s) == 7:
            numbers[8] = s
    
    return numbers

def part2(path: str):
    signals, codes = parse(path)

    total = 0
    for n, signal in enumerate(signals):
        numbers = _signal_to_numbers(signal)

        for i, j in [(0, 1), (0, 2), (1, 2)]:
            if len(numbers[(2, 3, 5)][i].intersection(numbers[(2, 3, 5)][j])) == 3:
                (idx, ) = {0, 1, 2} - {i, j}
                numbers[(2, 5)] = [numbers[(2, 3, 5)][i], numbers[(2, 3, 5)][j]]

        numbers[3] = numbers[(2, 3, 5)][idx]

        for k in range(len(numbers[(0, 6, 9)])):
            if len(numbers[(0, 6, 9)][k].intersection(numbers[3])) == 5:
                numbers[9] = numbers[(0, 6, 9)][k]
                numbers[(0, 6)] = [numbers[(0, 6, 9)][l] for l in range(3) if l != k]
                
        for s in numbers[(2, 5)]:
            for t in numbers[(0, 6)]:
                if len(s.intersection(t)) == 5:
                    numbers[5] = s
                    numbers[6] = t
                    numbers[0] = [u for u in numbers[(0, 6)] if u != t][0]
                    numbers[2] = [v for v in numbers[(2, 5)] if v != s][0]
        
        del numbers[(0, 6, 9)]
        del numbers[(2, 3, 5)]
        del numbers[(2, 5)]
        del numbers[(0, 6)]

        code_to_number = {_code_to_str(code): number for number, code in numbers.items()}
        res = ''
        for code in codes[n]:
            res += str(code_to_number[_code_to_str(code)])
        total += int(res)
    return total

def _code_to_str(code: Set[str]):
    return  ''.join(sorted(list(code)))

if __name__ == '__main__':
    main()
