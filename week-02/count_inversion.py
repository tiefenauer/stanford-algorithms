# count inversions
def sort_and_count(a):
    n = len(a)
    if n == 1:
        return a, 0
    left, right = a[:n // 2], a[n // 2:]
    b, x = sort_and_count(left)
    c, y = sort_and_count(right)

    d, z = merge_and_count_split(b, c, n)
    return d, x + y + z


def merge_and_count_split(b, c, n):
    count = 0
    d = [None] * n
    i, j = 0, 0
    for k in range(n):
        if j >= len(c) or i < len(b) and b[i] < c[j]:
            d[k] = b[i]
            i += 1
        elif j < len(c):
            d[k] = c[j]
            count += len(b[i:])
            j += 1
    return d, count


if __name__ == '__main__':
    a = [1, 3, 5, 2, 4, 6]
    print(a)
    print(sort_and_count(a))

    with open('IntegerArray.txt', 'r') as f:
        a = [int(line) for line in f.readlines()]
        print(len(a))
        _, num_inversions = sort_and_count(a)
        print(num_inversions)
