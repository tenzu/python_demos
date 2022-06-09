# coding:utf-8
import sympy as sp
import numpy as np


def eq1(heads, feet):
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    print(sp.solve([x + y - heads, 2 * x + 4 * y - feet], [x, y]))


def eq2(head, feet):
    a = np.array([[1, 1], [2, 4]])
    b = np.array([heads, feet])
    x = np.linalg.solve(a, b)
    print("There're", x[0], "roosters, and", x[1], "rabbits.")


heads = 35
feet = 94
eq1(heads, feet)
eq2(heads, feet)