from heapq import heappop, heappush


class Node(object):
    def __init__(self, left_node=None, right_node=None, weight=None):
        self.left_node = left_node
        self.right_node = right_node
        self.weight = 0
        self.weight = weight or left_node.weight + right_node.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __repr__(self):
        return str(self.weight)


if __name__ == '__main__':
    filename = 'huffman.txt'
    # filename = 'huffman_sample_1.txt'
    # filename = 'huffman_sample_2.txt'
    # filename = 'huffman_sample_3.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_symbols = int(lines[0])
        print(f'{n_symbols} symbols')
        weights = [int(line) for line in lines[1:]]
        nodes = [Node(None, None, weight) for weight in weights]
        assert len(nodes) == n_symbols, 'something went wrong'

        while len(nodes) > 1:
            heappush(nodes, Node(heappop(nodes), heappop(nodes)))

        def get_depth(node, minmax):
            if node.left_node:
                depth_left = 1 + get_depth(node.left_node, minmax)
            else:
                depth_left = 0
            if node.right_node:
                depth_right = 1 + get_depth(node.right_node, minmax)
            else:
                depth_right = 0

            return minmax(depth_left, depth_right)


        max_depth = get_depth(nodes[0], max)
        min_depth = get_depth(nodes[0], min)
        print('min. depth', min_depth)  # 9
        print('max. depth', max_depth)  # 19
