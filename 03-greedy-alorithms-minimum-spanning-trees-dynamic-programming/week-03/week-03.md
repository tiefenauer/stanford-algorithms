# Huffman Codes

## Introduction and Motivation
- Binary Codes: Mapping of characters of an alphabet ot a binary strings (e.g. ASCII)
- By using a variable bit length, some characters can be encoded with fewer bits
- The binary code has to be prefix-free in order to produce unambiguous encodings for all characters of the alphabet
    - prefix-free: for each pair of the alphabet, neither one is a prefix of the other
- by using a prefix-free encoding, the average number of bits used for encoding can be reduced     

## Problem Definition
- an encoding can be regarded as trees
- a prefix-free condition is then equivalent to the labels only appearing as leaves in the tree
- ina prefix-free encoding the encoding length of a character is equal to its depth in the tree
- the average encoding length of a tree can be computed by multiplying the probability of each character by its depth in the tree and summing up

## A Greedy Algorithm
- Huffmann's idea: build the tree bottom-up using successive mergers
- the number of bits used to encode a certain character is equal to the number of mergers it has participated in (directly or as part of a subtree)
- therefore the least frequent symbols should be encoded with the most bits/placed as the deepest nodes

## A More Complex Example
- Example with the alphabet E = {A, B, C, D, E, F} with different non-unique probabilities
- the tree is constructed bottom-up by merging the two letters with the smallest frequency into a meta-letter
- the probabilities of the meta letter is the sum of probabilities of the child letters
- the merge results in a new alphabet E' where the two letters have been replaced by one meta-letter
- this can be done recursively, treating each meta-letter as a normal letter after a merge 

## Correctness Proof 1
not viewed

## Correctness Proof 2
not viewed

# Introduction to Dynamic Programming

## Introduction: Weighted Independent Sets in Path Graphs
- problem statement: from a graph G = (V, E) with nonnegative weights on vertices an independent set with maximum total weight should be extracted 
    - independent set: set of non-adjacent vertices
- brute force (iterate through all possible subsets) would require exponential time
- a greedy algorithm picking a non-adjacent, unseen node with the highest weight in each iteration would not produce a correct result
- a divide-and-conquer approach would split the nodes up until there are only two nodes in each subgraph and then select the node with the higher weight. This might however lead to conflicts that are not easy to resolve

## WIS in Path Graphs: Optimal Substructure
- Thought experiment: suppose S is the max-weight IS of G and v_n the last vertex of the path. Let G' be the G with v_n removed. We have now 2 cases:
    - case 1: v_n is not in S --> S is also a max-weight IS of G'
    - case 2: v_n is in S --> G'' is G' with v_(n-1) removed and S\{v_n} is an max-weight IS of G''
- because there are only 2 cases if a little bird would tell us if the last node is in S or not, we could recurse on G' or G''
- by trying out both possibilities in parallel and returning the better one, we get a recursive brute-force algorithm that runs in exponential time
- dynamic programming tries to eliminate redundancy while computing the recursive algorithm and runs in O(n)

## WIS in Path Graphs: A Linear-Time Algorithm
- although the brute force approach runs in exponential time, the number of subproblems for a Graph with n nodes is only O(n) (when plucking only from the right)
- O(n) can be obtained by caching the solution of already solved subproblems ("memoization")
- Let G_i be the first i nodes of the path w_1, w_2, ..., w_n
- the caching can be done by building the graph bottom up and storing the results for G_i in an array A
    - A[0] = 0 (no nodes)
    - A[1] = w_1
    - for i in 2..n:
        - A[i] = max(A[i-1], A[i-2] + w_i)
        
## WIS in Path Graphs: A Reconstruction Algorithm
- above algorithm calculates the total weight of the max-weight IS of a path graph, but not the IS itself
- because the Array A contains all the solutions for the sub-problems it can be used to reconstruct the IS as follows:
    - process A from right to left
    - S = {}
    - if A[i-1] >= A[i-2] + w_i: i--
    - else add w_i to S and i -= 2

## Principles of Dynamic Programming
- The key ingredients of dynamic programmings are:
    - identify a small number of subproblems
    - can quickly + correctly solve larger subproblems given the solutions to smaller subproblems
    - after solving all subproblems, can quickly compute the final solution