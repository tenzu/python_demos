import numpy as np
from numpy.lib.function_base import percentile
import pygal
import os

# global variables
currentPath = os.getcwd()   # get current path
files = os.listdir(currentPath)  # collect all files in current path
txtFiles = []   # names of txt files will be stored in this list
groupList = []  # data from different txt files will be stored in this list


def fileOpen():  # filter all txt files in current path
    for txt in files:
        if 'txt' in txt:  # filter all txt files
            txtFiles.append(txt)


def mainProc():
    groupName = globals()
    stu_numbers = []  # student campus number
    stu_names = []  # student name
    usual_performances = []  # usual performance
    exam_performances = []  # final exam performance
    final_scores = []  # score summary
    frequencies = [0, 0, 0, 0, 0]  # frequencies of score levels
    percentage = [0, 0, 0, 0, 0]  # percentage of score levels
    scores_0 = []  # scores of level 1
    scores_1 = []  # scores of level 2
    scores_2 = []  # scores of level 3
    scores_3 = []  # scores of level 4
    scores_4 = []  # scores of level 5

    for line in f.readlines():
        try:
            if line[:-1].strip():
                stu_numbers.append(line.split()[1])
                stu_names.append(line.split()[2])
                usual_performances.append(int(line.split()[5]))
                exam_performances.append(int(line.split()[4]))
                final_scores.append(int(line.split()[7]))
        except ValueError:
            if line.split()[0] == '序号':
                continue
            else:
                print(line.split()[1] + ' ' + line.split()[2] +
                      ' abnormal data!!!')
        else:
            continue
    for value in final_scores:
        if int(value) >= 0 and int(value) < 60:
            scores_0.append(value)
            frequencies[0] += 1  # frequency of level 1
        elif int(value) >= 60 and int(value) < 70:
            scores_1.append(value)
            frequencies[1] += 1  # frequency of level 2
        elif int(value) >= 70 and int(value) < 80:
            scores_2.append(value)
            frequencies[2] += 1  # frequency of level 3
        elif int(value) >= 80 and int(value) < 90:
            scores_3.append(value)
            frequencies[3] += 1  # frequency of level 4
        elif int(value) >= 90 and int(value) <= 100:
            scores_4.append(value)
            frequencies[4] += 1  # frequency of level 5
        else:
            print("Score error!")
            break
    for i in range(len(percentage)):
        percentage[i] = frequencies[i]/len(stu_numbers)

    mean = [
        np.mean(scores_0),
        np.mean(scores_1),
        np.mean(scores_2),
        np.mean(scores_3),
        np.mean(scores_4)
    ]  # mean of levels
    std = [
        np.std(scores_0),
        np.std(scores_1),
        np.std(scores_2),
        np.std(scores_3),
        np.std(scores_4)
    ]  # standard deviations of levels

    groupName['group' + txt[:4]] = [
        stu_numbers, stu_names, usual_performances, exam_performances,
        final_scores, percentage, scores_0, scores_1, scores_2, scores_3,
        scores_4, mean, std
    ]
    groupList.append(groupName['group' + txt[:4]])


def barChart1Plotting():
    final_score_bar1 = pygal.Bar()
    final_score_bar1.title = "最终成绩区间 (%)"
    # final_score_bar1.title = "Final score intervals (%)"
    final_score_bar1.x_labels = [
        '不及格', '60 - 70', '70 - 80', '80 - 90', '90 - 100'
    ]
    final_score_bar1._x_title = "Final score intervals"
    final_score_bar1._y_title = "Final score frequency"
    for txt in txtFiles:
        final_score_bar1.add(
            txt[:4] + ' ' + str(len(groupList[txtFiles.index(txt)][0])) + "人", groupList[txtFiles.index(txt)][5])
        final_score_bar1.render_to_file('Final_score_bar1.svg')


def barChart2Plotting():
    final_score_bar2 = pygal.Bar()
    final_score_bar2.title = "最终成绩均值和标准差"
    final_score_bar2.x_labels = [
        '不及格', '60 - 70', '70 - 80', '80 - 90', '90 - 100'
    ]
    final_score_bar2._x_title = "Final score intervals"
    final_score_bar2._y_title = "Final score means and STD.s"
    for txt in txtFiles:
        final_score_bar2.add(
            "均值 " + txt[:4], groupList[txtFiles.index(txt)][11])
        final_score_bar2.add(
            "标准差 " + txt[:4], groupList[txtFiles.index(txt)][12])
    final_score_bar2.render_to_file('Final_score_bar2.svg')


def pieChartPlotting():
    final_score_pie = pygal.Pie()
    final_score_pie.title = "Final score percentage (%)"
    for i in range(len(groupList)):
        final_score_pie.add(
            '90 - 100', groupList[i][11][4] / len(groupList[0]) * 100)
        final_score_pie.add(
            '80 - 90', groupList[i][11][3] / len(groupList[0]) * 100)
        final_score_pie.add(
            '70 - 80', groupList[i][11][2] / len(groupList[0]) * 100)
        final_score_pie.add(
            '60 - 70', groupList[i][11][1] / len(groupList[0]) * 100)
        final_score_pie.add(
            '不及格', groupList[i][11][0] / len(groupList[0]) * 100)
    final_score_pie.render_to_file('Final_score_pie.svg')


fileOpen()
for txt in txtFiles:
    print(txt + " is under processing.")
    f = open(txt, 'r', encoding='UTF-8')
    mainProc()
    f.close()
    print(txt + ' finished.')
print('All files finished.')
barChart1Plotting()
barChart2Plotting()
print("Finished!")
