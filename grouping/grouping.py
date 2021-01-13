import random
# import os

f1 = open('students.txt', 'r')
f2 = open('groups.txt', 'w')
stulist = []


def read_students_old():
    for line in f1.readlines():
        try:
            if line[:-1].strip():
                if line.split()[3] == '重修':  # skip '重修'
                    continue
                elif line.split()[3] == '修读类别':  # skip title (if it exists)
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
stulist_len = len(stulist)
grp_len = 5
j = 1
while j <= stulist_len / grp_len:
    print('Group ' + str(j) + ':')
    f2.write('Group ' + str(j) + ':\n')
    i = 1
    while i <= grp_len:
        r_num = random.randint(0, len(stulist) - 1)
        tmp = stulist.pop(r_num)
        print(tmp)
        f2.write(tmp + '\n')
        i += 1
    print('\n')
    f2.write('\n')
    j += 1
print('Ungrouped student(s):')
f2.write('Ungrouped student(s):\n')
for i in stulist:
    print(i)
    f2.write(i + '\n')

f1.close()
f2.close()

# os.system('pause')
