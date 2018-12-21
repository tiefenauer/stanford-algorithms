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
        self._size = size
        self._uf = [None] * (self._size + 1)
        for num in range(1, self._size + 1):
            self._uf[num] = (num, 0)

    def __getitem__(self, item):
        """
        Finds the "leader" of the item <item>
        :param item: the item to check
        :return: the leader item that the <item> belongs to
        """
        if not 1 <= item <= self._size:
            raise ValueError("Item should be in the range [1..{}".format(self._size))
        parent = self.get_parent(item)
        prev = item
        while self._uf[parent][0] != parent:
            self._uf[prev] = self._uf[parent][0], self._uf[prev][1]
            prev = parent
            parent = self.get_parent(parent)
        return parent

    def union(self, first, second):
        """
        Unions <first> with <second> item
        :param first: the first item to be connected
        :param second: the second item to be connected
        :return: None
        """
        if not (1, 1) <= (first, second) <= (self._size, self._size):
            raise ValueError("Items {}, {} should be in the range [1..{}]".format(first, second, self._size))
        first_parent = self[first]
        second_parent = self[second]
        if first_parent == second_parent:
            # nodes are in the same partition
            return

        self.count -= 1
        first_rank = self._uf[first_parent][1]
        second_rank = self._uf[second_parent][1]

        if first_rank > second_rank:
            self._uf[second_parent] = self._uf[first_parent][0], self._uf[second_parent][1]
        elif second_rank > first_rank:
            self._uf[first_parent] = self._uf[second_parent][0], self._uf[first_parent][1]
        else:
            self._uf[second_parent] = self._uf[first_parent]
            self._uf[first_parent] = (first_parent, self._uf[first_parent][1] + 1)

    def get_parent(self, item):
        node, node_range = self._uf[item]
        return node


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
    for node, line in enumerate(lines[1:], 1):
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
