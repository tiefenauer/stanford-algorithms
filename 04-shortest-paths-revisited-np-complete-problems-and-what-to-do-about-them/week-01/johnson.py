import math
from collections import defaultdict
from heapq import heappop, heappush

import numpy as np
from tqdm import tqdm


def bellman_ford(graph, graph_inverted):
    """
    Implementation of the Bellman-Ford algorithm to find the single-source shortest path for a graph possibly containing
    negative edges.
    """
    print('creating modified graph by adding artificial start vertex s (id=0) with zero-edge to each vertex')
    s = 0
    graph_ = defaultdict(set, graph)
    graph_inverted_ = defaultdict(set, graph_inverted)
    for vertex in graph.keys():
        graph_[s].add(vertex)
        graph_inverted_[vertex].add((0, s))

    n = len(graph_)
    A = np.full(n, np.inf)
    A[s] = 0

    # we don't need to compute the full DP matrix, only the last 2 columns
    for i in tqdm(range(1, n + 1)):
        A_next = np.full(n, np.inf)
        for v in graph.keys():
            case_1 = A[v]

            if v in graph_inverted:
                # v has incoming edges from vertices w: compute path to v with at most i-1 edges from all ws
                case_2 = min(A[w] + c for (c, w) in graph_inverted[v])
            else:
                case_2 = math.inf

            A_next[v] = min(case_1, case_2)

        if i == n and not np.array_equal(A, A_next):
            print('negative cycle detected in additional iteration')
            return None

        A = A_next

    print('no cycle detected')
    # delete first column used for artificial start vertex
    return A[1:]


def dijkstra(graph, s, t):
    """
    Heap-based implementation of Dijkstra's algoritm for SSSP for a given source vertex s and target vertex t
    :param graph: graph as dictionary mapping the edges for each vertex as follows:
                    source_vertex -> {(cost, target_vertex}
    :param s: start vertex
    :param t: target vertex
    :return: the cost and path of the minimal path from s to t if there is one, else infinity
    """
    q, seen, mins = [(0, s, ())], set(), {s: 0}
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            if v1 == t:
                return cost, path

            for c, v2 in graph.get(v1, ()):
                if v2 in seen:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path))

    return float("inf")


def johnson(filename):
    print(f'processing {filename}')
    with open(filename) as f:
        lines = f.readlines()

    n_vertices, n_edges = map(int, lines[0].split())
    print(f'number of vertices: {n_vertices}')
    print(f'number of edges: {n_edges}')

    # create graph as dict: source -> (cost, target)
    graph = defaultdict(set)
    graph_inverted = defaultdict(set)  # precompute these for performance speedup
    for line in lines[1:]:
        u, v, c = map(int, line.split())
        graph[u].add((c, v))
        graph_inverted[v].add((c, u))

    assert len(graph.keys()) == n_vertices, 'length of vertices does not match'
    assert len(list(edge for edges in graph.values() for edge in edges)) == n_edges, 'length of edges does not match'

    print('running Bellman-Ford once to get single-source shortest path for a graph with possibly negative edges')
    A = bellman_ford(graph, graph_inverted)
    if A is None:
        # negative cost cycle detected
        return math.inf

    print('using shortest path from artificial start vertex as vertex weights')
    return min(A)

    # Below code would runs Dijkstra's algorithm for each combination of s-t pairs as part of Johnson's algorithm.
    # However, this is not necessary, because the BF algorithm will find the shortest path in a modified graph G' by
    # adding an artificial start node s with direct edges of length zero to all nodes in the original graph G. The
    # shortest path in G' will therefore be equal to the shortest path in G. Because s is directly connected to every
    # vertex with zero-length, the upper bound for any path is zero. Negative shortest paths will not be
    # affected by the artificial start node. Therefore it is enough to only return the shortest path from the DP-matrix
    # calculated by BF

    # vertex_weights = dict(zip(graph.keys(), A))
    #
    # print('re-weighting edges using vertex weights: C_e = C_e + p_u, - p_v')
    # for u, edges in graph.items():
    #     graph[u] = set((c + vertex_weights[u] - vertex_weights[v], v) for (c, v) in edges)
    #
    # assert all(
    #     c >= 0 for edges in graph.values() for (c, v) in edges), 're-weighting should result in nonnegative weights'
    #
    # print('running Dijkstra\'s SSSP algorithm on all combinations of s-t pairs')
    # from itertools import combinations
    # min_cost = math.inf
    # for s, t in tqdm(combinations(graph.keys(), 2), total=999000):
    #     cost, path = dijkstra(graph, s, t)
    #     original_cost = cost - vertex_weights[s] + vertex_weights[t]
    #     if original_cost < min_cost:
    #         min_cost = original_cost
    # return min_cost


if __name__ == '__main__':
    # test cases from:
    # https://www.coursera.org/learn/algorithms-npcomplete/discussions/weeks/1/threads/pt2lOePoEeaOJwr5wT2zdA
    # res_1 = johnson('sample_1.txt')  # -2
    # print('shortest path:', res_1)
    # res_2 = johnson('sample_2.txt')  # negative cycle
    # print('shortest path:', res_2)

    # res_1 = johnson('g1.txt')  # contains a negative cycle
    # print('shortest path 1:', res_1)
    # res_2 = johnson('g2.txt')  # contains a negative cycle
    # print('shortest path 2:', res_2)
    # res_3 = johnson('g3.txt')  # shortest path: -19
    # print('shortest path 3:', res_3)
    # print('shortest shortest path:', min(res_1, res_2, res_3))
