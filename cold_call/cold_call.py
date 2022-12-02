import random
import time
# import os

f1 = open('students.txt', 'r')
stulist = []


def read_students_old():
    for line in f1.readlines():
        try:
            if line[:-1].strip():
                if line.split()[3] == '重修':  # skip '重修'
                    continue
                else:
                    stulist.append(
                        line.split('\t')[2] + '    ' + line.split('\t')[3])
        except ValueError:
            if line.split()[0] == '序号':  # skip title (if it exists)
                continue
            else:
                print('Abnormal data!!!')  # skip '缓考', '缺考', etc.
        else:
            continue


def read_students():
    for line in f1.readlines():
        stulist.append(line.split('\t')[1] + '    ' + line.split('\t')[2])


read_students()

r_num = random.randint(1, 4)
print("The magic number is:", r_num)
list1 = random.sample(stulist, r_num)
for i in list1:
    print(i)
f2 = open("cc_record.txt", "a")
f2.write('Cold call on: ' +
         time.strftime('%Y-%m-%d %A %X %Z', time.localtime(time.time())) +
         '\n' + 'Totally ' + str(r_num) + ' students this time.' + '\n')
for i in list1:
    f2.write(i + '\n')

f1.close()
f2.close()
# os.system('pause')
