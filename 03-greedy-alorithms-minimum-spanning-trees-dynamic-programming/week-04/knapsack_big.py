import sys
import threading


def main():
    with open("knapsack_big.txt", mode='r') as f:
        lines = f.readlines()

    w, n = map(int, lines[0].split())
    print(f'Knapsack size: {w}')
    print(f'number of items: {n}')

    items = [tuple(map(int, line.split())) for line in lines[1:]]
    A = dict()

    def get_max_value(i, x):
        if i == 0:
            return 0
        str_ix = str(i) + ":" + str(x)
        if str_ix in A:
            return A[str_ix]
        v_i_prev, w_i_prev = items[i - 1]
        if w_i_prev > x:
            A[str_ix] = get_max_value(i - 1, x)
        else:
            A[str_ix] = max(get_max_value(i - 1, x),
                            v_i_prev + get_max_value(i - 1, x - w_i_prev))
        return A[str_ix]

    result = get_max_value(n, w)
    print(result)  # 4243395


if __name__ == '__main__':
    threading.stack_size(64 * 1024 * 1024)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target=main)
    thread.start()
