import random
from collections import Counter
from copy import deepcopy


# implementation from https://github.com/reetawwsum/Karger-Min-Cut/blob/master/karger.py
# ported to Python 3
def karger_min_cut(g):
    while len(g.keys()) > 2:
        # Selecting a random vertex
        u = random.choice(list(g.keys()))
        gu = g[u]
        # Selecting most comman vertex among the previously chosen random vertex
        v = gu.most_common(1)[0][0]
        gv = g[v]
        # Deleting second vertex from the graph
        del g[v]
        # Deleting self loop
        del gv[u]
        del gu[v]
        # Merging second vertex into first vertex
        gu.update(gv)
        for w in gv:
            gw = g[w]
            gw[u] += gw[v]
            del gw[v]
    return list(g.items())[0][1].most_common(1)[0][1]


if __name__ == '__main__':
    g = {}
    with open('kargerMinCut.txt', 'r') as f:
        for line in f.readlines():
            ints = [int(x) for x in line.split()]
            g[ints[0]] = Counter(ints[1:])

cuts = [karger_min_cut(deepcopy(g)) for _ in range(20)]
print(min(cuts))
