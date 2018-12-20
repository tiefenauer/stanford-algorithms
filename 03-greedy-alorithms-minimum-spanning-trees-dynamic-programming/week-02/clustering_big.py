from tqdm import tqdm




def distances_1(bit_string):
    res = []
    for i in range(len(bit_string)):
        d1 = list(bit_string)
        d1[-i - 1] = '1'
        d1 = ''.join(d1)
        if d1 != bit_string:
            res.append(d1)
    return res


if __name__ == '__main__':
    filename = 'clustering_big.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_nodes, n_bits = map(int, lines[0].split())
        print(f'{n_nodes} nodes')
        print(f'{n_bits} bits per node')

        distances = set()
        zero = "0" * 24
        distances.add(int(zero, 2))
        d1s = distances_1(zero)
        for d1 in d1s:
            distances.add(int(d1, 2))
            d2s = distances_1(d1)
            for d2 in d2s:
                distances.add(int(d2, 2))

        # nodes
        vertices = set([int(''.join(bits.split()), 2) for bits in lines[1:]])
        uf = UnionFind(vertices)
        for node in tqdm(vertices):
            for d in distances:
                adjacent_node = node ^ d
                if adjacent_node in vertices:
        print(len(clusters.values()))
