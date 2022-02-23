def binary_diagnostic():
    # part 1
    xor = 0b111111111111  # 12 bits
    zero_bits = {i: 0 for i in range(12)}
    one_bits = {i: 0 for i in range(12)}

    with open('input.txt', 'r') as f:
        for line in f:
            for i, bit in enumerate(line.strip()):
                if bit == '0':
                    zero_bits[i] += 1
                elif bit == '1':
                    one_bits[i] += 1
                else:
                    raise ValueError("Wrong bit!")

    gamma = ''
    for i in range(12):
        gamma += '0' if zero_bits[i] > one_bits[i] else '1'
    gamma = int(gamma, 2)
    epsilon = gamma ^ xor

    # return gamma * epsilon
###############################################################################
    # part 2

    with open('input.txt', 'r') as f:
        _bytes = f.read().splitlines()

        oxygen = binary_filter(_bytes, False)
        carbon = binary_filter(_bytes, True)

        return int(oxygen, 2) * int(carbon, 2)


def binary_filter(l, alt):
    for i in range(12):
        m = n = 0
        for j in l:
            m += 1 if j[i] == '0' else 0
            n += 1 if j[i] == '1' else 0
        if not alt:
            bit = '1' if n >= m else '0'
        else:
            bit = '0' if m <= n else '1'

        if len(l) > 1:
            l = list(filter(lambda x: x[i] == bit, l))
    return l[0]


if __name__ == '__main__':
    print(binary_diagnostic())
