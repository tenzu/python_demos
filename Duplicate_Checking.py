#This is a script to summarize duplicate checking resutls
import os
path = r'D:\123'
PDF_Names = []
#Final_List = []
f = open("List.txt", "w+")
for i in os.walk(path):
    for j in i[2]:
        if 'pdf' in j:
            PDF_Names.append(j)
for i in range(len(PDF_Names)):
    PDF_Names[i] = PDF_Names[i].strip(
        "-文本复制检测报告单（全文标明引文）.pdf")  #Filter for pdf files
    PDF_Names[i] = PDF_Names[i].split('_')
for i in range(len(PDF_Names)):
    #Final_List.append([PDF_Names[i][1], PDF_Names[i][0], PDF_Names[i][2]])
    f.write(PDF_Names[i][1] + '\t' + PDF_Names[i][0] + '\t' + PDF_Names[i][2] +
            '\n')
f.close()