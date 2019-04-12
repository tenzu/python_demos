# coding:utf-8
from scipy import interpolate
import matplotlib.pyplot as plt

x0, y0 = [1, 2, 3, 4], [1, 8, 27, 64]
# x1,y1 = [float(i) for i in x0],[float(i) for i in y0]
x1, y1 = list(map(float, x0)), list(map(float, y0))
x = 5.5
print('The interpolation result is:', interpolate.lagrange(x1, y1)(x))
print('The result of x^3 is:', x**3)

plt.title('Lagrangian Interpolation')
plt.xlabel(u'X-axis')
plt.ylabel(u'Y-axis')
plt.plot(x0, y0, 'or--')
plt.plot(x, interpolate.lagrange(x1, y1)(x), '*b')
plt.show()