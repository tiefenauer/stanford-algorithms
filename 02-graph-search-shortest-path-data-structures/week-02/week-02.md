# Dijkstra's Shortest Path Algorithm

## Dijkstra's Shortest Path Algorithm
- Finds for a single source vertex A a shortest path to any target vertex B under the following assumptions
    - B is reachable from A (can be found out using DFS or BFS)
    - graph edges have nonnegative (!) weights (e.g. lengths)! Dijkstra will NOT work with negative edges!
- Objection 1: but BFS already finds a shortest path in linear time
    - Answer: BFS also finds shortest paths, but only if all the edge lengths are equal (special case)!
- Objection 2: we could replace each weighted edge by a number of unit length edges
    - Answer: That would blow up the graph too much
- Objection 3: Why can we not just add the amount of the most negative edge to all edges to get only nonnegative edges?
    - Answer: because the number of edges for single sub-paths is different so this does not preserve the shortest path  
- The algorithm steps for a set of vertices V:
    - Initialization for source vertex s:
        - X = {s} (the set of visited edges)
        - A[s] = 0 (computed shortest path distances)
        - B[s] = [] (actual path from s to target vertex --> optional)
    - Main Loop: while X != V
        - from current optimal node v* in X pick the edge to vertex w* in V\X with the minimum total (!) distance (greedy)
        - set A[w*] = A[v*] + l_(v*w*)
        - set B[w*] = B[v*] + (v*w*)
        
## Dijkstra's Algorithm: Examples
- Some examples and a non-example to show why Dijkstra only works with nonnegative edges

## Correctness of Dijkstra's Algorithm
- Proof why the algorithm is correct

## Implementation and Running Time
- While-Loop: only consider edges crossing from X to V\X and select the edge with the minimum total length
- a naïve implementation would be in O(m*n) (m=number of edges, n=number of vertices):
    - the main loop iterates over all vertices (n-1 times)
    - in each loop each edge is evaluated (if it is selectable and if it is the edge with the minimum total length)
- This running time can be reduced to O(m*log n) by using a heap as data structure
    - heap is optimal to find a minimum
    - Insert and min-extraction in O(log n)
- Invariant #1: Keep all vertices (heads) in V\X in a heap
- Invariant #2: store as a map for alls v's in V\X with the smallest Dijkstra greedy score of an edge (u,v) with u in X (infinity, if no edge to v) as the key
- extract the minimum of the heap to get the next vertex w* to add to X
    - don't forget to set A[w*] to key(w*)
- because when moving a vertex w* from V\X to X the frontier changes, there might be edges that now cross the frontier (which haven't before) and the minimal Dijkstra score changes ==> the keys in the heap need to be extracted for all vertices in V\X that are head to an edge from w*:
    - for each edge (w,v): if v in V\X
        - delete v from heap
        - recompute key[v] = min(key(v), A[v] + l_wv)