# Failure mode 4
td = 0.02
p_max = 0.42E6
M0 = 1.277E5
m = 500
L = 2
v = 1.8
Q0 = 2*M0*v/L
DIFm = 1.00 # initial DIFm value
h = 0.3     # beam height
Iz = 5e6    # beam moment of inertia
EE = 3.25E10    # Young's modulus of C40 concrete

# Phase 1
dt1 = 0.0001
p0 = p_max
t10 = 0
vm10 = 0
ym10 = 0
am10 = p0/m
while t10 < td:
    vm10 += am10*dt1
    ym10 += vm10*dt1
    p0 += -p_max*dt1/td
    DIFm = M0*h/2/Iz/EE/dt1/(M0*h/2/Iz/EE/dt1)*1.20
    am10 = p0/m
    t10 += dt1

# Phase 2
dt2 = 0.0001
t20 = t10
vm20 = vm10
ym20 = ym10
am20 = 0
while t20 < 1/6*p_max*td*L**2/M0:
    vm20 += am20*dt2
    ym20 += vm20*dt2
    DIFm = M0*h/2/Iz/EE/dt2/(M0*h/2/Iz/EE/dt1)*1.20
    am20 = 0
    t20 += dt2

# Phase 3
dt3 = 0.0001
t30 = t20
vm30 = vm20
ym30 = ym20
am30 = -3*M0*DIFm/m/L**2
while vm30 > 0:
    vm30 += am30*dt3
    ym30 += vm30*dt3
    DIFm = M0*h/2/Iz/EE/dt2/(M0*h/2/Iz/EE/dt1)*1.20
    am30 = -3*M0*DIFm/m/L**2
    t30 += dt3

print("am30 =",am30)
print("vm30 =",vm30)
print("ym30 =",ym30)