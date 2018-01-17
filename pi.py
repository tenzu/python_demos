import math
k = 3

def pi_1(k):
	a = 0
	for i in range(0,k,1):
		a = a + 1/16**i*(4/(8*i+1)-2/(8*i+4)-1/(8*i+5)-1/(8*i+6))
	return(a)

def pi_2(k):
	b = 0
	a0,b0,t0,p0 = 1.0,1.0/math.sqrt(2),1/4.0,1.0
	for j in range (1,k+1,1):
		a1 = (a0+b0)/2.0
		b1 = math.sqrt(a0*b0)
		t1 = t0-p0*(a0-a1)**2
		p1 = 2*p0
		a0,b0,t0,p0 = a1,b1,t1,p1
	b = (a0+b0)**2/4.0/t0
	return(b)

for k in range(1,11,1):
	print('k=',k)
	pi_1(k)
	print('pi_1=',pi_1(k))
	pi_2(k)
	print('pi_2=',pi_2(k))
