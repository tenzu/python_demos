#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.arange(0,2*np.pi+np.pi/4,2*np.pi/8)
y = np.sin(x)
f = interpolate.splrep(x,y)
x1 = np.arange(0,2*np.pi+np.pi/4,np.pi/50)
y1 = interpolate.splev(x1,f)

plt.title('Spline Interpolation')
plt.xlabel(u'X-axis')
plt.ylabel(u'Y-axis')
plt.plot(x,y,'k+',x,y,'g:',x1,y1,'b--',x1,np.sin(x1),'r-.')
plt.axis([-0.05,2*np.pi+0.05,-1.05,1.05])
plt.legend(['Data','Linear','Cubic Spline','True'],loc=3)
plt.show()
