# This is an example of Newmark-beta method
# to output response of a 2DOFs system.
import math
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
M1 = 2801  # mass of the 1st DOF
M2 = 2801  # mass of the 2nd DOF
K1 = 24517E3  # stiffness coefficient of the 1st DOF
K2 = 24517E3  # stiffness coefficient of the 2nd DOF
zeta1 = 0.00  # damping ratio of the 1st DOF
zeta2 = 0.00  # damping ratio of the 2nd DOF
omega_N1 = math.sqrt(K1 / M1)  # natural frequency of the 1st DOF
omega_N2 = math.sqrt(K2 / M2)  # natural frequency of the 2nd DOF
C1 = zeta1 * 2 * M1 * omega_N1  # damping coefficient of the 1st DOF
C2 = zeta2 * 2 * M2 * omega_N2  # damping coefficient of the 2nd DOF
F0 = 889.6E3  # peak force
td = 0.02  # force duration
dt = 0.0001  # time step
T = 0.2  # time to stop outputting
V10 = 0  # initial velocity of the 1st DOF
V20 = 0  # initial velocity of the 2nd DOF
U10 = 0  # initial displacement of the 1st DOF
U20 = 0  # initial displacement of the 2nd DOF
F1, A1, V1, U1 = [], [], [], [
]  # list of force, acceleration, velocity, and displacement respectively of the 1st DOF
F2, A2, V2, U2 = [], [], [], [
]  # list of force, acceleration, velocity, and displacement respectively of the 1st DOF
Tl = [i * dt for i in range(0, int(T / dt), 1)]  # list of time


def Force1(t):
    if t >= 0 and t <= td:
        # return F0 * (1 - t / td)
        return 0
    else:
        return 0


def Force2(t):
    if t >= 0 and t <= td:
        return F0 * (1 - t / td)
    else:
        return 0


for i in range(0, int(T / dt), 1):
    if i == 0:
        F1.append(Force1(i * dt))
        F2.append(Force2(i * dt))
        A1.append(Force1(i * dt) / M1)
        A2.append(Force2(i * dt) / M2)
        V1.append(V10)
        V2.append(V20)
        U1.append(U10)
        U2.append(U20)
    else:
        F1.append(Force1(i * dt))
        F2.append(Force2(i * dt))
        A1.append((Force1(i * dt) - (K1 + K2) * U1[-1] + K2 * U2[-1] -
                   (C1 + C2) * V1[-1] + C2 * V2[-1]) / M1)
        A2.append((Force2(i * dt) - K2 * U2[-1] + K2 * U1[-1] - C2 * V2[-1] +
                   C2 * V1[-1]) / M2)
        V1.append(V1[-1] + (1.0 / 2) * (A1[-2] + A1[-1]) * dt)
        V2.append(V2[-1] + (1.0 / 2) * (A2[-2] + A2[-1]) * dt)
        U1.append(U1[-1] + (V1[-2] + V1[-1]) * dt)
        U2.append(U2[-1] + (V2[-2] + V2[-1]) * dt)

f11 = interp1d(Tl, A1, kind='cubic')
f12 = interp1d(Tl, A2, kind='cubic')
f21 = interp1d(Tl, V1, kind='cubic')
f22 = interp1d(Tl, V2, kind='cubic')
f31 = interp1d(Tl, U1, kind='cubic')
f32 = interp1d(Tl, U2, kind='cubic')
plt.title('2DOFs system')
plt.xlabel(u'Time (s)')
plt.ylabel(u'Y-axis')
# plt.plot(Tl, f1(Tl), 'r-.', Tl, f2(Tl), 'g--', Tl, f3(Tl), 'b-')
plt.plot(Tl, f31(Tl), 'b-', Tl, f32(Tl), 'r-', Tl, f32(Tl) - f31(Tl), 'y--')
plt.legend(['Acceleration', 'Velocity', 'Displacement'], loc=1)

plt.show()
print("The maximum displacement of the 1st DOF would be " +
      str(("%5.3f" % (max(U1) * 1000))) + "mm.")
print("The maximum displacement of the 2nd DOF would be " +
      str(("%5.3f" % (max(U2) * 1000))) + "mm.")
