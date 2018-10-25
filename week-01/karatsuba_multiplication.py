# programming assignment
def karatsuba(x, y):
    x, y = str(x), str(y)
    n = len(x)
    a, b = x[:n // 2], x[n // 2:]
    c, d = y[:n // 2], y[n // 2:]
    a, b, c, d = int(a), int(b), int(c), int(d)
    step1 = a * c
    step2 = b * d
    step3 = (a + b) * (c + d)
    step4 = str(step3 - step2 - step1)
    step5 = int(str(step1) + n * '0') \
            + step2 \
            + int(str(step4) + (n // 2) * '0')
    return step5


if __name__ == '__main__':
    # print(karatsuba(5678, 1234))
    x = 3141592653589793238462643383279502884197169399375105820974944592
    y = 2718281828459045235360287471352662497757247093699959574966967627
    print(karatsuba(x, y))
