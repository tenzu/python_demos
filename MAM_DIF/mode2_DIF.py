# Failure mode 2
td = 0.02
p_max = 0.41E6
M0 = 1.277E5
m = 500
L = 2
v = 0.8
Q0 = 2*M0*v/L
DIF = 1.20

# Phase 1
dt1 = 0.0001
p0 = p_max
t10 = 0
vm10 = 0
ym10 = 0
am10 = -3*(-1/2*p0*L**2+M0)/m/L**2
while t10 < td:
    vm10 += am10*dt1
    ym10 += vm10*dt1
    p0 += -p_max*dt1/td
    am10 = -3*(-1/2*p0*L**2+M0*DIF)/m/L**2
    t10 += dt1

# Phase 2
dt2 = 0.0001
t20 = t10
vm20 = vm10
ym20 = ym10
am20 = -Q0*DIF/m/L
while vm20 > 0:
    vm20 += am20*dt2
    ym20 += vm20*dt2
    am20 = -3*M0*DIF/m/L**2
    t20 += dt2

print("am20 =",am20)
print("vm20 =",vm20)
print("ym20 =",ym20)
