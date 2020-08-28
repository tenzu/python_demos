import numpy as np
import matplotlib.pyplot as plt
a = np.zeros([3, 2])
a[0, 0] = 1
a[0, 1] = 2
a[1, 0] = 9
a[2, 1] = 12
plt.imshow(a, interpolation="nearest")
plt.show()
