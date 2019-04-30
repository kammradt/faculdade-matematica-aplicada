import numpy as np


def main():
    """
    | 1  -2  -2  : -1 |
    | 1  -1   1  : -2 |
    | 2   1   3  :  1 |
    """

    A = [[1, -2, -2],
         [1, -1,  1],
         [2,  1,  3]]

    b = [-1, -2, 1]

    x = np.linalg.solve(A, b)


if __name__ == '__main__':
    main()