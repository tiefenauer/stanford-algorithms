import math
import random

import numpy as np
from tqdm import tqdm


def random_contraction(vertices, edges):
    while len([v for v in vertices if v]) > 2:
        u, v = random.choice(edges)
        edges.remove((u, v))
        for w in vertices[v - 1]:
            vertices[w - 1] = [u if x == v else x for x in vertices[w - 1]]
        vertices[v - 1] = []
    return min([len(v) for v in vertices if v])


def select_edge(g):
    return g[0]


def remove_edges_with(g, u, v):
    return g


if __name__ == '__main__':
    with open('kargerMinCut.txt', 'r') as f:
        vertices = [list(int(v) for v in line.split())[1:] for line in f.readlines()]
        edges = [(u, v) for u, vertex in enumerate(vertices) for v in vertex]
        print(f'{len(vertices)} vertices')
        print(f'{len(edges)} edges')

    min_min_cut = math.inf
    n = int(np.power(200, 2) * np.log(200))
    # n = 1000
    for i in tqdm(range(n)):
        random.seed = i
        min_cut = random_contraction(vertices.copy(), edges.copy())
        if min_cut < min_min_cut:
            min_min_cut = min_cut
    print(min_min_cut)
