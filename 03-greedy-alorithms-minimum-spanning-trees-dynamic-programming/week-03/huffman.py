from heapq import heappop, heappush


class Node(object):
    def __init__(self, left_node, right_node, weight=None):
        self.left_node = left_node
        self.right_node = right_node
        self.w = weight

    @property
    def weight(self):
        if self.left_node and self.right_node:
            return self.left_node.weight + self.right_node.weight
        return self.w

    def __lt__(self, other):
        return self.weight < other.weight


if __name__ == '__main__':
    filename = 'huffman.txt'
    # filename = 'huffman_sample_1.txt'
    # filename = 'huffman_sample_2.txt'
    # filename = 'huffman_sample_3.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_symbols = int(lines[0])
        weights = [int(line) for line in lines[1:]]
        nodes = [Node(None, None, weight) for weight in weights]
        while len(nodes) > 1:
            print(len(nodes))
            right_node = heappop(nodes)
            left_node = heappop(nodes)
            node = Node(left_node, right_node)
            heappush(nodes, node)


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
