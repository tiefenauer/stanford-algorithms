# Linear-Time selection

## Randomized Selection - Algorithm ([implementation](randomized_selection.py))

- selection problem: get the i-th smallest element from an array
- selection in O(n*log n) is possible with Merge Sort: the element will be at the i-th position
- selection in linear time is possible with randomized algorithm
- linear time O(n) holds true regardless of the length of the input array or the choice of the pivot
- linear selection is possible because only one recursive call has to be made
    - if the order is smaller than the position of the pivot element after partitioning, only the left partition needs to be recursively examined (with the same order)
    - if the order is greater than the position of the pivot element after partitioning, only the right partition needs to be recursively examined (with the order reduced by the position of the pivot)
    - if the order is equal to the position of the pivot element after partitioning, the pivot element is the i-th order element
    
## Randomized Selection - Analysis
Proof why Randomized Selection runs in O(n) on average (I skipped after half of the video)

# Graphs and the Contraction Algorithm

## Graphs and Minimum Cuts
- graph: vertices (V) and edges (E) (e.g. road network, internet, ...)
- cut of a graphs: partition of V into two non-empty sets A and B
    - crossing edges: edges where one vertex is in A and one is in B
    - minimum cut: cut with fewest number of crossing edges
    - minimum cut application: community detection in social networks, bottleneck detection in networks
    
## Graph representation
- m=#vertices, n=#edges
- a connected graph with n vertices has at least n-1 and at most n*(n-1)/2 edges
    - this means m is Omega(n) and O(n²) 
- sparse graph: m is close to O(n)
- dense graph: m is close to O(n²)
- representation option 1: adjacency matrix, which has a Theta(n²) space requirement (bad for sparse graphs)
- representation option 2: adjacency list, which has a Theta(n+m) space requirement

## Random Contraction Algorithm ([implementation](./random_contraction.py))
- calculates the minimum cut of a graph
- edges are subsequently deleted (i.e. vertices that are connected by an edge are merged) until there are only 2 vertices left (A and B)
- selection of vertices is randomized

## Analysis of Contraction Algorithm
- edges from the graph must not be selected for contraction if they connect A and B, otherwise A and B would collapse into the same node and the output graph graph would not contain distinct nodes A and B (i.e. the algorithm would not produce a minimum cut)
- denote the set of crossing edges connecting A and B as F
- success probability of the contraction algorithm boils down to the probability of selecting an edge from the graph that is in F
- for k=#edges in F, the degree (=#incident edges) of each vertex is at least k
- the probability for choosing an edge (i.e. screw up) from F is 2/n for the first iteration
    - in other words: the probability of success is 1 - 2/n
- for the next iteration the probability for success is 1 - k/#number of edges. However, the number of edges can not be stated generally. Therefore the probability for success is derived from the number of remaining vertices (which is n-1) 
    - any node in the contracted graph has again at least degree k (contracted nodes too, as they can be seen as a group of nodes in the original graph)
    - therefore the number of remaining edges is >= 1/2 * k(n-1)
    - this gives us the probability for the next iteration as 1 - 2/(n-1)
- this pattern can be generalized for the n-2 iterations: (1 - 2/n) * (1 - 2/(n-1)) * ... * (1 - 2/(n-(n-4))) * (1 - 2/(n-(n-3)))     
- this can be simplified by crossing out almost all terms (n-i)
    - this gives us a probability for success of 2/n(n-1) which is can be rounded down to 1/n²
    - this probability seems very low, but is actually high compared to the exponential number of edges
    - by repeatedly running the algorithm and taking the lowest value, the probability for getting the correct value for the minimum cut becomes pretty high. 
    - The probability that all trials fail can be expressed as (1 - 1/n²)^N, which becomes quite low for N = n² * ln n
    
## Counting Minimum Cuts
- a tree with n vertices has n-1 minimum cuts
- generally for graphs the number of minimum cuts is n choose 2 (i.e. n(n-1)/2)