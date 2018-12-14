if __name__ == '__main__':
    # filename = 'Median_simple.txt'
    filename = 'Median.txt'
    with open(filename, 'r') as f:
        a = []
        H_low, H_high = [], []
        s = 0
        for i in [int(line) for line in f.readlines()]:
            if H_high and i > H_high[0]:
                H_high.append(i)
            else:
                H_low.append(i)

            H_low.sort()
            H_high.sort()

            if len(H_low) > len(H_high) + 1:
                H_high.append(H_low[-1])
                H_low = H_low[:-1]
            if len(H_high) > len(H_low) + 1:
                H_low.append(H_high[0])
                H_high = H_high[1:]

            assert abs(len(H_low) - len(H_high)) <= 1

            both = H_low + H_high
            if len(both) % 2 == 0:
                ix = int(len(both) / 2) - 1
            else:
                ix = int((len(both) + 1) / 2) - 1
            s += both[ix]
            # print('H_low:', H_low)
            # print('H_high:', H_high)
            # print(s)
            # print()

        print(s % 10000)
