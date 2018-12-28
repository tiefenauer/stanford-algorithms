import math
from heapq import heappush

import numpy as np
from tqdm import tqdm


def bellman_ford(edges, vertices, weights, s):
    n = len(vertices)
    # create (i,v) matrix: i=1..n-1, v=|V|
    A = np.zeros((n, n))
    # assert len(A) == n - 1, '(i,v) matrix: i should be n-1'
    # assert len(A[0]) == n, '(i,v) matrix: v should be n'

    # base case
    A[0, :] = np.inf
    A[0, s] = 0

    # compute DP matrix A
    for i in tqdm(range(1, n)):
        for v in vertices:
            # Case 2:
            incoming_vertices = set(w for (w, x) in edges if x == v)
            if incoming_vertices:
                min_s_w_v = min(A[i - 1, w] + weights[(w, v)] for w in incoming_vertices)
            else:
                min_s_w_v = math.inf

            # take minimum of case 1 and 2
            A[i][v] = min(A[i - 1, v], min_s_w_v)

        if np.array_equal(A[i, :], A[i - 1, :]):
            print('early stopping because all shortest paths are the same')
            return A[:i, :]

    if np.array_equal(A[-1, :], A[-2, :]):
        print('no negative cycle detected in additional iteration')
        return A[:-1, 1:]
    return None


def dijkstra(s, edges, weights, vertices):
    X = {s}
    V = set(v for v in vertices if v != s)
    A = {s: 0}
    next_vertex = s
    while V:
        minimum = math.inf
        for source, total_weight in A.items():
            crossing_edges = [(u, v) for (u, v) in edges if u in X and v in V]
            for (u, v) in crossing_edges:
                weight = weights[(u, v)]
                if total_weight + weight < minimum:
                    minimum = total_weight + weight
                    next_vertex = v
        V.remove(next_vertex)
        X.add(next_vertex)
        A[next_vertex] = minimum
    return A


def find_crossing_edges(gr, source, V):
    crossing_edges = []
    for (target, weight) in gr[source]:
        if target in V:
            crossing_edges.append((target, weight))
    return crossing_edges


def johnson(filename):
    print(f'processing {filename}')
    with open(filename) as f:
        lines = f.readlines()

    n_vertices, n_edges = map(int, lines[0].split())
    print(f'number of vertices: {n_vertices}')
    print(f'number of edges: {n_edges}')

    # read weights
    vertices = set()
    edges = set()
    weights = dict()
    for line in lines[1:]:
        u, v, c = map(int, line.split())
        edge = (u, v)
        edges.add(edge)
        weights[edge] = c
        vertices.add(u)
        vertices.add(v)

    vertices = list(sorted(vertices))

    assert len(vertices) == n_vertices, 'length of vertices does not match'
    assert len(weights) == n_edges, 'length of edges does not match'

    # add artificial start vertex s (id=0) with zero-edge to each vertex
    s = 0
    for vertex in vertices:
        edges.add((s, vertex))
        weights[(s, vertex)] = 0
    vertices.insert(0, s)

    A = bellman_ford(edges, vertices, weights, s)
    if A is not None:
        print('no cycle detected')
        # print(A)

        # remove artificial start vertex
        vertices.remove(s)
        edges = [(u, v) for (u, v) in edges if u != s and v != s]
        weights = dict(((u, v), c) for ((u, v), c) in weights.items() if u != s and v != s)

        # set p_i, the vertex weights
        vertex_weights = dict(zip(vertices, A[-1, :]))
        # print(vertex_weights)

        # perform re-weighting
        for u, v in weights.keys():
            weights[(u, v)] = weights[(u, v)] + vertex_weights[u] - vertex_weights[v]

        assert all(w >= 0 for w in weights.values()), 're-weighting should result in nonnegative weights'

        # run djikstra n times with different start vertex
        shortest_paths = []
        for vertex in vertices:
            A = dijkstra(vertex, edges, weights, vertices)
            shortest_path = min(A.values())
            print('shortest path:', shortest_path)
            heappush(shortest_paths, shortest_path)

    # cycle detected
    return math.inf


if __name__ == '__main__':
    # res_1 = johnson('sample_1.txt')
    # res_2 = johnson('sample_2.txt')
    res_1 = johnson('g1.txt')
    res_2 = johnson('g2.txt')
    res_3 = johnson('g3.txt')
    # print(min(res_1, res_2, res_2))
