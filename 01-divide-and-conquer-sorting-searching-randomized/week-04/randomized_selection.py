import random


def rselect(a, i):
    assert i > 0, 'order must be greater than 0'
    assert i <= len(arr), 'order must be greater than 0'

    if len(a) == 1:
        return a[0]

    pivot_ix = pivot_random(a)

    a[0], a[pivot_ix] = a[pivot_ix], a[0]
    j = partition_inplace(a)

    left, right = a[:j], a[j + 1:]
    if j == i - 1:
        return a[j]

    if left and j > i - 1:
        return rselect(left, i)

    # note: right array cannot be empty because the pivot index must be smaller than the order here
    return rselect(right, i - j - 1)


def pivot_random(a):
    return random.randint(0, len(a) - 1)


def partition_inplace(a):
    i = 1
    for j in range(1, len(a)):
        if a[j] < a[0]:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i - 1], a[0] = a[0], a[i - 1]
    return i - 1


if __name__ == '__main__':
    arr = [3, 8, 2, 5, 1, 4, 7, 6]
    e = rselect(arr, 3)
    print(arr)
    print(e)
