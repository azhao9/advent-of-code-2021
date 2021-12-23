import os
from typing import List
from collections import defaultdict

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
    return [line.rstrip() for line in lines]

def _construct_graph(lines: List[str]):
    graph = defaultdict(list)

    for line in lines:
        v1, v2 = line.split('-')
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return graph

def part1(path: str):
    graph = _construct_graph(parse(path))
    visited = set()
    path_count = [0]
    count_paths('start', 'end', visited, graph, path_count)
    return path_count[0]

def count_paths(start, end, visited, graph, path_count):
    if start == start.lower():
        visited.add(start)

    if start == end:
        path_count[0] += 1
    else:
        for neighbor in graph[start]:
            if neighbor not in visited:
                count_paths(neighbor, end, visited, graph, path_count)

    if start == start.lower():
        visited.remove(start)

def count_paths2(start, end, visited_count, twice_visited, graph, path_count):
    if start == start.lower():
        visited_count[start] += 1

    if start == end:
        path_count[0] += 1
    else:
        for neighbor in graph[start]:
            if not visited_count[neighbor]:
                count_paths2(neighbor, end, visited_count, twice_visited, graph, path_count)
            elif not twice_visited[0] and neighbor not in ('start', 'end'):
                twice_visited[0] = neighbor
                count_paths2(neighbor, end, visited_count, twice_visited, graph, path_count)

    if start == start.lower():
        visited_count[start] -= 1
        if visited_count[start] == 1:
            twice_visited[0] = ''
            

def part2(path: str):
    graph = _construct_graph(parse(path))
    visited = defaultdict(int)
    path_count = [0]
    count_paths2('start', 'end', visited, [''], graph, path_count)
    return path_count[0]

if __name__ == '__main__':
    main()
