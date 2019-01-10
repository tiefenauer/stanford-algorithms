import random


def merge_sort(arr):
    """
    Sorts an array of integers using Merge-Sort in O(n log n) time.
    The array is recursively split into the left and right half and then recurses on each half.
    :param arr: array of integers
    :return: array with the same elements in sorted order
    """
    if len(arr) <= 1:
        # nothing to sort
        return arr

    # split into left and right half
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    # recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # merge both sorted halves into a new array
    return merge(left, right)


def merge(left, right):
    """
    Merge subroutine: Merges two sorted halves into a new array.
    Merging is done using separate indices for the left and right half and copying over elements of either into the new
    array.
    - The current left is copied if it is smaller than the current right element and the index is moved.
    - Vice versa the current right element is copied if it is smaller than the current left element
    Above steps are repeated until all the elements from both halves have been copied to the new array
    :param left: left half
    :param right: right half
    :return: both sides merged with element in ascecnding order
    """
    n = len(left) + len(right)
    c = [None] * n
    i, j = 0, 0
    for k in range(n):
        if j >= len(right) or i < len(left) and left[i] < right[j]:
            c[k] = left[i]
            i += 1
        elif j < len(right):
            c[k] = right[j]
            j += 1
    return c


if __name__ == '__main__':
    arr = list(range(10))
    random.shuffle(arr)
    print('array:', arr)
    arr_sorted = merge_sort(arr)
    print('sorted array:', arr_sorted)
    assert arr_sorted == list(range(10))
