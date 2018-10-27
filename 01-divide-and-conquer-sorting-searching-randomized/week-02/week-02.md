# Divide & Conquer Algorithms

## O(n log n) Algorighm for Counting Inversions I
- **divide** problem into smaller subproblems
- **conquer** the subproblem with recursive calls
- **merge** solutions of subproblems to get solution of original problem 
- count inversions in a list
    - brute force approach uses O(n²)
    - divide&conquer approach uses O(n log n) for the same reasons as in Merge Sort (recursive tree, two halves where each halve can be solved in linear time)
    
## O(n log n) Algorighm for Counting Inversions II
Just an explanation of how the algorithm works. The key element is that the merge-subroutine from the Merge Sort algorithm is piggy-backed here. I.e. the sub-arrays are sorted and split-inversions (inversions which span over both halves) as follows:
- suppose array A is split into two halves, B and C
- arrays B and C are sorted and merged into array D, as done in the [Merge Sort algorithm](../week-01/merge_sort.py)
- While doing the merging into D, a counter is increased as follows:
    - if an array element from B is copied to D, the counter is not increased. The reason for this is that the element is smaller than all elements in C
    - if an array element from C is copied to D the counter is increased by the number of elements in B which have not been copied to D. The reason for this is that these elements are all greater than the element from C (i.e. there's an inversion for each on of them)
- the value of the counter after merging is the number of split inversions over the two halves B and C

## Strassen's Subcubic Matrix Multiplication Algorithm
Just an explanation of how Strassen's method of multiplying two equally sized square matrices works. The takeaway point is that Strassen's method calculates only 7 products. All element of the final matrix can be calculated from this product. You can find an implementation [here](strassen.py).

The algorithm is better than the normal algorithm of multiplying rows/colums for each cell in the final matrix because this algorithm uses O(n³), whereas Strassen's algorithm is below that. The optimum would be O(n²).

## O(n log n) Algorithm for Closest Pair I (Advanced - Optional)

Not done

## O(n log n) Algorithm for Closest Pair II (Advanced - Optional)

Not done

# The Master Method (a.k.a. _Master Theorem_)

## Motivation
- The master method helps us to assess the performance of algorithms
- The Gauss method for integer multiplication is introduced

## Formal Statement
- Assumption: all subproblems have equal size (balanced subproblem sizes)
- for the base case T(n) <= a constant (for small n)
- for larger n: T(n) <= a*T(n/b) + O(n^d). The first term describes the work done in the recursions, the last term denotes the work done outside recursive calls.
    - a >= 1: number of subproblems (i.e. the number of recursive calls)
    - b > 1: input size shrinkage factor 
    - d: exponent in summing time of "combine steps"
    - a,b and d are constant and independent of n
- We distinguish 3 cases to determine f(n) to calculate the upper bound O(f(n)) for the running time T(n):

| Case | Condition | f(n) |
|---|---|---|
| 1 | a = b^d | n^d * log n |
| 2 | a < b^d | n^d |
| 3 | a > b^d | n^(log_b a) |


## Examples
The following examples are shown to illustrate how to calculate T(n):

| Example | Algorithm | a | b | d | Case |
|---|---|---|---|---|---|
| 1 | Merge Sort | 2 | 2 | 1 | 1 |
| 2 | Binary Search | 1 | 2 | 0 | 1 |
| 3 | naive integer multiplication | 4 | 2 | 1 | 3 |
| 4 | Gauss's recursive integer multiplication | 3 | 2 | 1 | 3 |
| 5 | Strassen's Algorithm | 7 | 2 | 2 | 3 |
| 6 | imaginary algorithm | 2 | 2 | 2 | 2 |

## Proof
Proof of the Master Method. This should help inferring the formula for the three cases instead of memorizing them.