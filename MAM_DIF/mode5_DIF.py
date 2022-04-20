# Failure mode 5
td = 0.02
p_max = 0.42E6
M0 = 1.277E5
m = 500
L = 2
v = 1.8
Q0 = 2*M0*v/L
xi0 = (-3*M0+Q0*L)/Q0
DIF = 1.20

# Phase 1
dt1 = 0.0001
p0 = p_max
t10 = 0
vs10 = 0
ys10 = 0
vm10 = 0
ym10 = 0
as10 = 1/3/M0*(3*p0*M0-2*Q0**2)/m
am10 = p0/m
while t10 < td:
    vs10 += as10*dt1
    ys10 += vs10*dt1
    vm10 += am10*dt1
    ym10 += vm10*dt1
    p0 += -p_max*dt1/td
    as10 = 1/3/M0*DIF*(3*p0*M0*DIF-2*Q0**2*DIF**2)/m
    am10 = p0/m
    t10 += dt1

# Phase 2
dt2 = 0.0001
t20 = t10
vs20 = vs10
ys20 = ys10
vm20 = vm10
ym20 = ym10
as20 = -2/3*Q0**2*DIF**2/m/M0*DIF
am20 = 0
while t20 < 1/6*p_max*td*L**2/M0:
    vs20 += as20*dt2
    ys20 += vs20*dt2
    vm20 += am20*dt2
    ym20 += vm20*dt2
    as20 = -2/3*Q0**2*DIF**2/m/M0*DIF
    am20 = 0
    t20 += dt2

# Phase 3
dt3 = 0.0001
t30 = t20
vm30 = vm20
ym30 = ym20
am30 = 0
while t30 <1/6*p_max*td*L**2/M0 :
    vm30 += am30*dt3
    ym30 += vm30*dt3
    am30 = 0
    t30 += dt3

# Phase 4
dt4 = 0.0001
t40 = t30
vm40 = vm30
ym40 = ym30
am40 = -3*M0*DIF/m/L**2
while vm40 > 0:
    vm40 += am40*dt4
    ym40 += vm40*dt4
    am40 = -3*M0*DIF/m/L**2
    t40 += dt4

print("am40 =",am40)
print("vm40 =",vm40)
print("ym40 =",ym40)