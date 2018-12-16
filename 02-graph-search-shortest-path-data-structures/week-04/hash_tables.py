from random import shuffle


def deduplicate(arr):
    d = dict()
    for k, v in arr:
        if k not in d:
            d[k] = v
    return [d[k] for k in d.keys()]


if __name__ == '__main__':
    arr = []
    for i in range(10):
        arr.append((i, 10 ** i))
    arr = arr + arr
    shuffle(arr)
    no_duplicates = deduplicate(arr)
    print(no_duplicates)
