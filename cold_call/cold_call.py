import random
import time

f1 = open('students.txt', 'r')
stulist = []
for line in f1.readlines():
    try:
        if line[:-1].strip():
            stulist.append(line.split('\t')[2] + '    ' + line.split('\t')[3])
    except ValueError:
        if line.split()[0] == '序号':
            continue
        else:
            print('Abnormal data!!!')
    else:
        continue
r_num = random.randint(5, 12)
print("The magic number is:"), r_num
list1 = random.sample(stulist, r_num)
for i in list1:
    print(i)
f2 = open("cc_record.txt", "a")
f2.write('Cold call on: ' +
         time.strftime('%Y-%m-%d %A %X %Z', time.localtime(time.time())) +
         '\n' + 'Totally ' + str(r_num) + ' students this time.' + '\n')
for i in list1:
    f2.write(i + '\n')
