from heapq import heapify, heappop


class UFNode(object):
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

    def __repr__(self):
        return f'{self.parent}'


class UnionFind(object):

    def __init__(self, vertices):
        self.vertices = vertices
        self.count = len(vertices)
        self.nodes = {}
        for vertex in vertices:
            self.nodes[vertex] = UFNode(vertex, 1)

    def find(self, vertex):
        """
        find leader of graph partition for given vertex
        :param vertex: vertex to use
        :return: leader vertex of the graph partition the vertex is in
        """
        if self.nodes[vertex].parent != vertex:
            self.nodes[vertex].parent = self.find(self.nodes[vertex].parent)
        return self.nodes[vertex].parent

    def union(self, v1, v2):
        """
        Merge two graph partitions
        :param v1: vertex in graph partition 1
        :param v2: vertex in graph partition 2
        """
        i = self.find(v1)
        j = self.find(v2)

        if i == j:
            return

        if self.nodes[i].rank < self.nodes[j].rank:
            self.nodes[i].parent = j
            self.nodes[j].rank += self.nodes[i].rank
        else:
            self.nodes[j].parent = i
            self.nodes[i].rank += self.nodes[j].rank
        self.count -= 1

    def is_connected(self, v1, v2):
        """
        Check if two vertices are in the same partition
        """
        return self.find(v1) == self.find(v2)

    def __repr__(self):
        clusters = {}
        for vertex in self.vertices:
            leader = self.find(vertex)
            if leader not in clusters:
                clusters[leader] = []
            clusters[leader].append(vertex)
        return str(clusters)

    def __len__(self):
        return self.count


class Edge(object):
    def __init__(self, p, q, c):
        self.p = p
        self.q = q
        self.c = c

    def __lt__(self, other):
        return self.c < other.c

    def __repr__(self):
        return f'({self.p})--{self.c}--({self.q})'


if __name__ == '__main__':
    # number of clusters
    k = 4
    print(f'{k} clusters')

    filename = 'clustering1.txt'
    # filename = 'clustering1_sample_1.txt'
    # filename = 'clustering1_sample_2.txt'
    # filename = 'clustering1_sample_3.txt'
    # filename = 'input_completeRandom_10_32.txt'
    with open(filename, 'r') as f:
        lines = f.readlines()
        n_nodes = int(lines[0])
        print(f'{n_nodes} nodes')

        # read all edges into heap
        edges = []
        vertices = set()
        for p, q, c in (line.split() for line in lines[1:]):
            p = int(p)
            q = int(q)
            c = int(c)
            edges.append(Edge(p, q, c))
            vertices.add(p)
            vertices.add(q)
        heapify(edges)
        print(f'{len(edges)} edges before merging')
        uf = UnionFind(vertices)
        print(f'{len(uf)} clusters before merging')

        max_spacing = 0
        T = set()
        while edges:
            edge = heappop(edges)
            if not uf.is_connected(edge.p, edge.q):
                # the max spacing is the weight of the edge that would lead to k-1 clusters
                if len(uf) == k:
                    max_spacing = edge.c
                    break
                v1 = uf.find(edge.p)
                v2 = uf.find(edge.q)
                uf.union(v1, v2)

        print('max distance:', max_spacing)
        print('number of clusters after merging:', len(uf))
        # print('clusters:', uf)
