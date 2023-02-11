import numpy as np


def PM(c1, p1, EAF, SIZE):
    return c1 * EAF * (SIZE ** p1)


def TM(c2, p2, PM):
    return c2 * (PM ** p2)


def EAF(params: list):
    return np.prod(params)
