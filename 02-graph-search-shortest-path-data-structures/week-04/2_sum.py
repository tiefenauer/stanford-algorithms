from bisect import bisect

if __name__ == '__main__':
    filename = 'algo1-programming_prob-2sum.txt'
    with open(filename, 'r') as f:
        print('reading ints into unsorted array')
        # sort list and use set to get rid of repetitions
        xs = list(sorted(set(int(line) for line in f.readlines())))

    # use a set because we are only interested in the NUMBER of target values (not the target values themselves)
    valid_sums = set()
    for x in xs:
        # compute indices of subarray with y-values that yield valid sums in the interval [-10000..100000]
        lower = bisect(xs, -10000 - x)
        upper = bisect(xs, 10000 - x)
        # map each x and y to their sum
        for s in map(lambda y: x + y, xs[lower:upper]):
            # no need to check for x!=y because we used a set to store the integers from the file
            valid_sums.add(s)

    print(len(valid_sums))
