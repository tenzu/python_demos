import os,shutil
for i in range(1,5,1):
    fp = open('test%0.2d.txt' % (i),'w')
    fp.close()
    os.chdir('case%0.2d' % (i))
    shutil.copyfile('../test%0.2d.txt' % (i),'test%0.2d.txt' % (i))
    #shutil.copyfile('..\\test%0.2d.txt' % (i),'test%0.2d.txt' % (i))
    os.chdir('../')
