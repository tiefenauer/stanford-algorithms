class Node(object):

    def __init__(self, name):
        self.name = name
        self.explored = False
        self.finishing_time = None
        self.scc_leader = False

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


def scc(edges):
    # reverse the graph
    edges = reverse_edges(edges)

    # initialize global variable for finishing time
    t = 0

    unexplored = find_unexplored_nodes(edges)
    while unexplored:
        # find highest unexplored node (by node name)
        node = max(unexplored, key=lambda node: node.name)

        # perform DFS
        node_order = dfs(node, edges)

        # set finishing times depending on node order
        for node in node_order:
            t += 1
            node.finishing_time = t

        unexplored = find_unexplored_nodes(edges)

    # reverse graph again and reset explored flag
    edges = reverse_edges(edges)
    for (a, b) in edges:
        a.explored = False
        b.explored = False

    sccs = []
    unexplored = find_unexplored_nodes(edges)
    while unexplored:
        # find highest unexlored node (by finishing time)
        node = max(unexplored, key=lambda node: node.finishing_time)
        node_order = dfs(node, edges)
        node_order[-1].scc_leader = True
        sccs.append(node_order)
        unexplored = find_unexplored_nodes(edges)

    return sccs


def reverse_edges(edges):
    return [(b, a) for (a, b) in edges]


def find_unexplored_nodes(edges):
    return set([a for (a, b) in edges if not a.explored])


def dfs(node, edges, node_order=None):
    # mark node as visited
    if node_order is None:
        node_order = []
    node.explored = True

    # find unexplored neighbors (alphabetic ordering
    neighbors = [b for (a, b) in edges if a == node and not b.explored]
    for b in sorted(neighbors, key=lambda x: x.name):
        dfs(b, edges, node_order)

    node_order.append(node)
    return node_order


if __name__ == '__main__':
    filename = 'SCC.txt'
    # filename = 'sample_graph.txt'
    with open(filename, 'r') as f:
        lines = list(f.readlines())
        edges = [(a, b) for (a, b) in [tuple(line.split()) for line in lines]]
        nodes = {}
        for (a, b) in edges:
            if a not in nodes:
                nodes[a] = Node(a)
            if b not in nodes:
                nodes[b] = Node(b)
        edges = [(nodes[a], nodes[b]) for (a,b) in edges]

        sccs = scc(edges)
        sccs_by_size = sorted(sccs, key=len)
        print(','.join(str(len(scc)) for scc in sccs_by_size[:5]))
