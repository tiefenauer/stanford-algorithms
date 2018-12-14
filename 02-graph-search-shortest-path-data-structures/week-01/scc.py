# https://github.com/Abdallah-Elshamy/Kosaraju-Two-Pass-Algorithm/blob/master/SCC.py


def dfs_1(g, i):
    global finishing_time
    global explored
    global t
    explored.add(i)
    for j in g[i]:
        if j not in explored:
            dfs_1(g, j)
    t += 1
    finishing_time[i] = t


def dfs_2(g, i):
    global sccs
    global explored
    global leader
    explored.add(i)
    sccs[i] = 1
    for j in g[i]:
        if j not in explored:
            dfs_2(g, j)
            sccs[leader] += 1


def read_graph(filename):
    with open(filename) as f:
        lines = f.readlines()

    g, g_rev = {}, {}
    for line in lines:
        a, b = tuple(line.split())
        a = int(a)
        b = int(b)
        if a not in g:
            g[a] = []
        if a not in g_rev:
            g_rev[a] = []
        if b not in g:
            g[b] = []
        if b not in g_rev:
            g_rev[b] = []
        g[a].append(b)
        g_rev[b].append(a)
    return g, g_rev


import resource
import sys

sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

if __name__ == '__main__':

    num_nodes = 875715
    filename = 'SCC.txt'
    # explored nodes
    explored = set()
    # finishing times
    finishing_time = {}
    # finishing time counter
    t = 0
    # SCC leader
    leader = None
    # SCC counters
    sccs = {}

    print(f'reading {num_nodes} nodes from {filename}')
    graph, graph_rev = read_graph(filename)

    # first pass
    print('DFS: 1st pass on reversed graph')
    for i in range(num_nodes - 1, 0, -1):
        if i not in explored:
            dfs_1(graph_rev, i)

    # second pass
    print('DFS: 2nd pass on original graph')
    explored.clear()
    for i in sorted(list(graph.keys()), key=lambda i: finishing_time[i], reverse=True):
        if i not in explored:
            leader = i
            dfs_2(graph, i)

    top_scc = sorted(list(sccs.values()), reverse=True)
    print(','.join(map(str, top_scc[:5])))
