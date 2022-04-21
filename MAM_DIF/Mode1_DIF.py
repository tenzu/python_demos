# Failure mode 1
td = 0.02
p_max = 0.41E6
M0 = 1.277E5
m = 500
L = 2
v = 0.8
Q0 = 2*M0*v/L
DIFs = 1.00

# Phase 1
dt1 = 0.0001
p0 = p_max
t10 = 0
vs10 = 0
ys10 = 0
as10 = -(Q0-L*p0)/(m*L)
while t10 < td:
    vs10 += as10*dt1
    ys10 += vs10*dt1
    p0 += -p_max*dt1/td
    as10 = -(DIFs*Q0-L*p0)/(m*L)
    t10 += dt1

# Phase 2
dt2 = 0.0001
t20 = t10
vs20 = vs10
ys20 = ys10
as20 = -Q0*DIFs/m/L
while vs20 > 0:
    vs20 += as20*dt2
    ys20 += vs20*dt2
    as20 = -Q0*DIFs/m/L
    t20 += dt2

print("as20 =",as20)
print("vs20 =",vs20)
print("ys20 =",ys20)
