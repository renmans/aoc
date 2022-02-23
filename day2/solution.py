def dive():
    # part one
    x = 0  # horizontal
    y = 0  # vertical

    with open('input.txt', 'r') as f:
        for line in f:
            command, value = line.strip().split()
            value = int(value)
            if command == 'forward':
                x += value
            elif command == 'down':
                y += value
            elif command == 'up':
                y -= value
            else:
                raise ValueError("Wrong Command!")
    # return x*y
###############################################################################
    # part two

    forward = 0
    aim = 0
    depth = 0

    with open('input.txt', 'r') as f:
        for line in f:
            command, value = line.strip().split()
            value = int(value)
            if command == 'forward':
                forward += value
                depth += value * aim
            elif command == 'down':
                aim += value
            elif command == 'up':
                aim -= value
            else:
                raise ValueError("Wrong Command!")
    return forward * depth


if __name__ == '__main__':
    print(dive())
