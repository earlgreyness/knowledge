import numpy as np
import math


def construct(n):

    def _element(i, j):
        return np.abs(i - j) + np.abs(i - j + 1)

    matrix = np.asmatrix(np.zeros(shape=(n, n)))

    for i in range(n):
        for j in range(n):
            matrix[i, j] = _element(i, j)

    return matrix


if __name__ == '__main__':

    print(construct(10))

    exit(0)

    for n in range(2, 15):
        print(n, ': ', np.linalg.det(construct(n)))

    # print(construct(8))
