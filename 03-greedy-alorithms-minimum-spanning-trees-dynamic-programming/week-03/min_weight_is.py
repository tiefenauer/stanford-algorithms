if __name__ == '__main__':
    filename = 'mwis.txt'
    # filename = 'huffman.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_weights = int(lines[0])
        weights = [int(line) for line in lines[1:]]
        assert n_weights == len(weights), 'something went wrong'

        A = [0] * n_weights
        A[1] = weights[0]
        for i in range(2, n_weights):
            A[i] = max(A[i - 1], A[i - 2] + weights[i - 1])

        i = len(A)
        S = set()
        while i >= 1:
            if A[i - 1] >= A[i - 2] + weights[i - 1]:
                i -= 1
            else:
                S.add(weights[i - 1])
                i -= 2

        string = ''
        for i in [1, 2, 3, 4, 17, 117, 517, 997]:
            if weights[i - 1] in S:
                string += '1'
                print(f'vertex {i} belongs to S')
            else:
                string += '0'
                print(f'vertex {i} does not belong to S')
        print(string)  # 10100110
