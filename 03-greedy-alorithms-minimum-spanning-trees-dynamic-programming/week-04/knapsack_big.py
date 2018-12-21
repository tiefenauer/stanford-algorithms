# https://github.com/diogojapinto/algorithms-python/blob/master/knapsack.py
####################################
# Algo2 Week3                      #
# Knapsack Algorithm               #
####################################

import threading, sys


class Knapsack:
    """Knapsack recursive algorithm implementation for integral weights"""

    def __init__(self, items, weights, values):
        """three lists"""
        self.nbItems = len(items)
        self.items = items
        self.weights = weights
        self.values = values

    def getMaxValue(self, w):
        """return the maximum sum of items'values such that the total weight <= W"""
        self.A = dict()
        return (self._recurseMaxValue(self.nbItems, w))

    def _recurseMaxValue(self, i, x):
        """recursively compute the value self.A[i][x]"""
        if i == 0:
            return 0
        str_ix = str(i) + ":" + str(x)
        if str_ix in self.A:
            return self.A[str_ix]
        if self.weights[i - 1] > x:
            self.A[str_ix] = self._recurseMaxValue(i - 1, x)
        else:
            self.A[str_ix] = max(self._recurseMaxValue(i - 1, x),
                                 self.values[i - 1] + self._recurseMaxValue(i - 1, x - self.weights[i - 1]))
        return self.A[str_ix]


def main():
    with open("knapsack_big.txt", mode='r') as f:
        # 1st line is [knapsack_size][number_of_items]
        w, nbItems = f.readline().split()
        print(w, nbItems)
        w = int(w)
        items, weights, values = [], [], []
        i = 1
        for line in f:
            v_i, w_i = line.split()
            v_i, w_i = int(v_i), int(w_i)
            items.append(i)
            i += 1
            weights.append(w_i)
            values.append(v_i)
        algo = Knapsack(items, weights, values)
        print("Question2 ", algo.getMaxValue(w))


##################
# Main() to test #
##################
if __name__ == '__main__':
    # For Question 1, just uncomment the following sub section
    ##    with open("knapsack1.txt", mode='r') as f:
    ##        #1st line is [knapsack_size][number_of_items]
    ##        w, nbItems = f.readline().split()
    ##        w = int(w)
    ##        items, weights, values = [], [], []
    ##        i = 1
    ##        for line in f:
    ##            v_i, w_i = line.split()
    ##            v_i, w_i = int(v_i), int(w_i)
    ##            items.append(i)
    ##            i += 1
    ##            weights.append(w_i)
    ##            values.append(v_i)
    ##        algo = Knapsack(items, weights, values)
    ##        print("Question1 ", algo.getMaxValue(w))
    ##
    ##

    # In summary, sys.setrecursionlimit is just a limit enforced by the interpreter itself.
    # threading.stack_size lets you manipulate the actual limit imposed by the OS. If you hit the latter limit first, Python will just crash completely.
    threading.stack_size(67108864)  # 64MB stack
    # to avoid RuntimeError: maximum recursion depth exceeded because by default 1000 is the limit returnt by sys.getrecursionlimit()
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target=main)  # instantiate thread object
    thread.start()  # run program at target

