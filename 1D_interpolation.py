#coding:utf-8
import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
x = np.linspace(0,10,11)
y = np.cos(-x**2/9.0)
f1 = interp1d(x,y)
f2 = interp1d(x,y,kind='quadratic')
f3 = interp1d(x,y,kind='cubic')
x1 = np.linspace(0,10,51)

plt.title('1D-interpolation')
plt.xlabel(u'X-axis')
plt.ylabel(u'Y-axis')
plt.plot(x,y,'k^',x1,f1(x1),'r-',x1,f2(x1),'g--',x1,f3(x1),'b-.')
plt.legend(['data', 'linear', 'quadratic', 'cubic'], loc=3)
#plt.axis([0,10,-1.2,1.2])

plt.show()
