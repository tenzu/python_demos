import random

f1 = open('students.txt', 'r')
f2 = open('groups.txt', 'w')
stulist = []
for line in f1.readlines():
    if line[:-1].strip():
        stulist.append('Class ' + line.split('\t')[2] + '    ' +
                       line.split('\t')[4] + '    ' + line.split('\t')[3])
        # stulist.append(+line.split('\t')[4])
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
