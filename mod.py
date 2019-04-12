# coding:utf-8
i = 1
while True:
    if i % 3 == 2 and i % 5 == 4 and i % 7 == 6 and i % 9 == 8 and i % 11 == 0:
        print(i)
        break
    else:
        i += 1