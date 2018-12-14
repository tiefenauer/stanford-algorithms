# Heaps

## Data Structures: Overview
- Examples: List, stack, queue, heap, search tree, hashtable, bloom filter, union-find, ...
- Reason: different data structures support different sets of operations ==> suitable for different tasks
- Rule of thumb: choose the minimal data structure that supports all the operations needed

## Heaps: Operations and Applications
- a.k.a. priority queue
- container for objects that have keys (e.g. employees, network edges, events, ...)
- a heap supports 2 operations:
    - INSERT: add a new object in O(log n)
    - EXTRACT-MIN: remove an object in heap with a minimum key (or maximum) value in O(log n)
- Also often seen: 
    - HEAPIFY (initialize a heap of n objects in O(n), not O(n*log n))
    - DELETE (delete arbitrary element from heap in O(log n))
- Application: Sorting --> fast way to do repeated minimum computations
    - Heap sort: O(n*log n)
        1. Insert all elements into heap, then
        2. extract-min to pluck out elements in sorted order 
- Application: Event Manager --> e.g. simulation for palyers in a video game
    - events of the game are inserted into the heap (key: time when the event should occur)
- Application: Median Maintanence --> tell the median of a sequence of numbers when getting them one-by-one
    - maintain two heaps: 
        - a Max-Heap H_low to store the lower half of the numbers
        - a Min-Heap H_high to store the upper half of the numbers
    - the median is either the max of H_low or the min of H_high (can both be fetched in O(log n))
    - when inserting the numbers, check if the number is smaller than the median (then insert it in H_low) or bigger (then insert it in H_high)
    - since this can lead to unbalanced heaps, they might have to be rebalanced by moving the maximum of H_low to H_high or vice versa
- Application: Speeding up Dijkstra down to O(m*log n)
    - since a minimum is calculated in each loop, a heap could be used
    
# Balanced Binary Search Tree (BBST)

## Operations and Applications
- BBST are like an improved version of sorted arrays with support for dynamic data
- a BBST sacrifices some of the running time advantages of a sorted array in order to support additional operations to insert/delete entries (because above operations work very fast on static data structure, but not on dynamic data).
- the following table shows the running times for operations on a sorted array compared to BBST 

| operation | description | running time in sorted array | running time in BBST |
|---|---|---|---|
| SEARCH | binary search | O(log n) | O(log n) |
| SELECT | given order statistic i, select i-th biggest element | O(1) | O(log n) |
| MIN/MAX | special select with i=1 or i=len | O(1) | O(log n) |
| PRED/SUCC | next smaller/bigger element | O(1) | O(log n) |
| RANK | how many entries in the BBST are <= a given value in O(log n) --> the rank is just the index of the value (or the index where it would be if it is not in the array) | O(1) | O(log n) |
| OUTPUT | in sorted order | O(n) | O(n) |
| INSERT | add a new element | O(n) | O(log n) |
| DELETE | remove an existing element | O(n) | O(log n) |

## BBST basics - I
- each node has a value and three pointers (left/right/parent)
- SEARCH TREE PROPERTY: all key stored in the left subtree of a node are smaller than the node value
- the search tree property is different from the heap property because it supports search, not finding the min/max
- for an unbalanced search tree, there are a lot of variants for the same set of values. The minimum height is log2 n, the maximum height is n
- The search for key k is implemented as follows:
    1. start at root
    2. if k<root --> go left if left else return null
    3. if if k>root --> go right if right else return null
    4. if k==root --> return root
- The insert of key k is implemented as follows:
    - if no duplicates allowed: search for k and insert instead of returning null
    - if duplicates allowed: continue by convention (e.g. left)
    - the search tree property must be maintained when inserting
    
## BBST basics - II
- the height of a search tree governs the worst-case running time of search/insert (knowing the number of nodes alone is not enough, unless the tree is balanced)
- more operations for binary search trees:
    - MIN: start at root, follow left until not possible anymore
    - MAX: like MIN, but go right
    - PRED: find next smaller value
        - easy case: node has a non-empty subtree --> return the largest element in the left subtree
        - difficult case: node has only right subtree --> follow parent until you find a node that is smaller than the start node. If there is none, the starting node has no predecessor (=is smallest)
    - OUTPUT: print all keys in sorted order using in-order traversal
        1. start at root (subtree T_l and T_r)
        2. recurse on T_l (--> go to 1. using the left node as root)
        3. print root
        4- recurse on T_r (--> go to 1. using the right node as root)
    - DELETE: a key k can be deleted by distinguishing 3 cases
        - search node
        - case 1: k has no children --> just delete k
        - case 2: k has only 1 child --> splice out k's node
        - case 3: k has 2 children --> difficult, use other tree operations
            - compute l=PRED(k) by following the right nodes in the left subtree
            - swap k and l
            - delete k: it cannot have a right child, because then we would have followed it. It can however have a left child, but to delete a node with only one child is easy (case 2)
    - SELECT and RANK: eacho node in the tree is augmented with metadata about the tree itself
        - e.g. the size of a node is the number of nodes in the subtree where the node is root. It can be computed recursively by summing up the sizes of the left and right tree and adding +1 (for itself)
    -  the size can be used to determine the RANK of a node
    
## Read-Black Trees (RBT)
- a RBT is an example of a balanced BST. The height is therefore always log n --> this ensures that all operations run in O(log n) 
- other examples: AVL trees, splaytress, B-trees, B+-trees
- RBTs must maintain four invariants
    - each node is either read or black (flag)
    - root is always black
    - no 2 reds in a row --> if a node is red, its children must be black
    - every root-NULL path (unsucessful search) passes the same number of black nodes
- by maintaining above invariants, the height is guaranteed to be <= 2* log2 (n+1)
