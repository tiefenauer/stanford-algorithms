# https://github.com/sestus/algorithms-stanford
import itertools


class UnionFind:

    def __init__(self, size):
        """
        Creates a new Union-Find data structure that holds <size> elements
        This class uses 1-based indexing, which means that we allocate 1 extra slot,
        but we have a more clear mapping
        :param size: the # of elements that we hold in our UF data structure
        """
        if size < 1:
            raise ValueError("size should be greater than one")
        self.count = size
        self.parents = [None] * size
        self.weights = [None] * size
        for x in range(size):
            self.weights[x] = 0
            self.parents[x] = x

    def __getitem__(self, item):
        """
        Finds the "leader" of the item <item>
        :param item: the item to check
        :return: the leader item that the <item> belongs to
        """

        # find path of objects leading to the root
        path = [item]
        root = self.parents[item]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def union(self, first, second):
        """
        Unions <first> with <second> item
        :param first: the first item to be connected
        :param second: the second item to be connected
        :return: None
        """
        # roots = [self[first], self[second]]
        # # Find the heaviest root according to its weight.
        # heaviest = max(roots, key=lambda r: self.weights[r])
        # for r in roots:
        #     if r != heaviest:
        #         self.weights[heaviest] += self.weights[r]
        #         self.parents[r] = heaviest
        first_parent = self[first]
        second_parent = self[second]
        if first_parent == second_parent:
            # nodes are in the same partition
            return

        self.count -= 1
        first_rank = self.weights[first_parent]
        second_rank = self.weights[second_parent]

        if first_rank > second_rank:
            self.parents[second_parent] = self.parents[first_parent]
        elif second_rank > first_rank:
            self.parents[first_parent] = self.parents[second_parent]
        else:
            self.parents[second_parent] = self.parents[first_parent]
            self.parents[first_parent] = first_parent
            self.weights[first_parent] = self.weights[first_parent] + 1


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

    uf = UnionFind(n_nodes)
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
    print(uf.count)  # 6118
