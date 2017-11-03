import math,numpy,random
import matplotlib.pyplot as plt
pi = math.acos(-1)  #define pi=3.14
RD = numpy.linspace(0,2*pi,360)
DISK_R = 0.0375E3   #disk radius

#Original segment center for spline
SPL_SEG = 100   #number of fibre spline segments
SPL_CR = 0.000315e3 #spline circles radius
F_LENG = 0.015E3    #fibre length (y value)
F_WIDT = 0.005E3    #fibre width (x value)
ORG_CTR = numpy.zeros((SPL_SEG+1,2))    #circle center on original spline
MIN_GAP = 1 #minimum gap between blocks

#To draw spline
for i in range(0,SPL_SEG+1):
    x = (-3./2.*pi+3.*pi/SPL_SEG*i)/(3.*pi/F_LENG)
    y = (F_WIDT/2.)*(-1)*math.cos(x*(3.*pi/2./(F_LENG/2.)))
    ORG_CTR[i,0] = x
    ORG_CTR[i,1] = y

#Location for fibres
NUM_F = 12   #fibre number
FC_CTR = numpy.zeros((NUM_F*(SPL_SEG+1),2)) #circle center on translated fibre (x, y)
F_LOCATIONS = numpy.zeros((NUM_F,3))    #fibre translation and rotation (x, y, angle)
F_CONT = 1  #fibre counter
while F_CONT <= NUM_F:
    F_AVLB = 1
    theta_F = random.randint(0.,360.)
    x_F = random.uniform(-(DISK_R-F_LENG/2.-0.00024133e3),(DISK_R-F_LENG/2.-0.00024133e3))
    y_F = random.uniform(-math.sqrt(0.02975867e3**2-x_F**2),math.sqrt(0.02975867e3**2-x_F**2))
    for i in range(0,SPL_SEG+1):
        FC_CTR[i+(F_CONT-1)*(SPL_SEG+1),0] = ORG_CTR[i,0]*math.cos(theta_F*pi/180.)-ORG_CTR[i,1]*math.sin(theta_F*pi/180.)+x_F
        FC_CTR[i+(F_CONT-1)*(SPL_SEG+1),1] = ORG_CTR[i,0]*math.sin(theta_F*pi/180.)+ORG_CTR[i,1]*math.cos(theta_F*pi/180.)+y_F
    if F_CONT <= NUM_F:
        for j in range((F_CONT-1)*(SPL_SEG+1),F_CONT*(SPL_SEG+1)):
            for k in range(1,(F_CONT-1)*(SPL_SEG+1)):
                if (FC_CTR[j,0]-FC_CTR[k,0])**2+(FC_CTR[j,1]-FC_CTR[k,1])**2 > (SPL_CR+SPL_CR)**2+MIN_GAP:
                    F_AVLB = F_AVLB*1
                else:
                    F_AVLB = F_AVLB*0
    else:
       break
    if F_AVLB == 1:
        F_LOCATIONS[F_CONT-1,0] = x_F
        F_LOCATIONS[F_CONT-1,1] = y_F
        F_LOCATIONS[F_CONT-1,2] = theta_F
        F_CONT += 1
    else:
        F_CONT = F_CONT

#Location for fibres
f1 = open('ORG_CTR.txt','w')
for i in range(len(ORG_CTR)):
    f1.write('%11.5f' % ORG_CTR[i,0] +' '+'%11.5f' % ORG_CTR[i,1] +'\n')
f1.close()
f2 = open('F_LOCATIONS.txt','w')
for i in range(len(F_LOCATIONS)):
    f2.write('%11.5f' % F_LOCATIONS[i,0] +' '+'%11.5f' % F_LOCATIONS[i,1]+' '+'%11.5f' % F_LOCATIONS[i,2] +'\n')
f2.close()
f3 = open('FC_CTR.txt','w')
for i in range(len(FC_CTR)):
    f3.write('%11.5f' % FC_CTR[i,0] +' '+'%11.5f' % FC_CTR[i,1]+'\n')
f3.close()
#plot fibres in matplob
#for i in range(0,len(ORG_CTR)):
#    cx = ORG_CTR[i,0]+SPL_CR*numpy.cos(RD)
#    cy = ORG_CTR[i,1]+SPL_CR*numpy.sin(RD)
#    plt.plot(cx,cy,'-b')
for i in range(0,len(FC_CTR)):
    cx = FC_CTR[i,0]+SPL_CR*numpy.cos(RD)
    cy = FC_CTR[i,1]+SPL_CR*numpy.sin(RD)
    plt.plot(cx,cy,'-r')

#Location for aggregate type 1
NUM_BA = 5  #number of aggregate type 1
BA_LOCATIONS = numpy.zeros((NUM_BA,3))    #aggregate translation and rotation (x, y, radius)
BA_CONT = 1  #aggregate counter
while BA_CONT <= NUM_BA:
    BA_AVLB = 1
    BA_R = random.uniform(0.004e3,0.005e3)
    x_BA = random.uniform(-(DISK_R-BA_R),DISK_R-BA_R)
    y_BA = random.uniform(-math.sqrt((DISK_R-BA_R)**2-x_BA**2),math.sqrt((DISK_R-BA_R)**2-x_BA**2))
    if BA_CONT <= NUM_BA+1:
        for i in range(0,NUM_F*(SPL_SEG+1)):
            if (FC_CTR[i,0]-x_BA)**2+(FC_CTR[i,1]-y_BA)**2 > (SPL_CR+BA_R)**2+MIN_GAP:
                BA_AVLB = BA_AVLB*1
            else:
                BA_AVLB = BA_AVLB*0
        for i in range(0,BA_CONT-1):
            if (BA_LOCATIONS[i,0]-x_BA)**2+(BA_LOCATIONS[i,1]-y_BA)**2 > (BA_LOCATIONS[i,2]+BA_R)**2+MIN_GAP:
                BA_AVLB = BA_AVLB*1
            else:
                BA_AVLB = BA_AVLB*0
    else:
        break
    if BA_AVLB == 1:
        BA_LOCATIONS[BA_CONT-1,0] = x_BA
        BA_LOCATIONS[BA_CONT-1,1] = y_BA
        BA_LOCATIONS[BA_CONT-1,2] = BA_R
        BA_CONT += 1
    else:
        BA_CONT = BA_CONT
#Record BA location
f1 = open('BA_LOCATIONS.txt','w')
for i in range(len(BA_LOCATIONS)):
    f1.write('%11.5f' % BA_LOCATIONS[i,0] +' '+'%11.5f' % BA_LOCATIONS[i,1]+' '+'%11.5f' % BA_LOCATIONS[i,2] +'\n')
f1.close()
#plot fibres in matplob
for i in range(0,len(BA_LOCATIONS)):
    cx = BA_LOCATIONS[i,0]+BA_LOCATIONS[i,2]*numpy.cos(RD)
    cy = BA_LOCATIONS[i,1]+BA_LOCATIONS[i,2]*numpy.sin(RD)
    plt.plot(cx,cy,'-y')

#Location for aggregate type 2
NUM_BB = 12  #number of aggregate type 2
BB_LOCATIONS = numpy.zeros((NUM_BB,3))    #aggregate translation and rotation (x, y, radius)
BB_CONT = 1  #aggregate counter
while BB_CONT <= NUM_BB:
    BB_AVLB = 1
    BB_R = random.uniform(0.003e3,0.004e3)
    x_BB = random.uniform(-(DISK_R-BB_R),DISK_R-BB_R)
    y_BB = random.uniform(-math.sqrt((DISK_R-BB_R)**2-x_BB**2),math.sqrt((DISK_R-BB_R)**2-x_BB**2))
    if BB_CONT <= NUM_BB:
        for i in range(0,NUM_F*(SPL_SEG+1)):
            if (FC_CTR[i,0]-x_BB)**2+(FC_CTR[i,1]-y_BB)**2 > (SPL_CR+BB_R)**2+MIN_GAP:
                BB_AVLB = BB_AVLB*1
            else:
                BB_AVLB = BB_AVLB*0
        for i in range(0,NUM_BA):
            if (BA_LOCATIONS[i,0]-x_BB)**2+(BA_LOCATIONS[i,1]-y_BB)**2 > (BA_LOCATIONS[i,2]+BB_R)**2+MIN_GAP:
                BB_AVLB = BB_AVLB*1
            else:
                BB_AVLB = BB_AVLB*0
        for i in range(0,BB_CONT-1):
            if (BB_LOCATIONS[i,0]-x_BB)**2+(BB_LOCATIONS[i,1]-y_BB)**2 > (BB_LOCATIONS[i,2]+BB_R)**2+MIN_GAP:
                BB_AVLB = BB_AVLB*1
            else:
                BB_AVLB = BB_AVLB*0
    else:
        break
    if BB_AVLB == 1:
        BB_LOCATIONS[BB_CONT-1,0] = x_BB
        BB_LOCATIONS[BB_CONT-1,1] = y_BB
        BB_LOCATIONS[BB_CONT-1,2] = BB_R
        BB_CONT += 1
    else:
        BB_CONT = BB_CONT
#Record BB location 
f1 = open('BB_LOCATIONS.txt','w')
for i in range(len(BB_LOCATIONS)):
    f1.write('%11.5f' % BB_LOCATIONS[i,0] +' '+'%11.5f' % BB_LOCATIONS[i,1]+' '+'%11.5f' % BB_LOCATIONS[i,2] +'\n')
f1.close()
#plot fibres in matplob
for i in range(0,len(BB_LOCATIONS)):
    cx = BB_LOCATIONS[i,0]+BB_LOCATIONS[i,2]*numpy.cos(RD)
    cy = BB_LOCATIONS[i,1]+BB_LOCATIONS[i,2]*numpy.sin(RD)
    plt.plot(cx,cy,'-g')

#Location for aggregate type 3
NUM_BC = 32  #number of aggregate type 3
BC_LOCATIONS = numpy.zeros((NUM_BC,3))    #aggregate translation and rotation (x, y, radius)
BC_CONT = 1  #aggregate counter
while BC_CONT <= NUM_BC:
    BC_AVLB = 1
    BC_R = random.uniform(0.002e3,0.003e3)
    x_BC = random.uniform(-(DISK_R-BC_R),DISK_R-BC_R)
    y_BC = random.uniform(-math.sqrt((DISK_R-BC_R)**2-x_BC**2),math.sqrt((DISK_R-BC_R)**2-x_BC**2))
    if BC_CONT <= NUM_BC:
        for i in range(0,NUM_F*(SPL_SEG+1)):
            if (FC_CTR[i,0]-x_BC)**2+(FC_CTR[i,1]-y_BC)**2 > (SPL_CR+BC_R)**2+MIN_GAP:
                BC_AVLB = BC_AVLB*1
            else:
                BC_AVLB = BC_AVLB*0
        for i in range(0,NUM_BA):
            if (BA_LOCATIONS[i,0]-x_BC)**2+(BA_LOCATIONS[i,1]-y_BC)**2 > (BA_LOCATIONS[i,2]+BC_R)**2+MIN_GAP:
                BC_AVLB = BC_AVLB*1
            else:
                BC_AVLB = BC_AVLB*0
        for i in range(0,NUM_BB):
            if (BB_LOCATIONS[i,0]-x_BC)**2+(BB_LOCATIONS[i,1]-y_BC)**2 > (BB_LOCATIONS[i,2]+BC_R)**2+MIN_GAP:
                BC_AVLB = BC_AVLB*1
            else:
                BC_AVLB = BC_AVLB*0
        for i in range(0,BC_CONT-1):
            if (BC_LOCATIONS[i,0]-x_BC)**2+(BC_LOCATIONS[i,1]-y_BC)**2 > (BC_LOCATIONS[i,2]+BC_R)**2+MIN_GAP:
                BC_AVLB = BC_AVLB*1
            else:
                BC_AVLB = BC_AVLB*0
    else:
        break
    if BC_AVLB == 1:
        BC_LOCATIONS[BC_CONT-1,0] = x_BC
        BC_LOCATIONS[BC_CONT-1,1] = y_BC
        BC_LOCATIONS[BC_CONT-1,2] = BC_R
        BC_CONT += 1
    else:
        BC_CONT = BC_CONT
#Record BC location
f1 = open('BC_LOCATIONS.txt','w')
for i in range(len(BC_LOCATIONS)):
    f1.write('%11.5f' % BC_LOCATIONS[i,0] +' '+'%11.5f' % BC_LOCATIONS[i,1]+' '+'%11.5f' % BC_LOCATIONS[i,2] +'\n')
f1.close()
#plot fibres in matplob
for i in range(0,len(BC_LOCATIONS)):
    cx = BC_LOCATIONS[i,0]+BC_LOCATIONS[i,2]*numpy.cos(RD)
    cy = BC_LOCATIONS[i,1]+BC_LOCATIONS[i,2]*numpy.sin(RD)
    plt.plot(cx,cy,'-b')

#Location for aggregate type 4
NUM_BD = 122  #number of aggregate type 4
BD_LOCATIONS = numpy.zeros((NUM_BD,3))    #aggregate translation and rotation (x, y, radius)
BD_CONT = 1  #aggregate counter
while BD_CONT <= NUM_BD:
    BD_AVLB = 1
    BD_R = random.uniform(0.001e3,0.002e3)
    x_BD = random.uniform(-(DISK_R-BD_R),DISK_R-BD_R)
    y_BD = random.uniform(-math.sqrt((DISK_R-BD_R)**2-x_BD**2),math.sqrt((DISK_R-BD_R)**2-x_BD**2))
    if BD_CONT <= NUM_BD:
        for i in range(0,NUM_F*(SPL_SEG+1)):
            if (FC_CTR[i,0]-x_BD)**2+(FC_CTR[i,1]-y_BD)**2 > (SPL_CR+BD_R)**2+MIN_GAP:
                BD_AVLB = BD_AVLB*1
            else:
                BD_AVLB = BD_AVLB*0
        for i in range(0,NUM_BA):
            if (BA_LOCATIONS[i,0]-x_BD)**2+(BA_LOCATIONS[i,1]-y_BD)**2 > (BA_LOCATIONS[i,2]+BD_R)**2+MIN_GAP:
                BD_AVLB = BD_AVLB*1
            else:
                BD_AVLB = BD_AVLB*0
        for i in range(0,NUM_BB):
            if (BB_LOCATIONS[i,0]-x_BD)**2+(BB_LOCATIONS[i,1]-y_BD)**2 > (BB_LOCATIONS[i,2]+BD_R)**2+MIN_GAP:
                BD_AVLB = BD_AVLB*1
            else:
                BD_AVLB = BD_AVLB*0
        for i in range(0,NUM_BC):
            if (BC_LOCATIONS[i,0]-x_BD)**2+(BC_LOCATIONS[i,1]-y_BD)**2 > (BC_LOCATIONS[i,2]+BD_R)**2+MIN_GAP:
                BD_AVLB = BD_AVLB*1
            else:
                BD_AVLB = BD_AVLB*0
        for i in range(0,BD_CONT-1):
            if (BD_LOCATIONS[i,0]-x_BD)**2+(BD_LOCATIONS[i,1]-y_BD)**2 > (BD_LOCATIONS[i,2]+BD_R)**2+MIN_GAP:
                BD_AVLB = BD_AVLB*1
            else:
                BD_AVLB = BD_AVLB*0
    else:
        break
    if BD_AVLB == 1:
        BD_LOCATIONS[BD_CONT-1,0] = x_BD
        BD_LOCATIONS[BD_CONT-1,1] = y_BD
        BD_LOCATIONS[BD_CONT-1,2] = BD_R
        BD_CONT += 1
    else:
        BD_CONT = BD_CONT
#Record BD location
f1 = open('BD_LOCATIONS.txt','w')
for i in range(len(BD_LOCATIONS)):
    f1.write('%11.5f' % BD_LOCATIONS[i,0] +' '+'%11.5f' % BD_LOCATIONS[i,1]+' '+'%11.5f' % BD_LOCATIONS[i,2] +'\n')
f1.close()
#plot fibres in matplob
for i in range(0,len(BD_LOCATIONS)):
    cx = BD_LOCATIONS[i,0]+BD_LOCATIONS[i,2]*numpy.cos(RD)
    cy = BD_LOCATIONS[i,1]+BD_LOCATIONS[i,2]*numpy.sin(RD)
    plt.plot(cx,cy,'-r')
plt.show()
