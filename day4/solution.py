import numpy as np


def bingo():
    with open('input.txt', 'r') as f:
        boards = []
        numbers = list(map(int, f.readline().strip().split(',')))
        for line in f:
            if line:
                temp = []
                for _ in range(5):
                    temp.append(list(map(int, f.readline().split())))
            boards.append(temp)
###############################################################################
    # part one
    np_boards = np.array(boards)
    queue = set(numbers[:4])

    for num in numbers[4:]:
        queue.add(num)
        for board in np_boards:
            for line in np.concatenate((board, board.transpose())):
                if set(line).issubset(queue):
                    # return sum(set(board.ravel()).difference(queue)) * num
                    pass
###############################################################################
    # part two
    np_boards = np.array(boards)
    queue = set(numbers[:4])
    skip = []

    for num in numbers[4:]:
        queue.add(num)
        for i, board in enumerate(np_boards):
            for line in np.concatenate((board, board.transpose())):
                if set(line).issubset(queue):
                    skip.append(i) if i not in skip else None
        if len(skip) == len(np_boards):
            return num * sum(set(np_boards[skip[-1]].ravel()
                                 ).difference(queue))


if __name__ == '__main__':
    print(bingo())
