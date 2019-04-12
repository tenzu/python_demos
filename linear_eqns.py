# coding:utf-8
import sympy as sp
import numpy as np


def eq1():
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    print(sp.solve([x + y - 35, 2 * x + 4 * y - 94], [x, y]))
    # print(sp.solve([x**2/9 + y**2/4 - 1, x + y - 1],[x, y]))


def eq2():
    A = np.mat('1 1;2 4')
    b = np.array([35, 94])
    x = np.linalg.solve(A, b)
    print(x)


eq1()