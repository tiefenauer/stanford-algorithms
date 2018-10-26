def quicksort(a, pivot_fun, counter=0):
    global num_comparisons
    n = len(a)
    if n <= 1:
        return a, counter

    # increase number of comparisons
    counter += n - 1

    # determine pivot element
    pivot_ix = pivot_fun(a, n)
    p = a[pivot_ix]

    # swap pivot element with first element and do partitioning
    a[0], a[pivot_ix] = a[pivot_ix], a[0]
    i = partition_inplace(a, p)

    # recurively sort left and right partition
    left, counter = quicksort(a[:i], pivot_fun, counter)
    right, counter = quicksort(a[i + 1:], pivot_fun, counter)

    return left + a[i:i + 1] + right, counter


def pivot_first(a, n):
    return 0


def pivot_last(a, n):
    return n - 1


def pivot_median_three(a, n):
    mid_ix = (n - 1) // 2
    first, middle, last = a[0], a[mid_ix], a[-1]
    if min(first, last) <= middle <= max(first, last):
        return mid_ix
    if min(middle, last) <= first <= max(middle, last):
        return 0
    if min(first, middle) <= last <= max(first, middle):
        return len(a) - 1
    return None


def partition_inplace(a, p):
    i = 1
    for j in range(1, len(a)):
        if a[j] < p:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i - 1], a[0] = a[0], a[i - 1]
    return i - 1


if __name__ == '__main__':
    arr = [3, 8, 2, 5, 1, 4, 7, 6]
    print(arr)
    print(quicksort(arr, pivot_fun=pivot_first))

    for pivot_fun, num_comparisons in [(pivot_first, 162085), (pivot_last, 164123), (pivot_median_three, 138382)]:
        with open('QuickSort.txt', 'r') as f:
            arr = [int(line) for line in f.readlines()]
        arr_sorted, counter = quicksort(arr, pivot_fun=pivot_fun)
        print(counter)
        print(counter == num_comparisons)
        print(arr_sorted == sorted(arr))
