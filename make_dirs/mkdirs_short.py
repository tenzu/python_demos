import os

for i in range(1, 5, 1):
    os.makedirs('case%0.2d' % (i))
    # os.chdir('case%0.2d' % (i))
    # fp = open('test'+str(i)+'.docx','w')
    # os.chdir('../')