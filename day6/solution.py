def lanternfish():
    with open('input.txt', 'r') as f:
        fish = list(map(int, f.readline().split(',')))

    for _ in range(80):
        fish = list(map(lambda x: x-1, fish))
        for i in range(len(fish)):
            if fish[i] == -1:
                fish[i] = 6
                fish.append(8)

    return len(fish)


if __name__ == '__main__':
    print(lanternfish())
