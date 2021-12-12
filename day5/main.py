from typing import List, Tuple

def main():
    print("part 1")
    print(part1("day5/test_input.txt"))
    print(part1('day5/input.txt'))

    print('part 2')
    print(part2('day5/test_input.txt'))
    print(part2('day5/input.txt'))

def parse(path: str):
    with open(path, 'r') as f:
        lines = f.readlines()

    vents = []
    for line in lines:
        start, arrow, end = line.split(' ')
        x1, y1 = start.split(',')
        x2, y2 = end.split(',')
        vents.append((int(x1.rstrip()), int(y1.rstrip()), int(x2.rstrip()), int(y2.rstrip())))
    
    return vents

def _get_points(x1, y1, x2, y2):
    if x1 == x2:
        return [(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)]
    elif y1 == y2:
        return [(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)]
    
    slope = int((y2 - y1) / (x2 - x1))
    if x2 > x1:
        return [(x1 + i, y1 + i * slope) for i in range(x2 - x1 + 1)]
    else:
        return [(x2 + i, y2 + i * slope) for i in range(x1 - x2 + 1)]

def _count_floor(floor: List[List[int]]) -> int:
    count = 0
    for row in floor:
        for el in row:
            count += int(el >= 2)
    return count
    
def _construct_floor(vents: List[Tuple[int, int, int, int]]) -> List[List[int]]:
    max_x, max_y = 0, 0
    for x1, y1, x2, y2 in vents:
        max_x = max(max_x, x1, x2)
        max_y = max(max_y, y1, y2)
    
    return [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]

def part1(path: str):
    vents = parse(path)
    
    floor = _construct_floor(vents)
    for x1, y1, x2, y2 in vents:
        if x1 != x2 and y1 != y2:
            continue

        for x, y in _get_points(x1, y1, x2, y2):
            floor[y][x] += 1
    
    return _count_floor(floor)



def part2(path: str):
    vents = parse(path)
    
    floor = _construct_floor(vents)
    for x1, y1, x2, y2 in vents:
        for x, y in _get_points(x1, y1, x2, y2):
            floor[y][x] += 1
    
    return _count_floor(floor)

if __name__ == '__main__':
    main()