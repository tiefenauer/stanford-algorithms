from networkx.utils import UnionFind
from tqdm import tqdm


def distances_1(bit_string):
    res = []
    for i in range(len(bit_string)):
        bits = list(bit_string)
        bits[i] = '1'
        d1_str = ''.join(bits)
        if d1_str != bit_string:
            res.append(d1_str)
        bits[i] = '0'
        d1_str = ''.join(bits)
        if d1_str != bit_string:
            res.append(d1_str)
    return res


if __name__ == '__main__':
    filename = 'clustering_big.txt'
    # filename = 'clustering_big_sample_1.txt'
    # filename = 'input_random_30_128_24.txt' # solution: 127
    # filename = 'input_random_79_65536_24.txt'  # solution: 29407
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_vertices, n_bits = map(int, lines[0].split())
        print(f'{n_vertices} vertices')
        print(f'{n_bits} bits per vertex')

        vertices = set([int(''.join(bits.split()), 2) for bits in lines[1:]])
        print(f'{len(vertices)} unique vertices')

        distances = {0}
        for d1 in distances_1("0" * 24):
            distances.add(int(d1, 2))
            for d2 in distances_1(d1):
                distances.add(int(d2, 2))

        print(f'{len(distances)} unique distances')

        uf = UnionFind(vertices)
        print('union-find created')
        for node in tqdm(vertices):

            for d in distances:
                adjacent_node = node ^ d
                if adjacent_node in uf.parents:
                    uf.union(node, adjacent_node)
        print(len(list(uf.to_sets())))
