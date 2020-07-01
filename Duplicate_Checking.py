# This is a script to summarize duplicate checking resutls
# 1. 查重文件统一采用“学号_姓名_论文题目.docx”
# 2. 以每个老师的姓名建立文件夹，其学生的查重文件和结果文件都放在其中
# 3. 所有查重结果都保存详细报告（pdf文件）
import os
Parent_Dir = r'D:\teaching\FYP documents\2020\查重'  # !!!confirm the path first!!!
Sub_Dir=os.listdir(Parent_Dir)  # 查重文件路径
Current_Dir=[]  # 以老师姓名命名的子文件夹
for i in range(len(Sub_Dir)):
    Current_Dir.append(Parent_Dir+'\\'+Sub_Dir[i])  # 查重结果文件绝对路径list
PDF_Names = []  # 查重文件目录list
f = open("List.txt", "w+")
for i in Current_Dir:
    for j in os.walk(i):
        for k in j[2]:  # Debug时发现j[2]存储了查重结果文件名，小幸运
            if 'pdf' in k:  # 剔除docx格式的查重文件
                PDF_Names.append(Sub_Dir[Current_Dir.index(i)]+'_'+k)   # 反查index，生成"教师姓名_学号_姓名_论文题目-文本复制检测报告单（全文标明引文）.pdf"list
for i in range(len(PDF_Names)):
    PDF_Names[i] = PDF_Names[i].strip(
        "-文本复制检测报告单（全文标明引文）.pdf")  # 剔除无用str
    PDF_Names[i] = PDF_Names[i].split('_')  # 拆分list
for i in range(len(PDF_Names)):
    f.write(PDF_Names[i][2] + '\t' + PDF_Names[i]
            [1] + '\t' + PDF_Names[i][3] + '\t'+PDF_Names[i][0]+'\n')
f.close()
