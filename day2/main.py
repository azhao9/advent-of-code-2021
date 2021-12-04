def main():
    print('part 1')
    print(get_position('day2/test_input.txt'))
    print(get_position('day2/input.txt'))

    print('part 2')
    print(get_position2('day2/test_input.txt'))
    print(get_position2('day2/input.txt'))

def get_position(path: str):
    depth = horizontal = 0
    with open(path, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        input, value = line.split(' ')
        if input == 'forward':
            horizontal += int(value)
        elif input == 'down':
            depth += int(value)
        elif input == 'up':
            depth -= int(value)
        
    return depth * horizontal

def get_position2(path: str):
    depth = horizontal = aim = 0
    with open(path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        input, value = line.split(' ')
        if input == 'forward':
            horizontal += int(value)
            depth += aim * int(value)
        elif input == 'down':
            aim += int(value)
        elif input == 'up':
            aim -= int(value)
    
    return depth * horizontal

if __name__ == "__main__":
    main()