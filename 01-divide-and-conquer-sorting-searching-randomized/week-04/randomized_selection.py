import random


def randomized_selection(a, k):
    """
    Extract the k-th smallest element from an array of integers using randomized selection
    The array will be partitioned around a random pivot element so that the left partition contains all the elements
    smaller and the right part all elements greater than the pivot element.
    The algorithm stops if the pivot element is equal to the order. Otherwise it recurses on the left partition (if the
    pivot element is greater than the order) or the right partition (if the pivot element is smaller than the order)
    :param a: array of integers
    :param k: order of the element
    :return: the k-th smallest element of the array
    """
    assert k > 0, 'order k must be greater than 0'
    assert k <= len(arr), 'order k cannot be greater than the length of the array'

    if len(a) == 1:
        return a[0]

    # get random pivot index
    pivot_ix = random.randint(0, len(a) - 1)

    # move pivot element to the front
    a[0], a[pivot_ix] = a[pivot_ix], a[0]
    # partition array into left and right part: i will be the start of the right partition
    i = partition_inplace(a)

    if i == k - 1:
        # the partition boundary matches the order: return the element at the partition boundary
        return a[i]

    left, right = a[:i], a[i + 1:]
    if left and i > k - 1:
        # the partition boundary is greater than the order: recurse on the left partition
        return randomized_selection(left, k)

    # the partition boundary is smaller than the order: recurse on the left partition
    # note: right array cannot be empty because the pivot index must be smaller than the order here
    return randomized_selection(right, k - i - 1)


def partition_inplace(a):
    """
    partition an array so that the left partition
    :param a: an array of integers
    :return: index of the first element of the right partition
    """
    i = 0
    for j in range(1, len(a)):
        if a[j] < a[0]:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i], a[0] = a[0], a[i]
    return i


if __name__ == '__main__':
    arr = list(range(1, 100))
    random.shuffle(arr)
    print('array:', arr)

    for k in range(1, 100):
        e = randomized_selection(arr, k)
        print('k:', k)
        print('result:', e)
        assert k == e
