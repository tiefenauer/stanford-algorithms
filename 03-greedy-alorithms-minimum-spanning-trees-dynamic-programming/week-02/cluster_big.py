# https://github.com/sestus/algorithms-stanford
import itertools

from networkx.utils import UnionFind


def hamming(bits_1, bits_2):
    return sum(bit_from != bit_to for (bit_from, bit_to) in zip(bits_1, bits_2))


if __name__ == "__main__":
    filename = "clustering_big.txt"
    with open(filename, "r") as f:
        lines = f.readlines()

    n_nodes, n_bits = map(int, lines[0].split())
    print(f'{n_nodes} nodes')
    print(f'{n_bits} bits per node')

    numbers = {}
    bits = {}
    for node, line in enumerate(lines[1:]):
        num = int(''.join(line.split()), 2)
        if num not in numbers:
            numbers[num] = []
        numbers[num].append(node)
        bits[num] = tuple(map(int, line.split()))

    uf = UnionFind(range(n_nodes))
    distances = [1 << i for i in range(n_bits)]
    distances += [(1 << ix_1) ^ (1 << ix_2) for (ix_1, ix_2) in itertools.combinations(range(n_bits), 2)]
    distances.append(0)

    for distance in distances:
        for number in numbers.keys():
            if (number ^ distance) in numbers:
                for node_from in numbers[number]:
                    for node_to in numbers[number ^ distance]:
                        bits_from = bits[number]
                        bits_to = bits[number ^ distance]
                        if hamming(bits_from, bits_to) < 3:
                            uf.union(node_from, node_to)
    print(len(list(uf.to_sets())))  # 6118
