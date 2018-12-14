from heapq import heapify

if __name__ == '__main__':
    numbers = [5, 1, 763, 3, 54, 2, 6, 1]
    print('some numbers:')
    print(numbers)
    print('heapify...')
    heapify(numbers)
    print(numbers)
    numbers.append(0)
    print(numbers)
