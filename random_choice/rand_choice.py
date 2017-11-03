#!/usr/bin/python
#coding=utf-8
import random,time,os
f1=open('students.txt','r',encoding='utf-8')
f2=open('rand_choice.txt','a')
stulist=[]
for line in f1.readlines():
    if line[:-1].strip():
        stulist.append('Class '+line.split('\t')[2]+'    '+line.split('\t')[4]+'    '+line.split('\t')[3])
a = random.choice(stulist)
print(a)
f2.write(a+'\n')
