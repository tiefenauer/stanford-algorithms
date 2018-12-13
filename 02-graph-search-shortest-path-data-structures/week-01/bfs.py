def bfs(graph, s):
    explored = []
    q = [s]
    while q:
        u = q.pop(0)
        for (v, w) in [(v, w) for (v, w) in graph if v == u and w not in explored]:
            explored.append(w)
            q.append(w)

    print(explored)


if __name__ == '__main__':
    graph = [('s', 'a'), ('s', 'b'), ('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e'), ('d', 'e')]
    bfs(graph, s='s')
