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
    for node, line in enumerate(lines[1:]):
        bits = tuple(map(int, line.split()))
        num = int(''.join(line.split()), 2)
        if num not in numbers:
            numbers[num] = []
        numbers[num].append((node, bits))

    uf = UnionFind(range(n_nodes))
    distances = [2 ** i for i in range(n_bits)]
    distances.extend([-num for num in distances])
    for pair in itertools.combinations(distances, 2):
        bit_1, bit_2 = pair
        distances.append(bit_1 + bit_2)
    distances = [0] + distances
    for distance in distances:
        for i in numbers.keys():
            if (i + distance) in numbers:
                for node_from, bits_from in numbers[i]:
                    for node_to, bits_to in numbers[i + distance]:
                        if hamming(bits_from, bits_to) < 3:
                            uf.union(node_from, node_to)
    print(len(list(uf.to_sets())))  # 6118
