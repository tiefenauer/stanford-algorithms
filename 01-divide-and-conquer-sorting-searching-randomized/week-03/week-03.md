# Quicksort - Algorithm

## Overview
- element of array is selected as pivot element: array is rearranged around this element 
    - elements to the left are smaller
    - elements to the right are larger
    - pivot element ends up in its "rightful" position
- partitions (left, right) are not sorted, but partitioning subroutine is used to make progress towards sorting
    - partitioning is cheap (linear time, no extra memory)
    - partitioning reduces problem size (recursively sort elements at the left and right through divide and conquer)

## Quicksort - Analysis
- partitioning subroutine should perform partitioning in linear time with no extra memory, i.e. in-place 
    - partitioning in linear time with extra memory is trivial!
- in-place partitioning uses a single scan through the array
    - pivot element is first item (and remains there)
    - 2 groups afterwards: elements that were already scanned and elements that will be scanned --> boundary j 
    - the first group can be partitioned into left and right partition --> boundary i
    - scan from left to right:
        - if element is bigger than the pivot element: leave it there
        - if element is smaller: swap with the first element of the right partition 
        
## Correctness of Quicksort (Review - Optional)

Not done

# Quicksort - Analysis

## Decomposing Principle


## Choosing a Good Pivot
- If given an already sorted array of size n and always choosing the first element as pivot, Quicksort runs in O(n²), which is bad
- the reason for this is that the split is very unbalanced: 
    - the left partition is an empty set and the right partition
    - the right partition is a set with size n-1
- choosing a good pivot is therefore crucial
- choosing the median as pivot results in a balanced split of left and right partition, which results in an running time T(n) = O(n*log n) as the lower bound of the algorithm
- because finding the median requires O(n) time, another idea is to choose the pivot at random in each recursion
    - a random pivot is "pretty good" "often enough"
    - a 25%/75% split is good enough for O(n*log(n)) running time
    - the chance for such a split is 50%: in an array with the numbers 1-100 all the numbers between 25 and 75 will result in a split with a left or right partition of at least 25%
    
## Probability Review I
- Concept #1: sample space: "all possible outcomes", each outcome has a known probability p>=0 should add up to 1
- Concept #2: events: subset of sample space, probability of event is sum of probabilities in event samples
- Concept #3: random variables: real-valued function from sample space to real value
- Concept #4: expectation: average value over all individual probabilities: E[X] = 1/n * sum( p(x_n)*x_n )
- Concept #5: linearity of expectation: The expected value of a sum of random variables is equal to the sum of the expected values of the random variables 
    - the expectation value of a single die is the sum of the individual probability values: 1/6 * (1+2+3+4+5+6) = 3.5 
    - the expectation value of the sum of two dice is the sum of expectation values of both dices: 3.5 + 3.5 = 7 

## Probability Review II
- Concept #6: Conditional probability: p(X|Y) = p(X and Y)/p(Y) 
- Concept #7: Independence of events: events are independend iff p(x and Y) == p(x) * p(x)
    - intuition: knowing that Y happens gives no information about the outcome of X
    - INTUITION IS OFTEN WRONG!!!
- only if two variables are independent: E[A * B] == E[A] * E[B] 