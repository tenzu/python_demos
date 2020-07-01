# This is a script to summarize duplicate checking resutls
import os
Parent_Dir = r'D:\teaching\FYP documents\2020\查重'  # !!!confirm the path first!!!
Sub_Dir=os.listdir(Parent_Dir)
Current_Dir=[]
for i in range(len(Sub_Dir)):
    Current_Dir.append(Parent_Dir+'\\'+Sub_Dir[i])
PDF_Names = []
f = open("List.txt", "w+")
for i in Current_Dir:
    for j in os.walk(i):
        for k in j[2]:
            if 'pdf' in k:
                PDF_Names.append(Sub_Dir[Current_Dir.index(i)]+'_'+k)
for i in range(len(PDF_Names)):
    PDF_Names[i] = PDF_Names[i].strip(
        "-文本复制检测报告单（全文标明引文）.pdf")  # Filter for pdf files
    PDF_Names[i] = PDF_Names[i].split('_')
for i in range(len(PDF_Names)):
    f.write(PDF_Names[i][2] + '\t' + PDF_Names[i]
            [1] + '\t' + PDF_Names[i][3] + '\t'+PDF_Names[i][0]+'\n')
f.close()
