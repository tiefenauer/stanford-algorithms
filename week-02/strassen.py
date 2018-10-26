import numpy as np


def split_matrix(x):
    m = np.split(x, 2, axis=1)
    ac = np.split(m[0], 2)
    bd = np.split(m[1], 2)
    return ac[0], bd[0], ac[1], bd[1]


def strassen(x, y):
    assert x.shape == y.shape, 'X and Y must have same dimensions'
    assert x.ndim == 2, 'X and Y must be 2-dimensional'
    assert x.shape[0] == x.shape[1], 'X and Y must be a quadratic matrices'
    n = x.shape[0]
    if n == 2:
        a, b, c, d = split_matrix(x)
        e, f, g, h = split_matrix(y)
        p1 = int(a * (f - h))
        p2 = int((a + b) * h)
        p3 = int((c + d) * e)
        p4 = int(d * (g - e))
        p5 = int((a + d) * (e + h))
        p6 = int((b - d) * (g + h))
        p7 = int((a - c) * (e + f))
        return np.vstack((
            np.hstack((p5 + p4 - p2 + p6, p1 + p2)),
            np.hstack((p3 + p4, p1 + p5 - p3 - p7))
        ))

    a, b, c, d = split_matrix(x)
    e, f, g, h = split_matrix(y)
    row1 = np.hstack((strassen(a, e) + strassen(b, g), strassen(a, f) + strassen(b, h)))
    row2 = np.hstack((strassen(c, e) + strassen(d, g), strassen(c, f) + strassen(d, h)))
    return np.vstack((row1, row2))


if __name__ == '__main__':
    x = np.random.randint(128, size=(8, 8))
    y = np.random.randint(128, size=(8, 8))
    z = strassen(x, y)
    print('result of multiplying X * Y', z)
    print('result is correct:', np.array_equal(z, np.dot(x, y)))
