from math import inf


def read_graph(filename):
    graph = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            elements = line.split()
            source = int(elements[0])
            edges = []
            for element in elements[1:]:
                target, weight = tuple(element.split(','))
                edges.append((int(target), int(weight)))
            graph[source] = edges
    return graph


def find_crossing_edges(gr, source, V):
    crossing_edges = []
    for (target, weight) in gr[source]:
        if target in V:
            crossing_edges.append((target, weight))
    return crossing_edges


def dijkstra(gr, s):
    X = set([s])
    V = set(v for v in gr.keys() if v is not s)
    A = {s: 0}

    while V:
        minimum = inf
        for source, total_weight in A.items():
            for (target, weight) in find_crossing_edges(gr, source, V):
                if total_weight + weight < minimum:
                    minimum = total_weight + weight
                    next_vertex = target
        V.remove(next_vertex)
        X.add(next_vertex)
        A[next_vertex] = minimum

    return A


if __name__ == '__main__':
    filename = 'dijkstraData.txt'
    # filename = 'sample_graph.txt'
    print(f'reading graph from {filename}')
    gr = read_graph(filename)
    print(f'created graph with {len(gr.keys())} vertices')

    print(f'starting Dijkstra')
    s = list(gr.keys())[0]
    A = dijkstra(gr, s)

    target_weights = []
    for target in list(map(int, '7,37,59,82,99,115,133,165,188,197'.split(','))):
        target_weights.append(A[target])
    print(','.join(str(weight) for weight in target_weights))

