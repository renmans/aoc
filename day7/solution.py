def whale():
    with open('input.txt', 'r') as f:
        positions = list(map(int, f.readline().split(',')))

    res = None
    for i in range(min(positions), max(positions)):
        _sum = 0
        for pos in positions:
            _sum += pos - i if pos > i else i - pos
        if res:
            res = _sum if _sum < res else res
        else:
            res = _sum
    return res


if __name__ == "__main__":
    print(whale())
