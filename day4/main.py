from typing import List


def main():
    print("part 1")
    print(part1("day4/test_input.txt"))
    print(part1('day4/input.txt'))

    print('part 2')
    print(part2('day4/test_input.txt'))
    print(part2('day4/input.txt'))


BOARD_DIM = 5


def parse(path: str):
    with open(path, "r") as f:
        lines = f.readlines()

    boards = []

    for i in range(len(lines)):
        if i == 0:
            numbers = lines[i].split()
        elif i % (BOARD_DIM + 1) == 1:
            board = []
        else:
            board.append(lines[i].split())
            if i % (BOARD_DIM + 1) == 0:
                boards.append(board)

    return numbers[0].split(','), boards

def mark_board(board: List[List[str]], number: str) -> None:
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == number:
                board[r][c] = ""

def check_board(board: List[List[str]]) -> bool:
    return _check_rows(board) or _check_cols(board)

def _check_rows(board: List[List[str]]) -> bool:
    for row in range(BOARD_DIM):
        if all(board[row][col] == "" for col in range(BOARD_DIM)):
            return True
    return False

def _check_cols(board: List[List[str]]) -> bool:
    for col in range(BOARD_DIM):
        if all(board[row][col] == "" for row in range(BOARD_DIM)):
            return True
    return False

def score_board(board: List[List[str]]) -> int:
    total = 0
    for row in range(BOARD_DIM):
        for col in range(BOARD_DIM):
            if board[row][col] != '':
                total += int(board[row][col])
    
    return total

def part1(path: str):
    numbers, boards = parse(path)

    for number in numbers:
        for board in boards:
            mark_board(board, number)
            if check_board(board):
                return int(number) * score_board(board)

def part2(path: str):
    numbers, boards = parse(path)

    won = [False] * len(boards)

    for number in numbers:
        for i in range(len(boards)):
            if won[i]:
                continue
            mark_board(boards[i], number)
            if check_board(boards[i]):
                won[i] = True
            
            if sum(won) == len(boards):
                return int(number) * score_board(boards[i])


if __name__ == "__main__":
    main()
