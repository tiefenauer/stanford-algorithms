import numpy as np

if __name__ == '__main__':
    filename = 'knapsack1.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        w, n = map(int, lines[0].split())
        print(f'Knapsack size: {w}')
        print(f'number of items: {n}')
        items = []
        for line in lines[1:]:
            items.append(tuple(map(int, line.split())))

        assert len(items) == n, 'length of items does not match metadata'

        A = np.zeros((n, w))
        for i in range(1, n):
            v_i, w_i = items[i]
            for j in range(w):
                if w_i > j:
                    A[i][j] = A[i - 1, j]
                else:
                    A[i][j] = max(A[i - 1, j], A[i - 1, j - w_i] + v_i)

        print(A.max())
