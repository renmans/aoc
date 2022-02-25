def hydrothermal_venture():
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    res = 0
    with open('input.txt', 'r') as f:
        for line in f:
            point1, point2 = line.split('->')
            x1, y1 = list(map(int, point1.strip().split(',')))
            x2, y2 = list(map(int, point2.strip().split(',')))
            if x1 == x2:
                for i in range(min(y1, y2), max(y1, y2)+1):
                    grid[x1][i] += 1
            elif y1 == y2:
                for i in range(min(x1, x2), max(x1, x2)+1):
                    grid[i][y1] += 1
            elif (x1 < x2 and y1 < y2) or (x1 > x2 and y1 > y2):
                x, y = min(x1, x2), min(y1, y2)
                for i in range(max(x1, x2) - x + 1):
                    grid[x][y] += 1
                    x += 1
                    y += 1
            else:
                x, y = min(x1, x2), max(y1, y2)
                for i in range(max(x1, x2) - x + 1):
                    grid[x][y] += 1
                    x += 1
                    y -= 1

    for i in range(1000):
        for j in range(1000):
            res += 1 if grid[i][j] > 1 else 0
    return res


if __name__ == '__main__':
    print(hydrothermal_venture())
