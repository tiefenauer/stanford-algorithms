def dfs(graph, s, visited=[]):
    """
    DFS
    """
    if s not in visited:
        visited += s
    for v in [v for (u, v) in graph if u == s and v not in visited]:
        dfs(graph, v, visited)
    return visited


def topological_sort(graph, order, n, f=ord):
    visited = []
    vertices = set(u for (u, v) in graph)
    if vertices:
        order[n] = f(vertices[0])
        topological_sort([(u, v) for (u, v) in graph if u != vertex[0]], n - 1)


if __name__ == '__main__':
    graph = [('s', 'a'), ('s', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('d', 'e')]
    visited = dfs(graph, 's')
    print(visited)
    print()
    print('topological sort:')
    order = [None] * len(graph)
    toposort = topological_sort(graph, order, len(order))
