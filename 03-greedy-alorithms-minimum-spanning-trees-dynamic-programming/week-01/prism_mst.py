from heapq import heapify, heappop


class Node(object):
    def __init__(self, n):
        self.n = n
        self.edges = []

    def __lt__(self, other):
        return min(e.c for e in self.edges) < min(e.c for e in other.edges)

    def __eq__(self, other):
        return min(e.c for e in self.edges) == min(e.c for e in other.edges)


class Edge(object):
    def __init__(self, u, v, c):
        self.u = u
        self.v = v
        self.c = c

    def __lt__(self, other):
        return self.c < other.c

    def __repr__(self):
        return f'({self.u})--{self.c}--({self.v})'

    def __hash__(self):
        return hash((self.u, self.v, self.c))


if __name__ == '__main__':
    filename = 'edges.txt'
    # filename = 'sample_edges.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_vertices, n_edges = map(int, lines[0].split())

        edges = []
        for line in lines[1:]:
            v, w, c = map(int, line.split())
            edges.append(Edge(v, w, c))

        V = set([e.u for e in edges] + [e.v for e in edges])
        assert len(edges) == n_edges
        assert len(V) == n_vertices

        X = {1}
        T = set()
        mst_cost = 0
        while len(X) != len(V):
            remaining_edges = [e for e in edges if (e.u in X) ^ (e.v in X)]
            heapify(remaining_edges)
            e = heappop(remaining_edges)
            X.add(e.u)
            X.add(e.v)
            T.add(e)
            mst_cost += e.c
        print(mst_cost)
