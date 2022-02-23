def sonar_sweep():
    # part one
    i = 0
    with open('input.txt', 'r') as f:
        prev = int(f.readline().strip())
        for line in f:
            next = int(line.strip())
            if next > prev:
                i += 1
            prev = next
    # return i
###############################################################################
    # part two

    i = 0
    with open('input.txt', 'r') as f:
        prev = int(f.readline().strip())
        curr = int(f.readline().strip())
        next = int(f.readline().strip())
        prev_sum = prev + curr + next

        for line in f:
            prev, curr = curr, next
            next = int(line.strip())
            next_sum = prev + curr + next
            i += 1 if next_sum > prev_sum else 0
            prev_sum = next_sum
    return i


if __name__ == '__main__':
    print(sonar_sweep())
