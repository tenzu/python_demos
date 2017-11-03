#coding:utf-8
import matplotlib.pyplot as plt

x1, x2, y1, y2 = 1, 22, 1, 10
x3 = 5
y3 = (x3-x1)/(x2-x1)*(y2-y1)+y1
print('y =',y3)
plt.plot([x1,x2],[y1,y2],'or--')
plt.plot(x3,y3,'b*')
plt.annotate('(x1,y1)', xy=(x1,y1), xytext=(x1,y1))
plt.annotate('(x2,y2)', xy=(x2,y2), xytext=(x2,y2))
plt.annotate('(x3,y3)', xy=(x3,y3), xytext=(x3,y3))
plt.xlabel(u'X-axis')
plt.ylabel(u'Y-axis')
plt.show()
