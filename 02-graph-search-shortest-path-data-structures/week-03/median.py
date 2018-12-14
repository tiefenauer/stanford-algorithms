from heapq import heappush, heappop

if __name__ == '__main__':
    # filename = 'Median_simple.txt'
    filename = 'Median.txt'
    with open(filename, 'r') as f:
        a = []
        H_low, H_high = [], []
        s = 0
        for x in [int(line) for line in f.readlines()]:
            if len(H_low) == 0:
                heappush(H_low, -x)
            else:
                m = -H_low[0]
                if x > m:
                    heappush(H_high, x)
                    if len(H_high) > len(H_low):
                        heappush(H_low, -heappop(H_high))
                else:
                    heappush(H_low, -x)
                    if len(H_low) - len(H_high) > 1:
                        heappush(H_high, -heappop(H_low))
            s += -H_low[0]

        print(s % 10000)
