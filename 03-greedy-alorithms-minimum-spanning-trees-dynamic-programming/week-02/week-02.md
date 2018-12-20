# Kruskal's MST ALgorithm

## Kruskal's MST Algorithm
- alternative to PRIM to calculate MST
- contrary to PRIM, Kruskal does not grow the MST from a vertex. Instead it will iteratively add the next cheapest edge that will not create a cycle

## Correctness of Kruskal's Algorithm
- proof that Kruskal will produce a MST

## Implementing Kruskal's Algorithm via Union-Find 1
- Straightforward algorithm with polynomial runtime O(mn) (m=#edges, n=#vertices)
    - sort edges in order of increasing cost --> O(m log n)
    - T = {}
    - for i=1 to m: --> O(m) iterations
        if T + [i] has no cycles:   --> can be detected using BFS or DFS in O(n)
            add i to T
    - return T
- the running time is O(m log n) + O(mn) = O(mn) (the second term dominates)
- the union-find data structure allows cycle checks in O(1) (!)
- the union-find data structure has two operations on a partitioned graph (=groups of connected components):
    - FIND(x): return group C_i to which vertex x belongs
    - UNION(C_i, C_j): merge groups C_i, C_j into a single one    

## Implementing Kruskal's Algorithm via Union-Find 2
- the connected components of the graph are stored in separate linked structure
- each component has an arbitrary leader vertex
- invariant: each vertex points to the leader of its component 
- Key point: given edge (u,v) we can check in O(1) if this edge forms a cycle (if both have the same leader)
- if we merge two groups, we have to maintain the invariant (i.e. update the leader pointers)
    --> in the worst case O(n) leader pointer updates are required!
    --> keep the leader of the larger group
    --> keep the size of each group in a field (allows comparing sizes in O(1))
- each vertex v updates its leader pointer at most O(log n) times, because each time v's leader pointer is updated, the population of its component at least doubles

## MST: State-of-the-Art and Open Questions (Advanced - Optional)
- not viewed

# Clustering

## Application to Clustering
- informal goal: classify n "points" (web pages, images, ...) into "coherent groups"
- a similarity measure is needed to form clusters as follows:
    1. initially, put each point in a separate cluster
    2. merge the two clostest clusters
    3. repeat until only k clusters are left
- above algorithm is called single-link clustering and islike Kruskal, but stopped early (points=vertices, distances=edge costs)

## Correctness of Clustering Algorithm
- proof why single-link clustering finds the max-spacing k-clustering

# Advanced Union-Find

## Lazy Unions (Advanced - Optional)
- not viewed

## Union-By-Rank (Advanced - Optional)
- not viewed

## Analysis of Union-By-Rank (Advanced - Optional)
- not viewed

## Path Compression (Advanced - Optional) 
- not viewed

## Path Compression: The Hopcroft-Ullman Analysis 1 (Advanced - Optional)
- not viewed

## Path Compression - The Hopcfort-Ullman Analysis 2 (Advanced - Optional)
- not viewed

## The Ackerman Function (Advanced - Optional)
- not viewed

## Path Compression: Tarjan's Analysis 1 (Advanced - Optional)
- not viewed

## Path Compression: Tarjan's Analysis 2 (Advanced - Optional)
- not viewed
