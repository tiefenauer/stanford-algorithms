from heapq import heapify

if __name__ == '__main__':
    numbers = [4, 8, 4, 9, 13, 11, 9, 4, 12]
    print('some numbers:')
    print(numbers)
    print('heapify...')
    heapify(numbers)
    print(numbers)
    numbers.append(0)
    print(numbers)
