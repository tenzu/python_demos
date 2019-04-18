# This is an example of constant acceleration method
# to output response of an SDOF.
# The spline interpolation method requires smaller timestep.
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
M = 10  # mass of SDOF
C = 2.0  # damping coefficient of SDOF
K = 25  # stiffness coefficient of SDOF
F0 = 20  # peak force
td = 5  # force duration
dt = 0.001  # time step
T = 60  # time to stop outputting
V0 = 0  # initial velocity
U0 = 0  # initial displacement
A, V, U = np.zeros(int(T / dt)), np.zeros(int(T / dt)), np.zeros(int(
    T / dt))  # list of acceleration, velocity, and displacement respectively
Tl = np.array([i * dt for i in range(0, int(T / dt), 1)])  # list of time


def Force(t):
    if t >= 0 and t <= td:
        return F0 * (1 - t / td)
    else:
        return 0


for i in range(0, int(T / dt), 1):
    if i == 0:
        V[i] = V0
        U[i] = U0
        A[i] = Force(i * dt) / M
    else:
        A[i] = (1 / M) * (Force(i * dt) - C * V[i - 1] - K * U[i - 1])
        V[i] = V[i - 1] + A[i - 1] * dt
        U[i] = U[i - 1] + V[i - 1] * dt + 0.5 * A[i - 1] * dt**2

f1 = interpolate.splrep(Tl, A)
A1 = interpolate.splev(Tl, f1)
f2 = interpolate.splrep(Tl, V)
V1 = interpolate.splev(Tl, f2)
f3 = interpolate.splrep(Tl, U)
U1 = interpolate.splev(Tl, f3)

plt.title('SDOF system')
plt.xlabel(u'Time (s)')
plt.ylabel(u'Y-axis')
plt.plot(Tl, A1, 'r-.', Tl, V1, 'g--', Tl, U1, 'b-')
plt.legend(['Acceleration', 'Velocity', 'Displacement'], loc=1)

plt.show()
print("The maximum displacement would be " + str(np.amax(U)) + ".")
