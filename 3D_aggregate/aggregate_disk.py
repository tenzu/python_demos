import math,random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
RD1 = np.linspace(0,2*np.pi,8)
RD2 = np.linspace(0,np.pi,8)
TD_RATIO = 0.4
DISK_R = 0.0375e3   #disk radius
DISK_T = DISK_R*TD_RATIO    #disk thickness
MIN_GAP = 0.0002e3   #minimum gap between blocks
#prepare for matlibplot plotting
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.set_xlim([-DISK_R,DISK_R])
ax.set_ylim([-DISK_R,DISK_R])
ax.set_zlim([-DISK_R,DISK_R])   #for plotting unstreched model
#ax.set_zlim([-DISK_T/2,DISK_T/2])  #actural z boundary
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#Location for aggregate type A
NUM_BA = 5  #number of aggregate type A
BA_LOCATIONS = np.zeros((NUM_BA,4))    #aggregate translation and rotation (x, y, z, radius)
BA_CONT = 1  #aggregate counter
while BA_CONT <= NUM_BA:
    BA_AVLB = 1
    BA_R = random.uniform(0.004e3,0.005e3)
    x_BA = random.uniform(-(DISK_R-BA_R-MIN_GAP),DISK_R-BA_R-MIN_GAP)
    y_BA = random.uniform(-(math.sqrt((DISK_R-BA_R)**2-x_BA**2)-MIN_GAP),math.sqrt((DISK_R-BA_R)**2-x_BA**2)-MIN_GAP)
    z_BA = random.uniform(-(DISK_T/2-BA_R-MIN_GAP),DISK_T/2-BA_R-MIN_GAP)
    if BA_CONT <= NUM_BA+1:
       for i in range(0,BA_CONT-1):
            if (BA_LOCATIONS[i,0]-x_BA)**2+(BA_LOCATIONS[i,1]-y_BA)**2+(BA_LOCATIONS[i,2]-z_BA)**2 > (BA_LOCATIONS[i,3]+BA_R)**2+MIN_GAP:
                BA_AVLB = BA_AVLB*1
            else:
                BA_AVLB = BA_AVLB*0
    else:
        break
    if BA_AVLB == 1:
        BA_LOCATIONS[BA_CONT-1,0] = x_BA
        BA_LOCATIONS[BA_CONT-1,1] = y_BA
        BA_LOCATIONS[BA_CONT-1,2] = z_BA
        BA_LOCATIONS[BA_CONT-1,3] = BA_R
        BA_CONT += 1
    else:
        BA_CONT = BA_CONT
#Record BA location
f1 = open('BA_LOCATIONS.txt','w')
for i in range(len(BA_LOCATIONS)):
    f1.write('%11.5f' % BA_LOCATIONS[i,0] +' '+'%11.5f' % BA_LOCATIONS[i,1]+' '+'%11.5f' % BA_LOCATIONS[i,2] +' '+'%11.5f' % BA_LOCATIONS[i,3] +'\n')
f1.close()
#plot aggregate type A in matplob
for i in range(0,len(BA_LOCATIONS)):
    cx = BA_LOCATIONS[i,0]+BA_LOCATIONS[i,3]*np.outer(np.cos(RD1), np.sin(RD2))
    cy = BA_LOCATIONS[i,1]+BA_LOCATIONS[i,3]*np.outer(np.sin(RD1), np.sin(RD2))
    cz = BA_LOCATIONS[i,2]+BA_LOCATIONS[i,3]*np.outer(np.ones(np.size(RD1)), np.cos(RD2))
    ax.plot_surface(cx,cy,cz,color='y')

#Location for aggregate type B
NUM_BB = 12  #number of aggregate type B
BB_LOCATIONS = np.zeros((NUM_BB,4))    #aggregate translation and rotation (x, y, z, radius)
BB_CONT = 1  #aggregate counter
while BB_CONT <= NUM_BB:
    BB_AVLB = 1
    BB_R = random.uniform(0.003e3,0.004e3)
    x_BB = random.uniform(-(DISK_R-BB_R-MIN_GAP),DISK_R-BB_R-MIN_GAP)
    y_BB = random.uniform(-(math.sqrt((DISK_R-BB_R)**2-x_BB**2)-MIN_GAP),math.sqrt((DISK_R-BB_R)**2-x_BB**2)-MIN_GAP)
    z_BB = random.uniform(-(DISK_T/2-BB_R-MIN_GAP),DISK_T/2-BB_R-MIN_GAP)
    if BB_CONT <= NUM_BB:
        for i in range(0,NUM_BA):
            if (BA_LOCATIONS[i,0]-x_BB)**2+(BA_LOCATIONS[i,1]-y_BB)**2+(BA_LOCATIONS[i,2]-z_BB)**2 > (BA_LOCATIONS[i,3]+BB_R)**2+MIN_GAP:
                BB_AVLB = BB_AVLB*1
            else:
                BB_AVLB = BB_AVLB*0
        for i in range(0,BB_CONT-1):
            if (BB_LOCATIONS[i,0]-x_BB)**2+(BB_LOCATIONS[i,1]-y_BB)**2+(BB_LOCATIONS[i,2]-z_BB)**2 > (BB_LOCATIONS[i,3]+BB_R)**2+MIN_GAP:
                BB_AVLB = BB_AVLB*1
            else:
                BB_AVLB = BB_AVLB*0
    else:
        break
    if BB_AVLB == 1:
        BB_LOCATIONS[BB_CONT-1,0] = x_BB
        BB_LOCATIONS[BB_CONT-1,1] = y_BB
        BB_LOCATIONS[BB_CONT-1,2] = z_BB
        BB_LOCATIONS[BB_CONT-1,3] = BB_R
        BB_CONT += 1
    else:
        BB_CONT = BB_CONT
#Record BB location 
f1 = open('BB_LOCATIONS.txt','w')
for i in range(len(BB_LOCATIONS)):
    f1.write('%11.5f' % BB_LOCATIONS[i,0] +' '+'%11.5f' % BB_LOCATIONS[i,1]+' '+'%11.5f' % BB_LOCATIONS[i,2] +' '+'%11.5f' % BB_LOCATIONS[i,3] +'\n')
f1.close()
#plot aggregate type B in matplob
for i in range(0,len(BB_LOCATIONS)):
    cx = BB_LOCATIONS[i,0]+BB_LOCATIONS[i,3]*np.outer(np.cos(RD1), np.sin(RD2))
    cy = BB_LOCATIONS[i,1]+BB_LOCATIONS[i,3]*np.outer(np.sin(RD1), np.sin(RD2))
    cz = BB_LOCATIONS[i,2]+BB_LOCATIONS[i,3]*np.outer(np.ones(np.size(RD1)), np.cos(RD2))
    ax.plot_surface(cx,cy,cz,color='g')

#Location for aggregate type B
NUM_BC = 32  #number of aggregate type B
BC_LOCATIONS = np.zeros((NUM_BC,4))    #aggregate translation and rotation (x, y, z, radius)
BC_CONT = 1  #aggregate counter
while BC_CONT <= NUM_BC:
    BC_AVLB = 1
    BC_R = random.uniform(0.002e3,0.003e3)
    x_BC = random.uniform(-(DISK_R-BC_R-MIN_GAP),DISK_R-BC_R-MIN_GAP)
    y_BC = random.uniform(-(math.sqrt((DISK_R-BC_R)**2-x_BC**2)-MIN_GAP),math.sqrt((DISK_R-BC_R)**2-x_BC**2)-MIN_GAP)
    z_BC = random.uniform(-(DISK_T/2-BC_R-MIN_GAP),DISK_T/2-BC_R-MIN_GAP)
    if BC_CONT <= NUM_BC:
        for i in range(0,NUM_BA):
            if (BA_LOCATIONS[i,0]-x_BC)**2+(BA_LOCATIONS[i,1]-y_BC)**2+(BA_LOCATIONS[i,2]-z_BC)**2 > (BA_LOCATIONS[i,3]+BC_R)**2+MIN_GAP:
                BC_AVLB = BC_AVLB*1
            else:
                BC_AVLB = BC_AVLB*0
        for i in range(0,NUM_BB):
            if (BB_LOCATIONS[i,0]-x_BC)**2+(BB_LOCATIONS[i,1]-y_BC)**2+(BB_LOCATIONS[i,2]-z_BC)**2 > (BB_LOCATIONS[i,3]+BC_R)**2+MIN_GAP:
                BC_AVLB = BC_AVLB*1
            else:
                BC_AVLB = BC_AVLB*0
        for i in range(0,BC_CONT-1):
            if (BC_LOCATIONS[i,0]-x_BC)**2+(BC_LOCATIONS[i,1]-y_BC)**2+(BC_LOCATIONS[i,2]-z_BC)**2 > (BC_LOCATIONS[i,3]+BC_R)**2+MIN_GAP:
                BC_AVLB = BC_AVLB*1
            else:
                BC_AVLB = BC_AVLB*0
    else:
        break
    if BC_AVLB == 1:
        BC_LOCATIONS[BC_CONT-1,0] = x_BC
        BC_LOCATIONS[BC_CONT-1,1] = y_BC
        BC_LOCATIONS[BC_CONT-1,2] = z_BC
        BC_LOCATIONS[BC_CONT-1,3] = BC_R
        BC_CONT += 1
    else:
        BC_CONT = BC_CONT
#Record BC location
f1 = open('BC_LOCATIONS.txt','w')
for i in range(len(BC_LOCATIONS)):
    f1.write('%11.5f' % BC_LOCATIONS[i,0] +' '+'%11.5f' % BC_LOCATIONS[i,1]+' '+'%11.5f' % BC_LOCATIONS[i,2] +' '+'%11.5f' % BC_LOCATIONS[i,3] +'\n')
f1.close()
#plot aggregate type C in matplob
for i in range(0,len(BC_LOCATIONS)):
    cx = BC_LOCATIONS[i,0]+BC_LOCATIONS[i,3]*np.outer(np.cos(RD1), np.sin(RD2))
    cy = BC_LOCATIONS[i,1]+BC_LOCATIONS[i,3]*np.outer(np.sin(RD1), np.sin(RD2))
    cz = BC_LOCATIONS[i,2]+BC_LOCATIONS[i,3]*np.outer(np.ones(np.size(RD1)), np.cos(RD2))
    ax.plot_surface(cx,cy,cz,color='b')

#Location for aggregate type D
NUM_BD = 122  #number of aggregate type D
BD_LOCATIONS = np.zeros((NUM_BD,4))    #aggregate translation and rotation (x, y, z, radius)
BD_CONT = 1  #aggregate counter
while BD_CONT <= NUM_BD:
    BD_AVLB = 1
    BD_R = random.uniform(0.001e3,0.002e3)
    x_BD = random.uniform(-(DISK_R-BD_R-MIN_GAP),DISK_R-BD_R-MIN_GAP)
    y_BD = random.uniform(-(math.sqrt((DISK_R-BD_R)**2-x_BD**2)-MIN_GAP),math.sqrt((DISK_R-BD_R)**2-x_BD**2)-MIN_GAP)
    z_BD = random.uniform(-(DISK_T/2-BD_R-MIN_GAP),DISK_T/2-BD_R-MIN_GAP)
    if BD_CONT <= NUM_BD:
        for i in range(0,NUM_BA):
            if (BA_LOCATIONS[i,0]-x_BD)**2+(BA_LOCATIONS[i,1]-y_BD)**2+(BA_LOCATIONS[i,2]-z_BD)**2 > (BA_LOCATIONS[i,3]+BD_R)**2+MIN_GAP:
                BD_AVLB = BD_AVLB*1
            else:
                BD_AVLB = BD_AVLB*0
        for i in range(0,NUM_BB):
            if (BB_LOCATIONS[i,0]-x_BD)**2+(BB_LOCATIONS[i,1]-y_BD)**2+(BB_LOCATIONS[i,2]-z_BD)**2 > (BB_LOCATIONS[i,3]+BD_R)**2+MIN_GAP:
                BD_AVLB = BD_AVLB*1
            else:
                BD_AVLB = BD_AVLB*0
        for i in range(0,NUM_BC):
            if (BC_LOCATIONS[i,0]-x_BD)**2+(BC_LOCATIONS[i,1]-y_BD)**2+(BC_LOCATIONS[i,2]-z_BD)**2 > (BC_LOCATIONS[i,3]+BD_R)**2+MIN_GAP:
                BD_AVLB = BD_AVLB*1
            else:
                BD_AVLB = BD_AVLB*0
        for i in range(0,BD_CONT-1):
            if (BD_LOCATIONS[i,0]-x_BD)**2+(BD_LOCATIONS[i,1]-y_BD)**2+(BD_LOCATIONS[i,2]-z_BD)**2 > (BD_LOCATIONS[i,3]+BD_R)**2+MIN_GAP:
                BD_AVLB = BD_AVLB*1
            else:
                BD_AVLB = BD_AVLB*0
    else:
        break
    if BD_AVLB == 1:
        BD_LOCATIONS[BD_CONT-1,0] = x_BD
        BD_LOCATIONS[BD_CONT-1,1] = y_BD
        BD_LOCATIONS[BD_CONT-1,2] = z_BD
        BD_LOCATIONS[BD_CONT-1,3] = BD_R
        BD_CONT += 1
    else:
        BD_CONT = BD_CONT
#Record BD location
f1 = open('BD_LOCATIONS.txt','w')
for i in range(len(BD_LOCATIONS)):
    f1.write('%11.5f' % BD_LOCATIONS[i,0] +' '+'%11.5f' % BD_LOCATIONS[i,1]+' '+'%11.5f' % BD_LOCATIONS[i,2] +' '+'%11.5f' % BD_LOCATIONS[i,3] +'\n')
f1.close()
#plot aggregate type D in matplob
for i in range(0,len(BD_LOCATIONS)):
    cx = BD_LOCATIONS[i,0]+BD_LOCATIONS[i,3]*np.outer(np.cos(RD1), np.sin(RD2))
    cy = BD_LOCATIONS[i,1]+BD_LOCATIONS[i,3]*np.outer(np.sin(RD1), np.sin(RD2))
    cz = BD_LOCATIONS[i,2]+BD_LOCATIONS[i,3]*np.outer(np.ones(np.size(RD1)), np.cos(RD2))
    ax.plot_surface(cx,cy,cz,color='r')

plt.show()
