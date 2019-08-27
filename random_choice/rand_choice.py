import random
# import os

f1 = open('students.txt', 'r')
f2 = open('rand_choice.txt', 'a')
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
a = random.choice(stulist)
print(a)
f2.write(a + '\n')

f1.close()
f2.close()

# os.system('pause')
