# The Knapsack Problem

## The Knapsack Problem
- given n items with w_i (the size of item i) and v_i (the value of item i) as well as W (the capacity)
    --> find a subset S of the items that maximize sum(v_i) subject to sum(w_i) <=W 

## A Dynamic Programming Algorithm
- V_(i,x): Value of the best solution that only uses the first i items and has a total size <= x
- For each i in {1, .., n} and any x there are two cases, from which we take the bigger value
    - V_(i-1, x) --> last item i excluded
    - v_i + V_(i-1, x-w_i) --> last item included
- The Knapsack problem can be solved by calculating a 2D-matrix of shape (n, W):
    - Initialize A[0,:] = 0
    - for i in {1,2,...,n}
        - for x in {0,1,...,W}    
            - A[i,x] = max(A[i-1,x], A[i-1, x-w_i] + v_i)
            - if w_i > W we are forced to use the first case

## Example (Optional)
- Example with n=4, W=6
- a matrix A is filled out
- as with the examples for Dynamic Programming before, this matrix holds the optimal value of the Knapsack Problem, but not the optimal subset
- the optimal subset can be reconstructed by backtracking from the maximum value

# Sequence Alignment

## Optimal Substructure
- Needleman-Wunsch algorithm: penalty for gap and mismatch
- Goal: minimize the sum of penalties
- As before we peel of single characters of string X and Y from the right, distinguishing three cases:
    - Case 1: x_m, y_m matched (the last letters appear in both alignments)
    - Case 2: x_m was matched with a gap (the last letter of the alignment of Y is a gap)
    - Case 3: y_m was matched with a gap (the last letter of the alignment of X is a gap)
    --> a case where a gap was matched with a gap does not make sense

## A Dynamic Programming Algorithm
- let P_ij be the penalty of optimal alignment of X_i with Y_j
- for all i=1..m and j=1..n
    - P_ij = min(match_score + P_i-1,j-i , gap_penalty + P_i-1,j , gap_penalty + P_i,j-1)
- Create a matrix A  in O(m*n) as follows:
    - A[i,0] = A[0,1] = i * gap_penalty
    - for i=1..m
        - for j=1..n
            - A[i.j] = min(
                A[i-1, j-1] + match_score, --> match x_i with y_i
                A[i-1, j] + gap_score, --> match x_i with a gap
                A[i, j-1] + gap_score --> match y_i with a gap
            )
- the optimal alignment can be reconstructed by backtracking from the last cell (A[m,n]) in O(m+n)

# Optimal Binary Search Trees

## Problem Definition
- as stated in part one, there are many possible binary search trees (BST) for any given set of keys
- Question: Which one should we use (which one is the best)?
- Answer: A balanced search tree like Red-Black-Trees (which has equal number of nodes to the left and right of the root)
    --> in the worst case th search time for this tree is its height, i.e. O(log n)
- if the frequency with which each key is searched is not uniform, this can still be improved by using an unbalanced search tree
    --> this will increase the search time for the worst case, but improve the average search time
- the goal is therefore to compute a valid search tree that minimizes the weighted (average) search time
    --> C(T) = sum(p_i * search_time_i)
    --> the search time of i can be computed from its depth + 1             

## Optimal Substructure
- a greedy algorithm will not work to compute the optimal BST
- this is true for top-down (select the most frequent node as root and then recurse) as well for bottom-up (select the least frequent nodes as leaves) approaches
- if we knew the optimal BST, we could backtrack from it --> dynamic programming approach
- this means for an optimal BST with node r, the left subtree is optimal for the keys [1..r-1] and the right subtree is optimal for the keys [r+1..n]. This is recursively true for any subtree.
- this means that the subtrees in the optimal BST are optimal substructure

## Proof of Optimal Substructure
- proof by contradiction that above substructures are optimal

## A Dynamic Programming Algorithm 1
- create a matrix A for dynamic programming by recurring over prefixes (left subtree) or suffixes (right subtree) of the BST
- the recurrence implies that for any prefix its suffixes must also be evaluated
- this means that the search time for any contiguous interval i..j must be calculated
- therefore A has dimension (i,j)
- For every 1 <= i <= j <= n
    - C_ij = min_r ( sum(p_i) + C_i,r-1, + C_r,ij)  for r=i..j 
    - if r=i: C_i,r-1 = 0
    - if r=j: C_r,ij = 0

## A Dynamic Programming Algorithm 2
- Important: solve the subproblems from smallest to largest (as we have done for Knapsack or Sequence Alignment)
- the size of the subproblem is calculated as the number of nodes in it (i.e. j-i+1)
- for s=0..n-1   --> s = j-i
    - for i=1..n
        - A[i, i+s] = min (sum(p_k) + A[i, r-1] + A[r+1, i+s])
- this means we compute the matrix A by computing the diagnoal and then moving the diagonal 
- The number of subproblesm to solve for this algorithm is O(n²/2) which is O(n²)
- in each subproblem we have O(j-i) possible roots to try out, which is O(n)
- The overall running time is therefore O(n³)