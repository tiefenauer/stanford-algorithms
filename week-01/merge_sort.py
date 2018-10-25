# O( n log(n) )
def merge_sort(arr):
    if len(arr) == 1:
        return arr
    n = len(arr)
    a = merge_sort(arr[:n // 2])
    b = merge_sort(arr[n // 2:])

    return merge(a, b, len(arr))


# merge subroutine
def merge(a, b, n):
    c = [None] * n
    i, j = 0, 0
    for k in range(n):
        if j >= len(b) or i < len(a) and a[i] < b[j]:
            c[k] = a[i]
            i += 1
        elif j < len(b):
            c[k] = b[j]
            j += 1
    return c


if __name__ == '__main__':
    arr = [5, 4, 1, 8, 7, 2, 6, 3]
    print(arr)
    print(merge_sort(arr))
