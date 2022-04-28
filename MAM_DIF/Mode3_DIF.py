# Failure mode 3
import math

td = 0.02
p_max = 0.40E6
M0 = 1.277E5
m = 500
L = 2
v = 1.2
Q0 = 2 * M0 * v / L
DIFm = 1.00  # initial DIFm value
h = 0.3  # beam height
Iz = 5e6  # beam moment of inertia
EE = 3.25E10  # Young's modulus of C40 concrete
VV = 0.01  # fibre volumn rate
DD = 3.5E-3  # spline radius

# Phase 1
dt1 = 0.0001
p0 = p_max
t10 = 0
vs10 = 0
ys10 = 0
vm10 = 0
ym10 = 0
as10 = 1 / m * p0 + 6 / L**2 / m * M0 - 4 / L / m * Q0
am10 = 1 / m * p0 - 6 / L**2 / m * M0 + 2 / L / m * Q0
while t10 < td:
    vs10 += as10 * dt1
    ys10 += vs10 * dt1
    vm10 += am10 * dt1
    ym10 += vm10 * dt1
    p0 += -p_max * dt1 / td
    # DIFm = M0 * h / 2 / Iz / EE / dt1 / (M0 * h / 2 / Iz / EE / dt1) * 1.15
    strainRate = h**3 / 2 / ym10**2 / dt1
    if strainRate < 40:
        DIFm = 2.26 + 2.29 * VV**2 - 1.15 * DD**2 - 2.8 * VV + 1.43 * DD - 0.01 * VV * DD + (
            1.2 * VV - 0.175 * DD + 2.44) * math.log(40, 10)
    elif strainRate > 400:
        DIFm = 2.26 + 2.29 * VV**2 - 1.15 * DD**2 - 2.8 * VV + 1.43 * DD - 0.01 * VV * DD + (
            1.2 * VV - 0.175 * DD + 2.44) * math.log(400, 10)
    else:
        DIFm = 2.26 + 2.29 * VV**2 - 1.15 * DD**2 - 2.8 * VV + 1.43 * DD - 0.01 * VV * DD + (
            1.2 * VV - 0.175 * DD + 2.44) * math.log(strainRate, 10)
    print("strain rate:", strainRate)
    print(DIFm)
    as10 = 1 / m * p0 + 6 / L**2 / m * M0 - 4 / L / m * Q0
    am10 = 1 / m * p0 - 6 / L**2 / m * M0 * DIFm + 2 / L / m * Q0
    t10 += dt1

print("ym10",ym10)

# Phase 2
dt2 = 0.0001
t20 = t10
vs20 = vs10
ys20 = ys10
vm20 = vm10
ym20 = ym10
as20 = (6 * M0 - 4 * Q0 * L) / m / L**2
am20 = (-6 * M0 * DIFm + 2 * Q0 * L) / m / L**2
while vs20 > 0:
    vs20 += as20 * dt2
    ys20 += vs20 * dt2
    vm20 += am20 * dt2
    ym20 += vm20 * dt2
    DIFm = M0 * h / 2 / Iz / EE / dt2 / (M0 * h / 2 / Iz / EE / dt1) * 1.15
    as20 = (6 * M0 - 4 * Q0 * L) / m / L**2
    am20 = (-6 * M0 * DIFm + 2 * Q0 * L) / m / L**2
    t20 += dt2

print(t20)
print("ys20 =", ys20)

# Phase 3
dt3 = 0.0001
t30 = t20
vm30 = vm20
ym30 = ym20
am30 = -3 * M0 * DIFm / m / L**2
while vm30 > 0:
    vm30 += am30 * dt3
    ym30 += vm30 * dt3
    DIFm = M0 * h / 2 / Iz / EE / dt3 / (M0 * h / 2 / Iz / EE / dt1) * 1.15
    am30 = -3 * M0 * DIFm / m / L**2
    t30 += dt3

print(t30)
print("ym30 =", ym30)
