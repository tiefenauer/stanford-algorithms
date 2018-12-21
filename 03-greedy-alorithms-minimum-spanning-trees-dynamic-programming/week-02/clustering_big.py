import itertools

from networkx.utils import UnionFind

if __name__ == "__main__":
    filename = "clustering_big.txt"
    with open(filename, "r") as f:
        lines = f.readlines()

    n_nodes, n_bits = map(int, lines[0].split())
    print(f'{n_nodes} nodes')
    print(f'{n_bits} bits per node')

    numbers = [int(''.join(line.split()), 2) for line in lines[1:]]
    nodes = {}
    for node, num in enumerate(numbers):
        if num not in nodes:
            nodes[num] = set()
        nodes[num].add(node)

    uf = UnionFind(range(n_nodes))

    distances = [1 << i for i in range(n_bits)]
    distances += [(1 << ix_1) ^ (1 << ix_2) for (ix_1, ix_2) in itertools.combinations(range(n_bits), 2)]
    distances.append(0)

    for distance in distances:
        for number in nodes.keys():
            if (number ^ distance) in nodes:
                for node_from in nodes[number]:
                    for node_to in nodes[number ^ distance]:
                        uf.union(node_from, node_to)
    print(len(list(uf.to_sets())))  # 6118
