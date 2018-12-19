# Two Motivating Applications

## Application: Internet Routing
- Internet as a graph: Vertices=end hosts/routers, edges=direct links
- Web as a graph: Vertices=Web pages, edges=hyperlinks
- Social Networks: vertices=people, edges=friend/follow relationship
- The problem with such graphs is that they become too large to compute the shortest path on a single device (e.g. a router would have to know the whole internet before sending a package)
- This requires a shortest path algorithm that uses only local computation (e.g. Bellman-Ford)

## Application: Sequence Alignment
- Aligning two sequences quickly becomes infeasible using brute-force algorithms
- The Needleman-Wunsch algorithm can do it very efficiently using dynamic programming

# Introduction to Greedy Algorithms

## Introduction to Greedy Algorithms
- Definition: sequence of decisions, hope everything works out at the end.
- in contrast with divide & conquer algorithms, greedy algorithms...
    - ...are easier to propose
    - ...the running time is easier to analyze
    - ...the correctness is harder to proof and often incorrect
- Dijkstra as an example of a greedy algorithm that is incorrect for graph with negative paths

## Application: Optimal Caching
- problem with caches: in case of a cache miss, some old entry has to be evicted --> which one should that be?
- Belady stated that the optimal algorithm is the one that evicts the entries which is requested the "furthest-in-future"
- We cannot foresee the future, but the statement is still useful
    - as a guideline for practical algorithms (e.g. LRU, which evicts the oldest entry)
    - as an idealized benchmark to compare to (e.g. after we have logs of page requests)

# A Scheduling Application

## Problem Definition
- one shared resource (e.g. processor), many jobs to do (e.g. processes) --> what order of jobs should we use
- assume each job has a priority (w_j) and a length (l_j)
- an objective function defines the goal to optimize (e.g. the sum of all w_j*l_j)

## A Greedy Algorithm
- one way to evaluate the greedy algorithm is to evaluate special cases
    - if all jobs have the same weights, prefer shorter jobs --> reduces waiting time of subsequent jobs
    - if all jobs have the same length, prefer higher weighted jobs --> preserves priority
- if above special cases give conflicting advice for general cases (e.g. if w_i > w_j and l_i > l_j), we need a scoring function that is increasing in weight and decreasing in length
    - e.g. w_j - l_j --> this does not always give the best sequence, e.g. for w_1, l_1 = 3, 5 and w_2, l_2 = 1, 2
    - e.g. w_j / l_j --> this always gives the best sequence (proof in next video)
- greedy algorithms are therefore OFTEN INCORRECT

## Correctness Proof - Part 1
- proof by contradiction

## Correctness Proof - Part 2
- proof by contradiction

## Handling Ties
not viewed
 
# Prim's Minimum Spanning Tree (MST) Algorithm

## MST Problem Definition
- given an UNDIRECTED graph G = (V, E) in its adjacency list representation  and a cost c_e for each edge e
- find the minimum cost tree (i.e. minimum edge cost) T as a subgraph of G that spans all vertices, i.e.
    - T must not contain any cycles
    - T must be connected (i.e. there is a path between all pairs of vertices)
- further assumptions:
    - input graph G is connected (can be detected e.g. by DFS)
    - edge costs are distinct

## Prim's MST Algorithm
- PRIM is very similar to Dijkstra
    0. X = {s} (s=seed edge), T = {}
    1. start with any edge from X
    2. add cheapest edge to an unexplored vertex to T
    3. repeat from 1 until X = V
- in contrast to Dijkstra, PRIM finds the MST, not the shortest path

## Correctness Proof 1
- proof that Prim always compute a spanning tree

## Correctness Proof 2
- proof that the MST calculated by Prim is minimal

## Fast Implementation 1
- Prim's running time can be calculated as O(mn) as follows:
    - O(n) iterations (n = #vertices)
    - O(m) time per iterations (m = #edges)
- this running time can be reduced to O(m log n) by using a heap as a data structure to store edges
    - problem: the minimal edge does not necessarily cross the frontier
- an even better implementation can be made by storing the vertices (not the edges) of V\X in the heap
    - the key for any v in V\X is the cheapest direct edge to X
    - if there are no direct edges from v to any x in X, the cost is infinite

## Fast Implementation 2
- each time a vertex is sucked from V\X into X, edges may now cross the frontier which haven't before (or vice versa)
- because for any v in V\X the heap key is the minimum edge to X, the keys might have to be recomputed
- a recompute is required for any vertex w in V\X with an edge (v, w)