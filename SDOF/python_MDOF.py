import numpy as np
import pandas as pd 
import math 

#number of dof
mdof_num = int(input('number of degree of freedom: '))

#input[k],[m],[c]
m = np.asmatrix(np.identity(mdof_num)) #type:mat
print('input m in turn')
for i in range(0,mdof_num):
    m[i,i] = float(input()) 
 
k = np.asmatrix(np.zeros((mdof_num,mdof_num)))
kk = list(range(0,mdof_num+1))
print('input k in turn')
for i in range(1,mdof_num+1):
    kk[i] = float(input())
for i in range(0,mdof_num):
    for j in range(i-1,i+2):
        if 0 <= j < mdof_num and i == j:
            k[i,j] = (-1)**(i+j)*(kk[i]+kk[i+1])  
        elif 0 <= j < mdof_num and i > j: 
            k[i,j] = (-1)**(i+j)*kk[i]  
        elif 0 <= j < mdof_num and i < j: 
            k[i,j] = (-1)**(i+j)*kk[i+1] 

###Proportional Damping            
a = 0.05
b = 0.02
c = a*m +b*k  


#parameter
ts = float(input('time step:'))      #time step
moment = 10                 #calculating time
num = math.ceil(moment/ts)  ### num = t_num-1
alfa = 0.25
beta = 0.5                    #newmark—beta parameter
  
a0 = 1/(alfa*ts*ts)
a1 = beta/(alfa*ts)
a2 = 1/(alfa*ts)
a3 = 1/(2*alfa)-1
a4 = beta/alfa-1
a5 = ts/2*(beta/alfa-2)
a6 = ts*(1-beta)
a7 = beta*ts

#set matrix
t = list(np.arange(0,moment,ts)) 
t.append(moment)
p = np.asmatrix(np.zeros((num+1,mdof_num)))   
d = np.asmatrix(np.zeros((num+1,mdof_num)))
v = np.asmatrix(np.zeros((num+1,mdof_num)))
a = np.asmatrix(np.zeros((num+1,mdof_num)))

#load (need to set) i:dof j:number of iteration 
for i in range(0,mdof_num):
    if i == 111:                 #rectangular load
        pp = 300
        td = 0.4
        for j in range(0,num+1):
            if t[j]<=td:
                p[j,i] = pp
            else:
                p[j,i] = 0
    elif i == 111:                  #triangle load
        for j in range(0,num+1):
            if t[j]<=0.2:
                p[j,i] = 3000*t[j]
            elif t[j]>0.2 and t[j]<=0.4:
                p[j,i] = 1200-3000*t[j]
            else:
                p[j,i] = 0   
    elif i == 111:                   #right triangle load
        p0 = 600
        td = 0.4
        for j in range(0,num+1):
            if t[j] >= 0 and t[j] <= td:
                p[j,i] = p0*(1 - t[j]/td)
            else:
                p[j,i] = 0
    elif i == 0:                 #simple harmonic load
        p0 = 100
        td = 5
        pi = math.cos(-1)
        for j in range(0,num+1):
            if t[j] <= td: 
                p[j,i] = p0*(math.sin(4*pi*t[j]/td))
            else:
                p[j,i] = 0 

#equation
ke = k+a0*m+a1*c
for i in range(0,num):
    pe = p[i+1,:].T + m*((a0*d[i,:] + a2*v[i,:] + a3*a[i,:]).T) + c*((a1*d[i,:] + a4*v[i,:] + a5*a[i,:]).T)
    d[i+1,:] = (ke.I * pe).T
    a[i+1,:] = a0*(d[i+1,:]-d[i,:])-a2*v[i,:]-a3*a[i+1,:]
    v[i+1,:] = a[i+1,:] + a6*a[i,:] + a7*a[i+1,:]

#save to file
df = pd.DataFrame(d)
df.to_csv('displacement.txt')
vf = pd.DataFrame(v)
df.to_csv('velocity.txt')
af = pd.DataFrame(a)
df.to_csv('acceleration.txt')


