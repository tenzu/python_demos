# This is an example of constant acceleration method
# to output response of an SDOF.
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

M = 10  # mass of SDOF
C = 2.0  # damping coefficient of SDOF
K = 25  # stiffness coefficient of SDOF
F0 = 20  # peak force
td = 5  # force duration
dt = 0.005  # time step
T = 60  # time to stop outputting
V0 = 0  # initial velocity
U0 = 0  # initial displacement
A, V, U = [], [], [
]  # list of acceleration, velocity, and displacement respectively
Tl = [i * dt for i in range(0, int(T / dt), 1)]  # list of time


def Force(t):
    if t >= 0 and t <= td:
        return F0 * (1 - t / td)
    else:
        return 0


for i in range(0, int(T / dt), 1):
    if i == 0:
        A.append(Force(i * dt) / M)
        V.append(V0)
        U.append(U0)
    else:
        A.append((Force(i * dt) - C * (V[-1] + dt / 2 * A[-1]) - K *
                  (U[-1] + dt * V[-1] + dt**2 / 4 * A[-1])) /
                 (M + dt / 2 * C + dt**2 / 4 * K))
        V.append(V[-1] + A[-1] * dt)
        U.append(U[-1] + V[-1] * dt + 0.5 * A[-1] * dt**2)

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
