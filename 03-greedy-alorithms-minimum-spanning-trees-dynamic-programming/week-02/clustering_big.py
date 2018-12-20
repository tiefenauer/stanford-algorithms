from networkx.utils import UnionFind
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
    # filename = 'clustering_big.txt'
    # filename = 'clustering_big_sample_1.txt'
    # filename = 'input_random_30_128_24.txt' # solution: 127
    filename = 'input_random_79_65536_24.txt'  # solution: 29407
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_vertices, n_bits = map(int, lines[0].split())
        print(f'{n_vertices} vertices')
        print(f'{n_bits} bits per vertex')

        vertices = [int(''.join(bits.split()), 2) for bits in lines[1:]]
        print(f'{len(vertices)} unique vertices')

        i = 0
        d1s = set()
        d2s = set()
        for d1 in distances_1("0" * 24):
            d1s.add(int(d1, 2))
            for d2 in distances_1(d1):
                d2s.add(int(d2, 2))
                i += 1

        print(f'{len(d1s) + len(d2s)} unique distances ({i} distances created)')
        distances = set.union(d1s, d2s, {0})

        uf = UnionFind(vertices)
        print('union-find created')
        for node in tqdm(vertices):
            # for d1 in d1s:
            #     neighbor = node ^ d1
            #     if neighbor in vertices:
            #         uf.union(node, neighbor)
            # for d2 in d2s:
            #     neighbor = node ^ d2
            #     if neighbor in vertices:
            #         uf.union(node, neighbor)

            for d in distances:
                adjacent_node = node ^ d
                if adjacent_node in uf.parents:
                    uf.union(node, adjacent_node)
        print(len(list(uf.to_sets())))
