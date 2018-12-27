import sys
import threading


def main():
    with open("knapsack_big.txt", mode='r') as f:
        lines = f.readlines()

    w, n = map(int, lines[0].split())
    print(f'Knapsack size: {w}')
    print(f'number of items: {n}')

    weights, values = [], []
    for line in lines[1:]:
        v_i, w_i = map(int, line.split())
        weights.append(w_i)
        values.append(v_i)

    A = dict()

    def get_max_value(i, x):
        if i == 0:
            return 0
        str_ix = str(i) + ":" + str(x)
        if str_ix in A:
            return A[str_ix]
        if weights[i - 1] > x:
            A[str_ix] = get_max_value(i - 1, x)
        else:
            A[str_ix] = max(get_max_value(i - 1, x),
                            values[i - 1] + get_max_value(i - 1, x - weights[i - 1]))
        return A[str_ix]

    result = get_max_value(len(weights), w)
    print("Question2 ", result)  # 4243395


##################
# Main() to test #
##################
if __name__ == '__main__':
    threading.stack_size(64 * 1024 * 1024)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target=main)
    thread.start()
