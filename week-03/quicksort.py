num_comparisons = 0


def quicksort(a, pivot_fun):
    global num_comparisons
    n = len(a)
    if n <= 1:
        return a

    num_comparisons += n - 1
    pivot_ix = pivot_fun(a, n)
    p = a[pivot_ix]
    a[0], a[pivot_ix] = a[pivot_ix], a[0]
    i = partition_inplace(a, p)
    left = a[:i]
    right = a[i + 1:]
    return quicksort(left, pivot_fun) + a[i:i + 1] + quicksort(right, pivot_fun)


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
    num_comparisons = 0
    print(quicksort(arr, pivot_fun=pivot_first), num_comparisons)

    # 162085, 164123, 138382
    for pivot_fun in [pivot_first, pivot_last, pivot_median_three]:
        with open('QuickSort.txt', 'r') as f:
            arr = [int(line) for line in f.readlines()]
        num_comparisons = 0
        arr_sorted = quicksort(arr, pivot_fun=pivot_fun)
        print(num_comparisons)
        print(arr_sorted == sorted(arr))
