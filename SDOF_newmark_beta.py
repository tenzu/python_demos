# This is an example of Newmark-beta method
# to output response of an SDOF.
import math
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
M = 253.3  # mass of SDOF
K = 10000  # stiffness coefficient of SDOF
zeta = 0.05  # damping ratio
omega_N = math.sqrt(K / M)  # natural frequency
C = zeta * 2 * M * omega_N  # damping coefficient of SDOF
F0 = 1000  # peak force
td = 2  # force duration
dt = 0.0001  # time step
T = 20  # time to stop outputting
V0 = 0  # initial velocity
U0 = 0  # initial displacement
F, A, V, U = [], [], [], [
]  # list of acceleration, velocity, and displacement respectively
Tl = [i * dt for i in range(0, int(T / dt), 1)]  # list of time
gamma = 1.0 / 2
beta = 1.0 / 6


def Force(t):
    if t >= 0 and t <= td:
        return F0 * (1 - t / td)
        # return F0 * math.sin(t / td * math.pi)
    else:
        return 0


for i in range(0, int(T / dt), 1):
    if i == 0:
        F.append(F0)
        A.append(F0 / M)
        V.append(V0)
        U.append(U0)
    else:
        F.append(Force(i * dt))
        A.append((1 / M) * (Force(i * dt) - C * V[-1] - K * U[-1]))
        V.append(V[-1] + (1 - gamma) * A[-2] * dt + gamma * A[-1] * dt)
        U.append(U[-1] + V[-2] * dt + (1.0 / 2 - beta) * A[-2] * dt**2 +
                 beta * A[-1] * dt**2)

f1 = interp1d(Tl, A, kind='cubic')
f2 = interp1d(Tl, V, kind='cubic')
f3 = interp1d(Tl, U, kind='cubic')
plt.title('SDOF system')
plt.xlabel(u'Time (s)')
plt.ylabel(u'Y-axis')
plt.plot(Tl, f1(Tl), 'r-.', Tl, f2(Tl), 'g--', Tl, f3(Tl), 'b-')
plt.legend(['Acceleration', 'Velocity', 'Displacement'], loc=1)

plt.show()
print("The maximum displacement would be " + str(max(U)) + ".")
