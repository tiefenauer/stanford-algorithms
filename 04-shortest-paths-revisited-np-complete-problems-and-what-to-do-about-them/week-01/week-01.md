# The Bellman-Ford Algorithm

## Single-Source Shortest Paths, Revisited
- Recap: given a directed graph G=(V, E), edge lengths C_e for each edge and a source vertex s
    --> find the shortest path from s to any target vertex v
- Dijkstra can find a shortest path for nonnegative edge lengths in O(m log n) using heaps (m=#edges, n=#vertices). However, Dijkstra has two drawbacks:
    - it works only on nonnegative edges (can be a problem if the graph models e.g. financial transactions)
    - the whole graph must be in-memory, i.e. it is not very distributed (can be a problem e.g. for internet routing)
- the Bellman-Ford algorithm does not have above drawbacks. 
- However there is a problem with negative edges: if we have a negative cycle in the s-v path, this could lead to an infinite loop, because we can always get a shorter path by going through the cycle one more time. If we want to compute cycle-free s-v paths on the other hand, this is a NP-hard problem (i.e. there is no efficient implementation).
- therefore we will concentrate on negative-cycle-free graphs for the BF algorithms for now. 
- in a later version, the BF algorithm should output the negative cycle if the input graph contains one.  

## Optimal Substructure
- the input graphs usually have no obvious ordering (except special graphs like path graphs)
- we can however exploit the sequential nature of the **output** graph (i.e. the shortest path, which is a sub-graph of the input graph)
- however, with this approach, it is not clear how to define "smaller" and "larger" subproblems
- by artificially restricting the number of edges in a path ("edge budget",  a parameter i in the BF algorithm). The subproblem size then corresponds with the number of permitted edges. This also allows input graphs with negative cycles, because the edge budget prevents infinite loops
- The algorithm is then as follows:
    - for i in [1,2,...]:
        - P = shortest s-v path with at most i edges. There are 2 cases:
            Case 1: P has <= (i-1) edges --> it is a shortest s-v path with at most (i-1) edges
            Case 2: P has i edges with last edge (w,v) --> P' is a shortest s-w path with at most (i-1) edges
            
## The Basic Algorithm 1
- the BF algorithm can compute the shortest s-t path in O(m*n)
- let L_i,v be the minimum length of a s-v path with <= i edges
- L_i,v = min(Case1, Case2) 
    --> Case1 = L_{i-1,v}
    --> Case2 = min(L_{i-1,w} + C_wv) for all w that have an edge to v 
- if the input graph is assumed to have no negative cycles, a shortest s-t path does not contain any cycles --> if it had one, we could simply remove it and get an even shorter path
- this means a shortest path can have at most n-1 edges (otherwise we would visit a vertex twice and have a cycle, which contradicts above assumption).
- this means we only have to compute above recursion for i in [0,1,...,n-1] 
- the algorithm in pseudo-code:
    - A = (i,v)-matrix
    - base case: i=0 --> empty path --> A[0,s] = 0, A[0,v] = +inf for all v != s
    - for i in [1,2,...,n-1]:
        - for each v in V:
            - A[i,v] = min(A[i-1, v], min(A[i-1, w] + c_wv))
            
## The Basic Algorithm 2
- the BF algorithm applied on an example graph

## Detecting-negative cycles
- above algorithm works for negative-cycle-free graphs
- we can detect a negative cycle if we run the algorithm for one more iteration (i.e. with i=n)
    --> if we don't get a better result, the graph does not have a negative cycle
- the rest of the video is the proof that the graph must contain a negative cycle if the matrix A is different for i=n than when computed for i=n-1

## A Space Optimization
- The basic algorithm uses O(n²) space
- this can be improved to linear space (O(n)) by only ever keeping the last two columns in the matrix
    --> we only need the results of the last iteration (i-1) to compute the values for i
    --> drawback: we can't reconstruct the optimal s-t path anymore
- by using predecessor pointers, we get linear space requirement AND the ability to recontstruct the shortest path!
- Idea: compute a second table B where B[i,v] = 2nd-to-last-vertex on a shortest s-v path with at most i edges (or NULL if no path exists)

# All-Pairs Shortest Paths (APSP)

## Problem Definition
- other than the single-source shortest path (Dijkstra, Bellman-Ford), APSP tries to find the shortest path for **all** pairs of vertices or report that G contains a negative cycle
- this could be simulated by running the single-source shortest path algorithm n times with different source vertices
- when there are only nonnegative edge costs, we can use Dijkstra (O(m log n)) as the workhorse
    --> for a sparsely connected graph (m is roughly n), the running time is O(n*m log n) = O(n² log n)
    --> for a densely conneccted graph (m is roughly n²), the running time is O(n³)
- when there are negative edge costs, we can use Bellman-Ford (O(n*m)):
    --> for a sparsely connected graph (m is roughly n), the running time is O(n²*m) = O(n³)
    --> for a densely conneccted graph (m is roughly n²), the running time is O(n⁴)
- O(n³) seems like an obvious minimal upper bound for the running time to compute APSP, but like with Strassen's algorithm for multiplication, there could be a similar algorithm for APSP, which has just not been found yet --> nobody knows if the optimal running time can be reduced 

## Optimal Substructure
- There is indeed an algorithm (Floyd Warshal) that does not require O(n⁴) but O(n³) running time to compute APSP for graphs with negative edge lengths
- for graphs with only nonnegative edge lengths, running Dijkstra n times will still be faster (O(n²))
- similar to the Bellman-Ford algorithm, it can be tricky to define the size ("smaller" or "largeer") of the subproblems. Instead of introducing a "edge budget" parameter i that defines this size, the key idea with Floyd-Warshall is to precisely define which vertices are allowed in a subproblem
    --> in Bellman-Ford, the prefix of the subproblem is defined by the number of allowed edges
    --> in Floyd-Warshall, the prefix of the subproblem ist defined by an arbitrary ordering of vertices 
- the optimal substructure lemma: suppose G has no negative cost cycle. Let P be a shortest (cycle-free) i-j path with all internal nodes in V(k)={1,2,...,k}
    --> Case 1: if P does not use vertex k, then P is a shortest i-j with all internal vertices in V(k-1)
    --> Case 2: if k is internal to P, then P1 is the shortest i-k path with all internal vertices in V(k-1) and P2 is the shortest k-j path with all internal nodes in V(k-i)
    
## The Floyd-Warshall Algorithm
- Pseudo Code:
    - let A=3D-Array indexed by (i,j,k)
    - base cases: for all i,j in V: 
        if i==j: A[i,j,0] = 0
        if (i,j) in E: A[i,j,0] = C_ij
        if (i,j) not in E: A[i,j,0] = inf 
    - for k in 1..n (smallest subproblem first!)
        - for i=1..n
            - for j=1..n
                A[i,j,k] = min(Case1, Case2)
                    --> Case1: A[i,j,k-1] (re-use the same path without k)
                    --> Case2: A[i,k,k-1] + A[k,j, k-1] (conatenate P1, the i-k path, and P2, the k-j path)
- Above code relies on the assumption that the input graph does not have negative cost cycles
- Question 1: What if the input graph has negative cycles?
    --> If the input graph does have a negative cost cycle, then at least one negative number in A[i,i,n] for at least one i in V at the end of the algorithm
- Question 2: How can we reconstruct a shortest i-j path?
    --> like in the BF algorithm we have use a helper matrix B, where as B[i,j]=max label of an internal node on a shortest i-j path
    --> B[i.j] = k if Case2 was used to compute the shortest path, else use the last vertex
    
## A Reweighting Technique
- Johnson's Algorithm shows that the APSP problem can be reduced to n invocations of Dijkstras algorithm, even for input graphs with negative edge lengths! (i.e. O(m*n*log n) running time)
- Johnson's Algorithm uses 1 invocation of Bellman-Ford (O(m*n)) and n invocations of Dijkstra (O(n*m*log n))
- Transforming a graph G with negative edge weights into a graph G' with only nonnegative edge lengths by adding some constant to all weights will work, but only if the number of edges between any (i,j) is the same for all paths between (i,j). Otherwise, the shortest path between i and j might change because the total length of the paths between i and j might be increased with different amounts 
- a better reweighting technique can be obtained by adding a weight p_i to every vertex i in V
    --> the new weight for an edge e=(u,v) with length C_e can be calculated as: C_e' = C_e + p_u, - p_v
    --> for any given path P=(s,t) (not necessarily a shortest path), the length L' can be computed as L'=L + p_s - p_t. Because the edges of P are reweighed as C_e' = C_e + p_u - p_v and each u and v are start and end vertex of an edge (except for u=s and v=t), the reweightings cancel each other out when summing up all reweighted edges (except for p_s and p_t)
    --> because every path between s and t is shifted by the same amount (p_s - p_t), regardless of the number of edges in between, the shortest path between s and t is not changed!
    --> the problem is therefore to find values p_i to transform the APSP for graphs with negative edgte lengths into a problem for a graph with nonnegative edge lengths
    
## Johnson's Algorithm 1
- The vertex weights p_i are computed by running the Bellman-Ford a single time (or Dijkstra, if there are only nonnegative edges). 
- The start vertex s is an artificial vertex with edges to all original vertices in the graph. The edge lengths are zero.
- by computing the shortest path from s to any vertex, the vertex weight p_v of each vertex v can be computed as the total length of the s-v path
- after that, all shortest paths can be computed by running Dijkstra n times with a different start vertex of the original graph each time
- for each shortest u-v path reconstruct the distiance in the original graph by calculating d(u,v) = d'(u-v) - p_u + p_v 

## Johnson's Algorithm 2
- recap of above 5 steps
- the running time of each step in Johnson's algorithm is O(n) + O(m*n) + O(m) + O(n*m*log n) + O(n²) --> O(m*n*log n) dominates
    --> much better than Floyd-Warshall for sparse graphs!
- proof why C'_e = C_e + p_u - p_v is greater or greater than one