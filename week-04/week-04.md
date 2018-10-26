# Linear-Time selection

## Randomized Selection - Algorithm

- selection problem: get the i-th smallest element from an array
- selection in O(n*log n) is possible with Merge Sort: the element will be at the i-th position
- selection in linear time is possible with randomized algorithm
- linear time O(n) holds true regardless of the length of the input array or the choice of the pivot
- linear selection is possible because only one recursive call has to be made
    - if the order is smaller than the position of the pivot element after partitioning, only the left partition needs to be recursively examined (with the same order)
    - if the order is greater than the position of the pivot element after partitioning, only the right partition needs to be recursively examined (with the order reduced by the position of the pivot)
    - if the order is equal to the position of the pivot element after partitioning, the pivot element is the i-th order element
    
## Randomized Selection - Analysis
