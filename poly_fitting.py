# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 101)
y = x ** 3 + 10
z = np.polyfit(x, y, 3)  # curve fitting by cubic polynomial
p = np.poly1d(z)
yvals = np.polyval(z, x)
print(p)

plt.title('Poly-fitting')
plt.xlabel(u'X-axis')
plt.ylabel(u'Y-axis')
plot1 = plt.plot(x, y, 'b*')
plot2 = plt.plot(x, yvals, 'r--')
# plt.axis([0,3,0,30])
plt.legend(['Original data', 'Fitted Curve'], loc=2)
plt.show()
