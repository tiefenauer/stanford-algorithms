# Graph Search and Connectivity
## Overview
- Motivations for graph search
    - check if network is connected (e.g. Bacon Number)
    - driving directions (from A to B)
    - formulate a plan (path as a sequence of decisions, e.g. to solve a Sudoku puzzle)
- generic graph search: algorithm starts at starting node S and iteratively adds vertices that are reachable in order to explore the graph. Any graph search algorithm has 2 goals: 
    - find everything findable from S
    - don't explore anything twice (goal: O(m+n))

## Breadth-First Search (BFS) - The Basics
- takes linear time O(n_s + m_s) using a QUEUE (FiFo) where n_s and m_s are the number of nodes resp. edges reachable from s
- explores nodes in "layers": 
    1. start with a starting node s
    2. add immediate neighbors to queue Q
    3. remove first node from Q and use this as the starting node for the next iteration
- can compute shortest path
- can compute connected components of an undirected graph

## BFS and Shortest Paths
- the shortest path from s to v can be computed by counting the number of layers between s and v
- the rest of the video is an example on a simple graph and a proof why the shortest path is the number of layers between s and v

## BFS and Undirected Connectivity
- Connected components = the "pieces" of a a graph
- Goal: compute all connected components (e.g. to check if a network is disconnected)
- this can be done by running BFS with every node of the graph as starting node
    - keep a list of nodes explored by any starting node
    - only run BFS if the starting node is not in the list

## Depth-First Search (DFS): The Basics
- takes linear time using a STACK (LiFo)
- like exploring a maze: go as far as possible, backtracking only when necessary
- compute topological ordering
- can compute connected components in directed graphs

## Topological Sort
- Topological Ordering: Order of vertices so that for each edge (u,v) the property f(u) < f(v) whereas f(x) is a function mapping a vertex to an ordinal
    --> all the edges go forward when the vertices are put next to each other in ther topological ordering
- motivation: e.g. to build sequence of courses where course A might be a prerequisite for course B
- a graph must not contain a directed cycle to have an ordering
- every directed acyclic graph has a sink vertex (vertex without outgoing edges). The reason for this is the following: when following n edges, we have visited n+1 vertices. If we have visited all vertices in an acyclic graph and there is still an outgoing edge in the last vertex, the next vertex MUST be an already visited vertex (pigeon hole principle), i.e. it contains a cycle (contradiction to acyclic assumption)
- The sink vertex MUST come last in the topological ordering

## Computing Strongly Connected Components (SCC) - The Algorithm
- SCC: maximally connected subgraphs where we can get from any vertex A to any vertex B
- DFS can be used to compute the SCCs of a graph
    - using DFS with a node of a SCC as start node, DFS will find all nodes of the SCC
    - unfortunately, it can also traverse edges that lead to nodes of other SCC when starting with the wrong node
    - in the worst case, DFS will find all nodes from the entire graph
    - therefore DFS can not simply be used iteratively, each time using a different node from a graph as starting point    
- Kosaraju's Two-Pass Algorithm: 2-pass algorithm
    - 1st step: reverse all edges
    - 2nd step: run DFS on reversed graph (first pass) --> this will find out the "magical" order of nodes for the second pass by computing the finishing times
        0. reverse the edges of the graph
        1. initialize a global variable t=0 to hold the finishing times
        3. use the highest node of the the currently unexplored nodes as starting point and perform DFS
        4. each time you encounter a dead end, increase t and set the node's finishing time as t
        5. while backtracking increase t and set the finishing time for each backtracked node
        6. when DFS is finished for the current starting point, continue with 3. 
    - 3rd step: run DFS on original graph (second pass) --> when using above order of nodes as starting nodes, this will discover the SCCs!
        0. initialize a global variable s=None to hold the current leader
        1. Reverse the edges to get the original graph again
        2. use the finishing times from the first pass to find out the order of the nodes to use as starting points
        3. start with the node with the highest finishing time (from the set of unexplored nodes) as starting node (an current leader) and perform a DFS
        4. set the current leader for each node while performing DFS 
        5. continue with 3
        
## Computing Strongly Connected Components (SCC) - The Analysis
- proof why Kosaraiu's algorithm works
- proof by drawing a meta-graph of the SCCs (rest of proof omitted here)