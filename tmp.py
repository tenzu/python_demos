import numpy as np
import matplotlib.pyplot as plt

X=np.empty((100,2))
X[:,0]=np.random.uniform(0.,100.,size=100)
X[:,1]=0.75*X[:,0]+3+np.random.normal(0,10.,size=100)
plt.scatter(X[:,0],X[:,1])
plt.show()