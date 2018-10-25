# Introduction
## Why study algorithms?
Just some justifications why algorithms and understanding them are important.

## Integer multiplication (IM)

- an algorithm is a function of input values to output values
- IM as a simple example for an algorithm as a function of two input values to an output value
- number of operations grows quadratically with the number of digits in the input values
- **Refuse to be content**
    * always ask: can we do better?

## Karatsuba multiplication (KM)
- KM as special form of IM which fewer number of operations
- KM is a recursive algorithm

## About the course
Just some introduction of the topics covered, target audience, prerequisites, grading/assessment and supporting material.

## Merge Sort (MS): Motivation and example
- MS as classic demonstration of _divide and conquer_
- better than selection-, insertion- or bubble-sort
- MS is a recursive algorithm

## Merge Sort: Pseudocode
- some implementation hints ignoring end cases
- running time for input size _m_ is approximately _4m + 2_ which can be simplified to _6m_
- see [merge_sort.py](merge_sort.py) for an implementation in Python

## Merge Sort: Analysis
- number of recursions (levels): _log (n)_
- end case for recursion: single-digit array
- worst case for running time is _n log(n)_
- intuition about how many subproblems there are and what their sizes are for each level of recursion

## Guiding Principles for Analysis of Algorithms

- **Principle #1**: O-Notation gives _worst-case_, not average case (this would require domain knowledge)
- **Principle #2**: Constant factors can be neglected, because:
    * it's easier
    * constants depend on compiler/implementation
    * we lose very little predictive power
- **Principle #3**: Focus on large input sizes _n_, because only big problems are interesting 
    * Statements like _O(n log(n)) is better than O(n²)_ only hold true for large n 
- **Notion of fast**: algorithm grows slowly with input size
- **Holy grail**: Linear growth

# Asymptotic Analysis (AA)

## The Gist
- **Motivation for AA**: Introduce vocabulary for reasoning about algorithms that is
    * coarse enough to suppress details (abstraction)
    * sharp enough for comparison (predictive power)
- **High-level idea**: Suppress constant factors (system-dependent) and lower-order terms (irrelevant for large inputs)        
- **Example 1**: check if array _arr_ contains integer _i_ (O(n))
- **Example 2**: check if any of the arrays _arr1_ and _arr2_ contains integer _i_  (O(n))
- **Example 3**: check if the arrays _arr1_ and _arr2_ contain a common integer _i_ with a nested loop (O(n²))

## Big-Oh Notation
- Informal: _O(f(n))_, wobei _f(n)_ die obere Grenze für grosse _n_ angibt
- Formal: T(n) = O(f(n)) iff there are constants _c, n' > 0_ such that T(n) <= c*f(n) for all n >= n'
    * c und n' sind **unabhängig** von n!
    * c definiert die obere Grenze
    * n' definiert, was "grosse n" bedeutet 
    
## Basic examples
- **Example 1**: T(n) = a_k*n^k + .... + a_n
    - T(n) = O(n), i.e. constants and lower order terms are suppressed 
    - Proof: gültig für n'=1 und c=a_k*n^k + .... + a_n
- **Example 2 (non-example)**: for every k >= 1 n^k is not in O(n^(k-1))
    - Proof by contradiction: n^k <= c*n^(k-1) for all n >= n'
        - collapses to n <= c for all n >= n', which is false     
        
## Big Omega and Theta
- Big Omega and Big Theta are **close relatives** of Big-Oh          
    - Big-Oh: "T(n) is less than or equal to" (_f(n)_ gives upper bound)
    - Big-Omega: "T(n) is greater than or equal to" (_f(n)_ gives lower bound)
    - Big-Theta: "T(n) is equal to" (_f(n)_ gives upper and lower bounds with two different constants c1 and c2)
- Little-Oh notation is a stronger constraint in that the Big-Oh notation has to hold for all constants c>0